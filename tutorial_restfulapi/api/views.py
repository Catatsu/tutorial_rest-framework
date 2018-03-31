from rest_framework import viewsets, mixins
from .serializer import *
from polls.models import Question, Choice


class QuestionViewSet(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    """
    Questionのデータを返すよ
    """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class ChoiceViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """
    Choiceのデータを返すよ
    """
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()

    def get_queryset(self):
        pk = self.kwargs.get('questions_pk')
        return self.queryset.filter(question=pk)
