import json
from rest_framework import status
from rest_framework.test import APITestCase
from tracticeapi.models import Artist


class ArtistTests(APITestCase):
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

    def test_create_artist(self):
        url = '/artists'
        data = {"name": "Nate Smith"}

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response['name'], "Nate Smith")

    def test_update_artist(self):
        self.test_create_artist()
        url = '/artists/1'
        data = {"name": "Jojo Mayer"}

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        put_response = self.client.put(url, data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_204_NO_CONTENT)

        get_response = self.client.get(url, format='json')
        json_response = json.loads(get_response.content)
        self.assertEqual(json_response['name'], "Jojo Mayer")
