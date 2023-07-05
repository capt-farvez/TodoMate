from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

class TodoListView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        todos = self.get_queryset()
        return render(request, 'home.html', {'todos': todos})


@csrf_exempt
def todos_list(request):

    if request.method == 'GET':
        tod = Todo.objects.all()
        serializer = TodoSerializer(tod, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)