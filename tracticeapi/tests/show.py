import json
from rest_framework import status
from rest_framework.test import APITestCase
from tracticeapi.models import Show, Artist
from django.contrib.auth.models import User


class ShowTests(APITestCase):
    def setUp(self) -> None:
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
        }
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        # Create an artist associated with that user
        self.artist = Artist.objects.create(name="Test Artist", user=self.user)

        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.token = json_response["token"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def test_create_show(self):
        url = '/shows'
        data = {
            "description": "Jam Out!",
            "artist_id": self.artist.id,
            "performance_date": "2024-04-20T19:00:00Z",
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response['description'], "Jam Out!")
        self.assertEqual(json_response['performance_date'], "2024-04-20T19:00:00Z")

    def test_update_show(self):
        self.test_create_show()
        url = '/shows/1'
        data = {
            "description": "Jam In.",
            "artist_id": self.artist.id,
            "performance_date": "2024-04-22T19:00:00Z",
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        put_response = self.client.put(url, data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_204_NO_CONTENT)

        get_response = self.client.get(url, data, format='json')
        json_response = json.loads(get_response.content)
        self.assertEqual(json_response['description'], "Jam In.")
        self.assertEqual(json_response['performance_date'], "2024-04-22T19:00:00Z")
