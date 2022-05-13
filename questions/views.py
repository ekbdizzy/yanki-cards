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

from .models import Hint, Question, Theme
from .permissions import IsAuthor, IsPublicTheme
from .serializers import (
    HintSerializer,
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

    permission_classes = [IsAuthenticated, IsAuthor | IsPublicTheme]
    serializer_class = ThemeDetailSerializer
    queryset = Theme.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class QuestionCreateView(CreateAPIView):
    """Create new question."""

    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = QuestionSerializer

    def post(self, request, *args, **kwargs):
        theme = get_object_or_404(Theme, pk=self.request.data.get('theme_id'))
        self.check_object_permissions(self.request, theme)
        return self.create(request, *args, **kwargs)


class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    """Details of, update or delete questions."""

    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj


class HintCreateView(CreateAPIView):
    """Create new hints."""

    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = HintSerializer

    def post(self, request, *args, **kwargs):
        question = get_object_or_404(
            Theme,
            pk=self.request.data.get('question_id'),
        )
        self.check_object_permissions(self.request, question)
        return self.create(request, *args, **kwargs)


class HintDetailView(RetrieveUpdateDestroyAPIView):
    """Details of, update or delete hints."""

    permission_classes = [IsAuthenticated, IsAuthor]
    serializer_class = HintSerializer
    queryset = Hint.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
