import json

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User

from ..models import Theme
from ..serializers import ThemeSerializer


class ThemeTestCase(APITestCase):
    def setUp(self):

        self.user1 = User.objects.create(email='user1@mail.com')
        self.user2 = User.objects.create(email='user2@mail.com')

        self.theme_public_1 = Theme.objects.create(
            title='Public theme 1',
            is_private=False,
            author=self.user1,
        )
        self.theme_public_2 = Theme.objects.create(
            title='Public theme 2',
            is_private=False,
            author=self.user2,
        )

        self.theme_private_1 = Theme.objects.create(
            title='Private theme by user 1',
            author=self.user1,
        )
        self.theme_private_2 = Theme.objects.create(
            title='Private theme by user 2',
            author=self.user2,
        )

        self.url_list_create = reverse('theme-list')
        self.url_detail = reverse(
            'theme-detail',
            kwargs={'pk': self.theme_private_1.id},
        )

    def test_anonymous_get(self):

        public_themes = [self.theme_public_1, self.theme_public_2]
        serializer_data = ThemeSerializer(public_themes, many=True).data

        response = self.client.get(self.url_list_create)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_authenticated_get(self):

        themes = [
            self.theme_public_1,
            self.theme_public_2,
            self.theme_private_1,
        ]

        serializer_data = ThemeSerializer(themes, many=True).data

        self.client.force_login(self.user1)
        response = self.client.get(self.url_list_create)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):

        self.assertEqual(Theme.objects.all().count(), 4)

        self.client.force_login(self.user1)
        book_data = {"title": 'Created Theme'}
        data = json.dumps(book_data)
        response = self.client.post(
            self.url_list_create,
            data=data,
            content_type='application/json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Theme.objects.all().count(), 5)
        self.assertTrue(
            Theme.objects.filter(title='Created Theme', is_private=True),
        )
