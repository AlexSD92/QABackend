from .models import Question
from .serializers import QuestionsSerializer
from rest_framework import viewsets


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(question_author=self.request.user)

