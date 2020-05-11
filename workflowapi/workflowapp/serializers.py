# serializers.py
from rest_framework import serializers

from .models import workflow, comment, step


class stepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = step
        fields = ['name', 'description']

class workflowSerializer(serializers.HyperlinkedModelSerializer):
    steps = stepSerializer( many=True, read_only=True)
    class Meta:
        model = workflow
        fields = ['name', 'description', 'steps' ]

class commentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = comment
        fields = ['name', 'text']
