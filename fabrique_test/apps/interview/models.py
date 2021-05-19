import uuid

from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.auth import get_user_model
from django.core import exceptions as dj_exceptions

UserModel = get_user_model()


class InterviewStatusChoices(models.TextChoices):
    ACTIVE = 'ACTIVE', 'active'
    INACTIVE = 'INACTIVE', 'inactive'


class Interview(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    status = models.CharField(choices=InterviewStatusChoices.choices, default=InterviewStatusChoices.ACTIVE,
                              max_length=8)
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    edited_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']


class Question(PolymorphicModel):
    interview = models.ForeignKey('Interview', on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    edited_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']


class TextQuestion(Question):
    pass


class ChoiceQuestion(Question):
    pass


class MultiChoicesQuestion(Question):
    pass


class ChoiceVariations(models.Model):
    question = models.ForeignKey(ChoiceQuestion, on_delete=models.CASCADE, related_name='variations')
    body = models.CharField(max_length=255)
    is_right = models.BooleanField()

    def full_clean(self, *args, **kwargs):
        super(ChoiceVariations, self).full_clean(*args, **kwargs)
        if self.is_right and self.question.variations.filter(is_right=True).exists():
            raise dj_exceptions.ValidationError({'is_right': 'Question already has right answer'})

    class Meta:
        ordering = ['-pk']


class MultiChoicesVariations(models.Model):
    question = models.ForeignKey(MultiChoicesQuestion, on_delete=models.CASCADE, related_name='variations')
    body = models.CharField(max_length=255)
    is_right = models.BooleanField()


    class Meta:
        ordering = ['-pk']


class Answer(PolymorphicModel):
    owner = models.ForeignKey('AnswerOwner', on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    edited_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']


class TextAnswer(Answer):
    question = models.ForeignKey('TextQuestion', on_delete=models.CASCADE, related_name='answers')
    answer = models.TextField(max_length=1000)


class ChoiceAnswer(Answer):
    question = models.ForeignKey('ChoiceQuestion', on_delete=models.CASCADE, related_name='answers')
    answer = models.ForeignKey('ChoiceVariations', on_delete=models.CASCADE)


class MultiChoicesAnswer(Answer):
    question = models.ForeignKey('MultiChoicesQuestion', on_delete=models.CASCADE, related_name='answers')
    answer = models.ManyToManyField('ChoiceVariations')


class AnswerOwner(PolymorphicModel):
    pass

    class Meta:
        ordering = ['-pk']


class UserAnswerOwner(AnswerOwner):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='answers')


class AnonymousUserAnswerOwner(AnswerOwner):
    anonymous_user = models.UUIDField(default=uuid.uuid4, unique=True)
