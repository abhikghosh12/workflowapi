# serializers.py
from rest_framework import serializers

from .models import workflow, comment

class workflowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = workflow
        fields = ['name', 'description', 'steps']

class commentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = comment
        fields = ['name', 'text']
