from rest_framework import serializers
from .models import Answer


class AnswersSerializer(serializers.ModelSerializer):
    answer_author = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Answer
        exclude = ['related_question']