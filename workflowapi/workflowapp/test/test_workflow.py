import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import workflow, workflow, step
from ..serializers import commentSerializer, workflowSerializer, stepSerializer
from django.conf.urls import url, include
from rest_framework.test import APITestCase, APIClient

# initialize the APIClient app

client = APIClient()
client.login(username='admin', password='admin')

class GETNewworkflowTest(APITestCase):
    """Test module for get a new workflow"""

    def setUp(self):
        self.valid_payload = {
            "name": "How to nail something",
            "description": "Basic instructions to nail something",
            "steps": [
              {
                 "name": "Place nail",
                 "description": "Hold nail on top the thing to be nailed"
              },
              {
                "name": "Hit nail",
                "description": "Hit the nail repeatedly with a hammer"
              }
            ]
        }


    def test_create_valid_workflow(self):
        response = self.client.post('/workflow/1',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        response_get = self.client.get('/workflow/1')
        self.assertEqual(response_get.status_code, status.HTTP_200_OK)

class CreateNewworkflowTest(APITestCase):
    """Test module for insertig a new workflow"""

    def setUp(self):
        self.valid_payload = {
            "name": "How to nail something",
            "description": "Basic instructions to nail something",
            "steps": [
              {
                 "name": "Place nail",
                 "description": "Hold nail on top the thing to be nailed"
              },
              {
                "name": "Hit nail",
                "description": "Hit the nail repeatedly with a hammer"
              }
            ]
        }


    def test_create_valid_workflow(self):
        response = self.client.post('/workflow/1',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CreateNewworkflowTest(APITestCase):
    """Test module for updating a new workflow"""

    def setUp(self):
        self.valid_payload = {
            "name": "How to nail something",
            "description": "Basic instructions to nail something",
            "steps": [
              {
                 "name": "Place nail",
                 "description": "Hold nail on top the thing to be nailed"
              },
              {
                "name": "Hit nail",
                "description": "Hit the nail repeatedly with a hammer"
              }
            ]
        }


    def test_update_valid_workflow(self):
        response = self.client.post('/workflow/1',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

        self.updated_valid_payload = {
            "name": "How to nail something",
            "description": "Bzxcasic instructions to nail something",
            "steps": [
              {
                 "name": "Place nail",
                 "description": "updated Hold nail on top the thing to be nailed"
              }
            ]
        }

        response_update = self.client.put('/workflow/1',
            data=json.dumps(self.updated_valid_payload),
            content_type='application/json')
        self.assertEqual(response_update.status_code, status.HTTP_200_OK)

class DeleteSingleworkflowTest(APITestCase):
    """Test module for deleting an existing workflow record"""
    def setUp(self):
        self.valid_payload = {
            "name": "How to nail something",
            "description": "Basic instructions to nail something",
            "steps": [
              {
                 "name": "Place nail",
                 "description": "Hold nail on top the thing to be nailed"
              }
            ]
        }

    def test_create_valid_workflow(self):
        response = self.client.post('/workflow/1',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )

    def test_valid_delete_workflow(self):
        response_delete = self.client.delete('/workflow/1')
        self.assertEqual(response_delete.status_code, status.HTTP_404_NOT_FOUND)
