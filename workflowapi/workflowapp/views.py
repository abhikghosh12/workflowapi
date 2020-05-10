from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import workflowSerializer, commentSerializer, stepSerializer
from .models import workflow, comment, step

# Create your views here.

class workflowViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = workflow.objects.all()
    serializer_class = workflowSerializer


class commentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = comment.objects.all()
    serializer_class = commentSerializer



class stepViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = step.objects.all()
    serializer_class = stepSerializer
