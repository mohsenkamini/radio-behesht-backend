from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import RadioUser
from django.contrib.auth import get_user_model

class UsersAPITest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123"
            email="test@example.com"
        )
        self.url = reverse('users')

    def test_get_user_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.aserEqual(response.data['username'], "testuser")

    def test_get_user_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



