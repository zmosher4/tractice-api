import json
from rest_framework import status
from rest_framework.test import APITestCase
from tracticeapi.models import Artist


class SongTests(APITestCase):
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
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.token = json_response["token"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)

    def test_create_song(self):
        url = '/songs'
        data = {
            "title": "Strings",
            "description": "Very vocal, very drums.",
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response['title'], "Strings")
        self.assertEqual(json_response['description'], "Very vocal, very drums.")

    def test_update_song(self):
        self.test_create_song()

        url = '/songs/1'
        data = {
            "title": "Stringy",
            "description": "Very vocal, very drums!",
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        put_response = self.client.put(url, data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_204_NO_CONTENT)

        get_response = self.client.get(url, format='json')
        json_response = json.loads(get_response.content)
        self.assertEqual(json_response['title'], "Stringy")
        self.assertEqual(json_response['description'], "Very vocal, very drums!")
