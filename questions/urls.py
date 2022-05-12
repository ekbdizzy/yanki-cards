from django.urls import path

from .views import ThemeDetailView, ThemeListView


urlpatterns = [
    path('themes/', ThemeListView.as_view()),
    path('themes/<int:pk>/', ThemeDetailView.as_view()),
]
