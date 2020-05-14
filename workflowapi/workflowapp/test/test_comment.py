# Unit test for comments
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import workflow, comment, step
from ..serializers import workflowSerializer, commentSerializer, stepSerializer
from django.conf.urls import url, include
from rest_framework.test import APITestCase, APIClient

# initialize the APIClient app

client = APIClient()
client.login(username='admin', password='admin')

class Comment(APITestCase):
    """ Test module for Comment model """

    def setUp(self):
        self.project = comment.objects.create(
            name='comment 1', text ='take it easy')
        self.project2 = comment.objects.create(
            name='comment 2', text ='take care')

    def test_comment(self):
        comment_project = comment.objects.get(name='comment 1')
        comment_project_2 = comment.objects.get(name='comment 2')
        self.assertEqual(
            comment_project.get_comment(), "take it easy belongs to comment 1.")
        self.assertEqual(
            comment_project_2.get_comment(), "take care belongs to comment 2.")

    def test_get_all_comments(self):
        # get API response
        response = self.client.get('/comment/')
        # get data from db
        comments = comment.objects.all()
        serializer = commentSerializer(comments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_comment(self):
        response = self.client.get('/comment/1')
        comment1 = comment.objects.get(name='comment 1')
        serializer = commentSerializer(comment1)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_comment(self):
        response = self.client.get('/comment/30')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewcommentTest(APITestCase):
    """ Test module for inserting a new comment"""

    def setUp(self):
        self.valid_payload = {
            'name': 'Project',
            'text': 'projectxxxx',
        }

    def test_create_valid_comment(self):
        response = self.client.post('/comment/3',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UpdateSinglecommentTest(APITestCase):
    """ Test module for updating an existing comment record """

    def setUp(self):
        self.project = comment.objects.create(
            name='Project', text='projectxxxx')

        self.valid_payload = {
            'name': 'Projedfct',
            'text': 'projectdfg3xxxx',
            }

    def test_valid_update_comment(self):
        response = self.client.put('/comment/1',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class DeleteSinglecommentTest(APITestCase):
    """Test module for deleting an existing comment record"""

    def setUp(self):
        self.project = comment.objects.create(
            name='Project', text='projectxxxx')

    def test_valid_delete_comment(self):
        response = self.client.delete('/comment/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_puppy(self):
        response = self.client.delete('/comment/30')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
