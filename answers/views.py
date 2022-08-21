from .models import Answer
from questions.models import Question
from .serializers import AnswersSerializer
from questions.serializers import QuestionsSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
# from .permissions import IsAnswerAuthor
from django.shortcuts import render, get_object_or_404


class CreateAnswer(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer

    def perform_create(self, serializer):
        user = self.request.user
        # slug = self.kwargs.get('slug')
        question = get_object_or_404(Question, slug=self.kwargs.get('slug'))
        serializer.save(answer_author=user, related_question=question)


class ListAnswer(ListAPIView):
    serializer_class = AnswersSerializer

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        return Answer.objects.filter(related_question__slug=slug)

class AnswerDetails(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswersSerializer