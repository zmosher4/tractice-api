import json
from rest_framework import status
from rest_framework.test import APITestCase
from tracticeapi.models import Show, Song, Artist


class ShowSongTests(APITestCase):
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

    def test_create_show_song(self):
        artist = Artist.objects.create(name="Benny Greb", user_id=1)

        show = Show.objects.create(
            description="Acoustic Night",
            performance_date="2024-02-10T19:00:00Z",
            user_id=1,  # Use a valid user ID from your database
        )
        song1 = Song.objects.create(title="Go", artist_id=1, description="Dreamy.")
        song2 = Song.objects.create(title="Op", artist_id=1, description="Sad.")

        url = '/showsongs'
        data = {"show_id": 1, "song_id": 1}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('show', json_response)
        self.assertIn('song', json_response)

    def test_update_show_song(self):
        self.test_create_show_song()

        url = '/showsongs/1'
        data = {"show_id": 1, "song_id": 2}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        put_response = self.client.put(url, data, format='json')
        self.assertEqual(put_response.status_code, status.HTTP_204_NO_CONTENT)

        get_response = self.client.get(url, format='json')
        json_response = json.loads(get_response.content)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertIn('show', json_response)
        self.assertIn('song', json_response)
        self.assertEqual(json_response['song']['id'], 2)
