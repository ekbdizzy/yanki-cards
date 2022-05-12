from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response

from .models import Theme
from .serializers import (
    QuestionSerializer,
    ThemeDetailSerializer,
    ThemeSerializer,
)


class ThemeListView(ListCreateAPIView):
    """Get list of public and private themes."""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ThemeSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Theme.objects.filter(is_private=False) | user.themes.all()
        return Theme.objects.filter(is_private=False)


class ThemeDetailView(RetrieveUpdateDestroyAPIView):
    """Details of, update or delete private themes."""

    # TODO add permission_class IsAuthor

    permission_classes = [IsAuthenticated]
    serializer_class = ThemeDetailSerializer

    def get_queryset(self):
        theme_id = self.kwargs.get('pk')
        queryset = Theme.objects.filter(id=theme_id)
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == request.user:
            return super().update(self, request, args, kwargs)
        return Response(
            {"error": "Only author can retrieve theme."},
            status=status.HTTP_403_FORBIDDEN,
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.author == request.user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"error": "Only author can delete theme."},
            status=status.HTTP_403_FORBIDDEN,
        )


class QuestionCreateView(CreateAPIView):
    """Create new question."""

    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer


class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    """Details of, update or delete questions."""

    pass
