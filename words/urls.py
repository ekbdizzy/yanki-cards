from django.urls import path

from .views import get_translation_view


urlpatterns = [
    path('words/translate/', get_translation_view),
]
