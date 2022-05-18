from django.urls import path

from .views import (
    TranslationsStackDeleteView,
    TranslationsStackView,
    create_new_translation_view,
    get_anki_cards_view,
    get_translation_view,
)


urlpatterns = [
    path('words/translate/', get_translation_view),
    path('words/', create_new_translation_view),
    path('words/translations/', TranslationsStackView.as_view()),
    path('words/translations/<int:pk>', TranslationsStackDeleteView.as_view()),
    path('words/cards/', get_anki_cards_view),
]
