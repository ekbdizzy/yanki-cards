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

        self.url_list_create = reverse('theme-list-create')
        self.url_detail = reverse(
            'theme-detail',
            kwargs={'pk': self.theme_private_1.id},
        )

    def test_get(self):

        # Unauthenticated
        public_themes = [self.theme_public_1, self.theme_public_2]
        serializer_data = ThemeSerializer(public_themes, many=True).data

        response = self.client.get(self.url_list_create)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

        # Authenticated
        self.client.force_authenticate(self.user1)
        themes = [
            self.theme_public_1,
            self.theme_public_2,
            self.theme_private_1,
        ]
        serializer_data = ThemeSerializer(themes, many=True).data
        response = self.client.get(self.url_list_create)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(Theme.objects.all().count(), 4)
        theme_data = {"title": 'Created Theme'}
        data = json.dumps(theme_data)

        # Unauthenticated
        response = self.client.post(
            self.url_list_create,
            data=data,
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Theme.objects.all().count(), 4)

        # Authenticated
        self.client.force_authenticate(self.user1)
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

    def test_update(self):
        update_data = {"title": 'Updated Theme'}

        # Unauthenticated
        response = self.client.patch(self.url_detail, data=update_data)
        theme = Theme.objects.get(id=self.theme_private_1.id)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(theme.title, self.theme_private_1.title)

        # Authenticated
        self.client.force_authenticate(self.user1)
        response = self.client.patch(self.url_detail, data=update_data)
        theme = Theme.objects.get(id=self.theme_private_1.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(theme.title, update_data['title'])

    def test_delete(self):
        self.assertEqual(Theme.objects.all().count(), 4)

        # Unauthenticated
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Theme.objects.all().count(), 4)

        # Authenticated
        self.client.force_authenticate(self.user1)
        response = self.client.delete(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Theme.objects.all().count(), 3)
