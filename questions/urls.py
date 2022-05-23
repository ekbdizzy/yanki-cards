from django.urls import path

from .views import (
    HintCreateView,
    HintDetailView,
    QuestionCreateView,
    QuestionDetailView,
    ThemeDetailView,
    ThemeListCreateView,
)

urlpatterns = [
    path('themes/', ThemeListCreateView.as_view(), name='theme-list-create'),
    path('themes/<int:pk>/', ThemeDetailView.as_view(), name='theme-detail'),
    path(
        'questions/create/',
        QuestionCreateView.as_view(),
        name='question-create',
    ),
    path(
        'questions/<int:pk>/',
        QuestionDetailView.as_view(),
        name='question-detail',
    ),
    path('hints/', HintCreateView.as_view(), name='hint-create'),
    path('hints/<int:pk>/', HintDetailView.as_view(), name='hint-detail'),
]
