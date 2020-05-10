from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import workflowSerializer, commentSerializer
from .models import workflow, comment

# Create your views here.

class workflowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = workflow.objects.all()
    serializer_class = workflowSerializer
    permission_classes = [permissions.IsAuthenticated]

class commentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = comment.objects.all()
    serializer_class = commentSerializer
    permission_classes = [permissions.IsAuthenticated]
