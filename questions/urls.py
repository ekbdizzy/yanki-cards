from django.urls import path

from .views import (
    QuestionCreateView,
    QuestionDetailView,
    ThemeDetailView,
    ThemeListView,
)

urlpatterns = [
    path('themes/', ThemeListView.as_view()),
    path('themes/<int:pk>/', ThemeDetailView.as_view()),
    path('questions/', QuestionCreateView.as_view()),
    path('questions/<int:pk>/', QuestionDetailView.as_view()),
]
