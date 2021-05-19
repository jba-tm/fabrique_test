from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)

from .routers import router
from fabrique_test.apps.interview.api import views as interview_views

app_name = 'api'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('', include(router.urls)),
    path('question_type/', interview_views.QuestionResourceTypeAPIView.as_view(), name='question_type-list'),
    path('answer_type/', interview_views.AnswerResourceTypeAPIView.as_view(), name='answer_type-list'),
    path('answer_owner_type/', interview_views.AnswerOwnerResourceTypeAPIView.as_view(), name='answer_owner_type-list')
]
