from django.shortcuts import render, redirect
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
        # print(todos)
        return render(request, 'home.html', {'todos': todos})

def addTodo(request):
    title = ""  # Default value for title
    description = ""  # Default value for description

    if request.method == 'POST':
        print(request.POST)

        title = request.POST.get("title")
        print(title)
        description = request.POST.get("description")
        todos = Todo(title=title, description=description)
        todos.save()
        print(todos)
        # print(Todo.objects.all())
        return redirect('/')

    return render(request, 'addNewTodo.html', {'title':title, 'description':description})

def delete_todo(request, pk):
    todos = Todo.objects.get(pk=pk)
    todos.delete()
    return redirect('/')

def update_todo(request, pk):
    todos = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        todos.title = title
        todos.description = description
        todos.save()
        return redirect('/')

    return render(request, 'update.html', {'todos': todos})

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