import json

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User

from ..models import Question, Theme
from ..serializers import QuestionSerializer


class QuestionTestCase(APITestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(email='user1@mail.com')
        self.user2 = User.objects.create(email='user2@mail.com')
        self.theme_private_1 = Theme.objects.create(
            title='Private theme by user 1',
            author=self.user1,
        )
        self.theme_private_2 = Theme.objects.create(
            title='Private theme by user 2',
            author=self.user2,
        )

        self.question_1_theme_1 = Question.objects.create(
            theme=self.theme_private_1,
            text='Question 1 Theme 1',
        )

        self.question_2_theme_1 = Question.objects.create(
            theme=self.theme_private_1,
            text='Question 2 Theme 1',
        )

        self.question_1_theme_2 = Question.objects.create(
            theme=self.theme_private_2,
            text='Question 1 Theme 1',
        )

        self.question_2_theme_2 = Question.objects.create(
            theme=self.theme_private_2,
            text='Question 2 Theme 2',
        )

        self.url_create = reverse('question-create')
        self.url_detail = reverse(
            'question-detail',
            kwargs={'pk': self.question_1_theme_1.id},
        )

    def test_get(self):

        # Unauthorized
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authorized
        self.client.force_authenticate(self.user1)
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serialized_data = QuestionSerializer(self.question_1_theme_1).data
        self.assertEqual(response.data, serialized_data)

    def test_create(self):
        self.assertEqual(Question.objects.all().count(), 4)
        question_data = {
            "text": "Created question",
            "theme_id": self.theme_private_1.id,
        }
        data = json.dumps(question_data)

        # Unauthorized
        response = self.client.post(
            self.url_create,
            data=data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Question.objects.all().count(), 4)

        # Authorized, not Author
        self.client.force_authenticate(self.user2)
        response = self.client.post(
            self.url_create,
            data=data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Question.objects.all().count(), 4)

        # Authorized, Author
        self.client.force_authenticate(self.user1)
        response = self.client.post(
            self.url_create,
            data=data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.all().count(), 5)
        self.assertTrue(
            Question.objects.filter(
                text=question_data['text'],
                theme_id=question_data['theme_id'],
            ).first(),
        )

    def test_update(self):
        update_data = {"text": "Updated question"}

        # Unauthorized
        response = self.client.patch(
            self.url_detail,
            data=update_data,
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Authorized, not author
        self.client.force_authenticate(self.user2)
        response = self.client.patch(
            self.url_detail,
            data=update_data,
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Authorized, author
        self.client.force_authenticate(self.user1)
        response = self.client.patch(
            self.url_detail,
            data=update_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        question = Question.objects.get(id=self.question_1_theme_1.id)
        self.assertEqual(question.text, update_data['text'])

    def test_delete(self):
        self.assertEqual(Question.objects.all().count(), 4)
        self.client.force_authenticate(self.user1)
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Question.objects.all().count(), 3)
