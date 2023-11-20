from django.urls import path
from .views import ResponseViewSet2,FormViewSet,AnswerViewSet,QuestionViewSet

urlpatterns = [
    path('submit-response/', ResponseViewSet2.as_view(), name='submit_response'),
    path('form/',FormViewSet.as_view(),name='submit_form'),
    path('question/',QuestionViewSet.as_view()),
    path('answer/',AnswerViewSet.as_view())
]
