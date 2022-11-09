from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from Main.models import User, ScoreLog

class SimpleBackendTest(APITestCase):
    url = reverse('score-get')
    
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('username', 'Pas$w0rd')

    def test_get_score_zero(self):
        # test 0 score
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url, {"score" : 0})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Result"], 1)
        # self.assertEqual(ScoreLog.objects.get().test_col, None)

        self.assertEqual(ScoreLog.objects.get().score_2, '2.0')

    def test_get_score_positive_first(self):
        # test first positive score
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url, {"score" : 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Result"], 2)

    def test_get_score_positive_random(self):
        # test random positive score
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url, {"score" : 15})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Result"], 16)

    def test_get_score_negative_first(self):
        # test first negative score
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url, {"score" : -1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Result"], 0)

    def test_get_score_negative_random(self):
        # test random negative score
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url, {"score" : -5})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["Result"], -4)

    def test_get_score_not_numeric_input(self):
        self.client.force_authenticate(self.user)

        # test non numeric
        response = self.client.get(self.url, {"score" : "asdsad"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # empty string
        response = self.client.get(self.url, {"score" : ""})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # no query params
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)