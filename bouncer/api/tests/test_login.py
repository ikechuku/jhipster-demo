from rest_framework import status
from .mock_data import registration_data,auth_data
from rest_framework.test import APITestCase
from django.urls import reverse
from django.urls import reverse

from ..models.user import User
import bcrypt


class TestLogin(APITestCase):
    def setUp(self):
        data = registration_data.customer_registration_data()
        hashed = bcrypt.hashpw(
            data['password'].encode('utf-8'), bcrypt.gensalt())
        token = 'sometoken'
        user = User.objects.create(
            user_name=data['user_name'],
            password=hashed,
            email_verification_token=token,
            user_type='customer',
        )
        user.save()

    def test_login(self):
        url = reverse('login')
        response = self.client.post(url, auth_data.auth_data())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Login was successful")
