import json
import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from tracticeapi.models import Show


class PracticeSessionTests(APITestCase):
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

    def test_create_practice_session(self):
        show = Show.objects.create(
            description="Acoustic Night",
            performance_date="2024-02-10T19:00:00Z",
            user_id=1,  # Use a valid user ID from your database
        )
        url = '/practicesessions'
        data = {
            "session_date": "2013-01-11T14:00:00Z",
            "show_id": 1,
            "notes": "learn two more songs",
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response['session_date'], "2013-01-11T14:00:00Z")
        self.assertEqual(json_response['notes'], "learn two more songs")

        self.assertIn('show', json_response)
        self.assertEqual(json_response['show']['id'], 1)
        self.assertEqual(json_response['show']['description'], "Acoustic Night")
        self.assertEqual(
            json_response['show']['performance_date'], "2024-02-10T19:00:00Z"
        )

    def test_update_practice_session(self):
        self.test_create_practice_session()

        url = '/practicesessions/1'
        data = {
            "session_date": "2024-01-10T14:00:00Z",
            "show_id": 1,
            "notes": "Focused on transitions!",
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        put_response = self.client.put(url, data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_204_NO_CONTENT)

        get_response = self.client.get(url, data, format='json')
        json_response = json.loads(get_response.content)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['session_date'], "2024-01-10T14:00:00Z")
        self.assertEqual(json_response['notes'], "Focused on transitions!")
        self.assertIn('show', json_response)
        self.assertEqual(json_response['show']['id'], 1)
