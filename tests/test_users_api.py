from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.users_url = reverse("user-list")
        self.user_detail_url = reverse("user-detail", kwargs={"pk": self.user.pk})

    def test_get_users(self):
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {"username": "newuser", "password": "newpassword"}
        response = self.client.post(self.users_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_user(self):
        data = {"username": "updateduser", "password": "updatedpassword"}
        response = self.client.put(self.user_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user(self):
        response = self.client.delete(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
