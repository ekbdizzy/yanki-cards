from django.urls import path

from .views import create_new_translation_view, get_translation_view


urlpatterns = [
    path('words/translate/', get_translation_view),
    path('words/', create_new_translation_view),
]
