from rest_framework import serializers
from .models import Question


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        slug = serializers.SlugField(read_only=True)
        model = Question
        fields = '__all__'