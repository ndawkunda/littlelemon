from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.authtoken.models import Token
from restaurant.models import MenuItem,Boking
from django.urls import reverse
from rest_framework.test import APIClient, force_authenticate
from restaurant.serializers import MenuItemSerializer
from rest_framework import status, request


# Create your tests here.

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testuser')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.MenuItem1 = MenuItem.objects.create(title='Burger', price=80, inventory=10)
        self.MenuItem2 = MenuItem.objects.create(title='Pizza', price=80, inventory=10)

    def test_getall(self):
        url = reverse('MenuItem-view')
        response = self.client.get(url)
        MenuItem = MenuItem.objects.all()
        serializer = MenuItemSerializer(MenuItem, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assert_(response.status_code, status.HTTP_200_OK)