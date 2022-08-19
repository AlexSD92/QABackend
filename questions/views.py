from .models import Question
from .serializers import QuestionsSerializer
from rest_framework import viewsets
from .permissions import IsQuestionAuthor


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer
    lookup_field = 'slug'

    permission_classes = [IsQuestionAuthor]

    def perform_create(self, serializer):
        serializer.save(question_author=self.request.user)

