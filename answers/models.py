from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from questions.models import Question


class Answer(models.Model):
    answer_summary = models.CharField(max_length=300, verbose_name='Answer Summary')
    answer_details = models.TextField(verbose_name='Answer Details')
    answer_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    answer_published = models.DateTimeField(auto_now_add=True, verbose_name='Answer Published')
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.answer_summary