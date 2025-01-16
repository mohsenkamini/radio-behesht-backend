from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class StreamRequestAPITest(APITestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", 
            password="password123"
        )
        self.client.login(username="testuser", password="password123")

    def test_create_stream_request_valid(self):
        data = {
            'program_name': 'Test Program',
            'description': 'Test Description',
            'schedule': 'Daily',
            'start_date': '2024-01-01',
            'episodes': 10,
            'contact': 'testuser@example.com',
        }
        response = self.client.post('/api/stream/request/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_stream_request_invalid(self):
        data = {
            'program_name': 'Test Program',
            # Missing some other required fields
        }

        response = self.client.post('/api/stream/request/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

