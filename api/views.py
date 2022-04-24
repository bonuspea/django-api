from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework import generics
from .models import Task

# Create your views here.
#GET--> ListAPIView
#POST--> CreateAPIView
#PUT--> UpdateAPIView
#DELETE--> DestroyAPIView

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

