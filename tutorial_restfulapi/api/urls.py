from django.conf.urls import url, include
from rest_framework_nested import routers
from .views import QuestionViewSet, ChoiceViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'questions', QuestionViewSet)

# nested router
questions_router = routers.NestedSimpleRouter(router, r'questions', lookup='questions')
# ex /questions/1/choices/1
questions_router.register(r'choices', ChoiceViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(questions_router.urls)),
]
