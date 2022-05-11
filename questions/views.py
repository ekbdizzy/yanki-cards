from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Theme
from .serializers import ThemeSerializer


class ThemeListView(ListCreateAPIView):
    """Get list of public themes."""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ThemeSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Theme.objects.filter(is_private=False) | user.themes.all()
        return Theme.objects.filter(is_private=False)
