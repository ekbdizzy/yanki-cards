from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Feedback
from .serializer import FeedbackSerializer


class FeedbackCreateView(CreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
    queryset = Feedback.objects.all()

    def post(self, request, *args, **kwargs):
        user = request.user
        return self.create(request, user=user, *args, **kwargs)
