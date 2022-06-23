import json

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User

from ..models import Hint, Question, Theme
from ..serializers import HintSerializer


class HintTestCase(APITestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(email='user1@mail.com')
        self.user2 = User.objects.create(email='user2@mail.com')
        self.theme = Theme.objects.create(
            title='Private theme by user 1',
            author=self.user1,
        )
        self.question = Question.objects.create(
            theme=self.theme,
            text='Question 1 Theme 1',
        )
        self.hint_1 = Hint.objects.create(
            text='Hint 1',
            question=self.question,
        )
        self.hint_2 = Hint.objects.create(
            text='Hint 2',
            question=self.question,
        )
        self.url_create = reverse('hint-create')
        self.url_detail = reverse(
            'hint-detail',
            kwargs={'pk': self.hint_1.id},
        )

    def test_get(self):

        # Unauthorized
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authorized
        self.client.force_authenticate(self.user1)
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = HintSerializer(self.hint_1).data
        self.assertEqual(serialized_data, response.data)

    def test_create(self):
        self.assertEqual(Hint.objects.all().count(), 2)
        hint_data = {
            'text': 'Created hint',
            'question_id': self.question.id,
        }
        data = json.dumps(hint_data)

        # Unauthorized
        response = self.client.post(
            self.url_create,
            data=data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Hint.objects.all().count(), 2)

        # Authorized not author
        self.client.force_authenticate(self.user2)
        response = self.client.post(
            self.url_create,
            data=data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Hint.objects.all().count(), 2)

        # Authorized author
        self.client.force_authenticate(self.user1)
        response = self.client.post(
            self.url_create,
            data=data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hint.objects.all().count(), 3)
        self.assertTrue(Hint.objects.filter(text=hint_data['text']).first())

    def test_update(self):
        hint_data = {"text": "Updated text"}
        data = json.dumps(hint_data)
        self.client.force_authenticate(self.user1)
        response = self.client.patch(
            self.url_detail,
            data=data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.hint_1.refresh_from_db()
        self.assertEqual(self.hint_1.text, hint_data['text'])

    def test_delete(self):
        self.assertEqual(Hint.objects.all().count(), 2)
        self.client.force_authenticate(self.user1)
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Hint.objects.all().count(), 1)
