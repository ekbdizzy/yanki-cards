from rest_framework import permissions
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from .models import Theme
from .serializers import (
    QuestionSerializer,
    ThemeDetailSerializer,
    ThemeSerializer,
)


class IsAuthor(permissions.BasePermission):
    """Permission check for authority of theme."""

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


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

    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = ThemeDetailSerializer
    queryset = Theme.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class QuestionCreateView(CreateAPIView):
    """Create new question."""

    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer


class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    """Details of, update or delete questions."""

    pass
