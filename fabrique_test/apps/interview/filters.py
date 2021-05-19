import django_filters
from fabrique_test.apps.core.filters import OrderingFilter
from .models import (
    Interview,
    Question,
    Answer,
    ChoiceVariations,
    MultiChoicesVariations,
)


class ChoiceVariationsFilter(django_filters.FilterSet):
    class Meta:
        model = ChoiceVariations
        fields = {
            'question': ['exact'],
            'is_right': ['exact'],

        }


class MultiChoicesVariationsFilter(django_filters.FilterSet):
    class Meta:
        model = MultiChoicesVariations
        fields = {
            'question': ['exact'],
            'is_right': ['exact'],

        }


class AnswerFilter(django_filters.FilterSet):
    order_by = OrderingFilter(
        fields=(
            ('created_at', 'created at'),
        )
    )

    class Meta:
        model = Answer
        fields = {
            'owner': ['exact'],
            'created_at': ['date']
        }


class QuestionFilter(django_filters.FilterSet):
    order_by = OrderingFilter(
        fields=(
            ('created_at', 'created at'),
        )
    )

    class Meta:
        model = Question
        fields = {
            'interview': ['exact'],
            'created_at': ['date']
        }


class InterviewFilter(django_filters.FilterSet):
    order_by = OrderingFilter(
        fields=(
            ('created_at', 'created at'),
        )
    )

    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Interview
        fields = {
            'title': [],
            'created_at': ['date']
        }
