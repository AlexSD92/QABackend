from .models import Question
from .serializers import QuestionsSerializer
from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsQuestionAuthor


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionsSerializer
    lookup_field = 'slug'
    permission_classes = [IsQuestionAuthor]
    # authentication_classes = [TokenAuthentication, SessionAuthentication]


    def perform_create(self, serializer):
        serializer.save(question_author=self.request.user)

