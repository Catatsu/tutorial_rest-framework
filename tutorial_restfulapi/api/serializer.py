from rest_framework import serializers
from polls.models import Question, Choice
from django.db.models import F


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')
        read_only_fields = ('question', 'choice_text', )

    def update(self, instance, validated_data):
        instance.votes += 1
        instance.save()

        return instance


class QuestionSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choice', )

