
# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import TodoSerializer  
from rest_framework.permissions import IsAuthenticated    # add this
from .models import Todo                     # add this
        
class TodoView(viewsets.ModelViewSet):
  permission_classes = [IsAuthenticated]       # add this
  serializer_class = TodoSerializer          # add this
  def get_queryset(self):
        qs = super().get_queryset()

        # Get only contact about current authenticated user
        qs = qs.filter(user=self.request.user)
           # add this