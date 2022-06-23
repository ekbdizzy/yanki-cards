import json

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User

from ..models import Feedback


class FeedbackTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email='user1@mail.com')
        self.feedback = Feedback.objects.create(
            theme="I have a problem",
            title="Title of feedback",
            text="Some text",
        )

    def test_create(self):
        url = reverse('feedback-create')
        feedback = {
            "theme": "problem",
            "title": "Title of feedback",
            "text": "Some description of problem",
        }
        data = json.dumps(feedback)
        self.client.force_authenticate(self.user)

        self.assertEqual(Feedback.objects.all().count(), 1)
        response = self.client.post(
            url,
            data=data,
            content_type='application/json',
        )
        self.assertTrue(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.all().count(), 2)
        self.assertTrue(
            Feedback.objects.filter(title=feedback['title']).first(),
        )

        # Test theme is not in CHOICES
        feedback = {
            "theme": "Theme is not in CHOICES",
            "title": "Title of feedback",
            "text": "Some description of problem",
        }
        data = json.dumps(feedback)
        self.client.force_authenticate(self.user)
        response = self.client.post(
            url,
            data=data,
            content_type='application/json',
        )
        self.assertTrue(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Feedback.objects.all().count(), 2)
