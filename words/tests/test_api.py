import csv
import io
import json
from unittest import mock

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from users.models import User

from ..models import Phrase, TranslationsStack
from ..serializers import TranslationsStackSerializer
from ..views import get_translation_view


class WordAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = User.objects.create(email='user1@mail.com')

        self.apple_tr = Phrase.objects.create(language='tr', phrase='elma')
        self.pear_en = Phrase.objects.create(language='en', phrase='pear')
        self.pear_ru = Phrase.objects.create(language='ru', phrase='груша')
        self.pear_tr = Phrase.objects.create(language='tr', phrase='armut')
        self.hello_en = Phrase.objects.create(language='en', phrase='hello')
        self.hello_tr = Phrase.objects.create(language='tr', phrase='merhaba')

        self.translations_stack_single = TranslationsStack.objects.create(
            user=self.user,
        )
        self.translations_stack_single.phrases.set([self.pear_tr, self.pear_ru])

        self.translations_stack_1 = TranslationsStack.objects.create(
            user=self.user,
        )
        self.translations_stack_1.phrases.set([self.hello_en])
        self.translations_stack_2 = TranslationsStack.objects.create(
            user=self.user,
        )
        self.translations_stack_2.phrases.set([self.hello_tr, self.hello_en])

    @mock.patch('words.views.get_yandex_token', return_value='token')
    @mock.patch('words.views.translate_phrase')
    def test_get_translation_view(self, translate_phrase, get_token):

        url = reverse('word-translate')
        phrase = {"phrase": "яблоко", "language": "en"}
        expected_response = [{"text": "apple", "detectedLanguageCode": "ru"}]
        translate_phrase.return_value = expected_response

        request = self.factory.post(url, data=phrase)
        response = get_translation_view(request)
        self.assertEqual(response.status_code, 200)

    def test_create_new_translation_view(self):
        url = reverse('create-translation')
        self.client.force_authenticate(self.user)

        # stack does not exists:
        phrases_request = [
            {"phrase": "яблоко", "language": "ru"},
            {"phrase": "apple", "language": "en"},
        ]
        response = self.client.post(
            url,
            data=json.dumps(phrases_request),
            content_type='application/json',
        )
        phrases = [
            Phrase.objects.filter(phrase='apple', language='en').first(),
            Phrase.objects.filter(phrase='яблоко', language='ru').first(),
        ]
        self.assertTrue(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(all(phrases))
        self.assertTrue(
            TranslationsStack.objects.filter(
                user=self.user,
                phrases__in=phrases,
            ),
        )

        # there is only one stack:
        phrases_request = [
            {"phrase": "груша", "language": "ru"},
            {"phrase": "pear", "language": "en"},
        ]
        self.assertTrue(TranslationsStack.objects.all().count(), 3)
        response = self.client.post(
            url,
            data=json.dumps(phrases_request),
            content_type='application/json',
        )
        phrases = [self.pear_en, self.pear_ru, self.pear_tr]
        translations_stack = TranslationsStack.objects.filter(
            user=self.user,
            phrases__in=phrases,
        ).first()
        self.assertTrue(TranslationsStack.objects.all().count(), 3)
        self.assertTrue(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(translations_stack)
        self.assertEqual(translations_stack.phrases.count(), 3)

        # there are more than one stack:
        phrases_request = [
            {"phrase": "привет", "language": "ru"},
            {"phrase": "hello", "language": "en"},
        ]
        self.assertTrue(TranslationsStack.objects.all().count(), 3)
        response = self.client.post(
            url,
            data=json.dumps(phrases_request),
            content_type='application/json',
        )
        self.assertTrue(TranslationsStack.objects.all().count(), 2)
        self.assertTrue(response.status_code, status.HTTP_201_CREATED)

        phrases = [self.hello_en, self.hello_tr]
        translations_stack = TranslationsStack.objects.filter(
            user=self.user,
            phrases__in=phrases,
        ).first()
        self.assertTrue(translations_stack)
        self.assertTrue(
            Phrase.objects.filter(phrase="привет", language="ru").first(),
        )
        self.assertEqual(translations_stack.phrases.count(), 3)

    def test_get_translations_stacks_list(self):
        url = reverse('translations-list')
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        translations_stacks = TranslationsStack.objects.filter(user=self.user)
        serialized_data = TranslationsStackSerializer(
            translations_stacks,
            many=True,
        ).data
        self.assertEqual(serialized_data, response.data)

    def test_delete_translation_stack(self):
        self.assertEqual(TranslationsStack.objects.all().count(), 3)
        url = reverse(
            'delete-translation',
            kwargs={'pk': self.translations_stack_2.id},
        )
        self.client.force_authenticate(self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TranslationsStack.objects.all().count(), 2)

    def test_get_anki_cards(self):
        url = reverse('get-anki-cards')
        self.client.force_authenticate(self.user)

        # request without param lang
        response = self.client.get(
            url,
            content_type='text/csv',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response_error = {
            "error": "Should have param 'lang' with languages: (?lang=ru,en)",
        }
        self.assertEqual(response.data, response_error)

        response = self.client.get(
            url,
            data={'lang': 'tr,en'},
            content_type='text/csv',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        content = response.content.decode('utf-8')
        csv_reader = csv.reader(io.StringIO(content))
        body = list(csv_reader)
        self.assertEqual(body[1], ['merhaba\thello'])
