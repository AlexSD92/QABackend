from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet
from answers.views import CreateAnswer, ListAnswer, AnswerDetails

router = DefaultRouter()
router.register('questions', QuestionViewSet, basename='questions')


urlpatterns = [
    path('', include(router.urls)),
    path('questions/<slug:slug>/createanswer/', CreateAnswer.as_view()),
    path('questions/<slug:slug>/listanswer/', ListAnswer.as_view()),
    path('questions/<slug:slug>/listanswer/<int:pk>', AnswerDetails.as_view()),
    
    path('accounts/', include('allauth.urls')),
    

]