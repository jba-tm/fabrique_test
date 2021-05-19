from rest_framework import routers

from fabrique_test.apps.interview.api.views import (
    InterviewViewSet,
    QuestionViewSet,
    ChoiceVariationsViewSet,
    MultiChoicesVariationsViewSet,
    AnswerViewSet,
    AnswerOwnerUnionSerializer,
)

router = routers.DefaultRouter()

router.register('interview', InterviewViewSet, 'interview')
router.register('question', QuestionViewSet, 'question')
router.register('choice_variation', ChoiceVariationsViewSet, 'choice_variations')
router.register('multi_choices_variation', MultiChoicesVariationsViewSet, 'multi_choices_variation')
router.register('answer', AnswerViewSet, 'answer')
router.register('answer_owner', AnswerViewSet, 'answer_owner')
