from django.urls import path

from .views import (
    TranslationsStackDeleteView,
    TranslationsStackView,
    create_new_translation_view,
    get_anki_cards_view,
    get_translation_view,
)


urlpatterns = [
    path('words/translate/', get_translation_view, name='word-translate'),
    path(
        'words/create/',
        create_new_translation_view,
        name='create-translation',
    ),
    path(
        'words/translations/',
        TranslationsStackView.as_view(),
        name='translations-list',
    ),
    path(
        'words/translations/<int:pk>',
        TranslationsStackDeleteView.as_view(),
        name='delete-translation',
    ),
    path('words/cards/', get_anki_cards_view, name='get-anki-cards'),
]
