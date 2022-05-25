from contextlib import suppress

from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()  # noqa N806


class UserManagerTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email='user@mail.com',
            password='awesome_password',
        )
        self.superuser = User.objects.create_superuser(
            email='superuser@mail.com',
            password='super_password',
        )

    def test_create_user(self):
        self.assertEqual(self.user.email, 'user@mail.com')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)
        self.assertFalse(self.user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(TypeError):
            User.objects.create_user(email='')

        with self.assertRaises(TypeError):
            User.objects.create_user(email='abc')

        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='awesome_password')

    def test_create_superuser(self):

        self.assertEqual(self.superuser.email, 'superuser@mail.com')
        self.assertTrue(self.superuser.is_active)
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)

        with self.assertRaises(ValueError):
            self.superuser = User.objects.create_superuser(
                email='superuser@mail.com',
                password='super_password',
                is_superuser=False,
            )

        with self.assertRaises(ValueError):
            self.superuser = User.objects.create_superuser(
                email='superuser@mail.com',
                password='super_password',
                is_staff=False,
            )
