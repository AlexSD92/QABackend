from rest_framework import serializers
from .models import Question


class QuestionsSerializer(serializers.ModelSerializer):
    # question_author = serializers.StringRelatedField()
    slug = serializers.SlugField(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'