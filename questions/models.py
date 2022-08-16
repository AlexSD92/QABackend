from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_summary = models.CharField(max_length=300, verbose_name='Question Summary')
    question_details = models.TextField(verbose_name='Question Details')
    question_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    question_published = models.DateTimeField(auto_now_add=True, verbose_name='Question Published')
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.question_summary