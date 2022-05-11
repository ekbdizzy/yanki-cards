from django.urls import path

from .views import ThemeListView


urlpatterns = [
    path('themes/', ThemeListView.as_view()),
]
