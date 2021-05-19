from django.contrib import admin
from polymorphic.admin import (
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin,
    PolymorphicInlineSupportMixin,
    StackedPolymorphicInline,
)

from .models import (
    Interview,
    Question,
    TextQuestion,
    ChoiceQuestion,
    MultiChoicesQuestion,
    ChoiceVariations,
    MultiChoicesVariations,
    Answer,
    TextAnswer,
    ChoiceAnswer,
    MultiChoicesAnswer,
    AnswerOwner,
    UserAnswerOwner,
    AnonymousUserAnswerOwner,
)


class QuestionInline(StackedPolymorphicInline):
    """
    An inline for a polymorphic model.
    The actual form appearance of each row is determined by
    the child inline that corresponds with the actual model type.
    """

    class TextQuestionInline(StackedPolymorphicInline.Child):
        model = TextQuestion

    class ChoiceQuestionInline(StackedPolymorphicInline.Child):
        model = ChoiceQuestion

    class MultiChoicesQuestionInline(StackedPolymorphicInline.Child):
        model = MultiChoicesQuestion

    model = Question
    child_inlines = (
        TextQuestionInline,
        ChoiceQuestionInline,
        MultiChoicesQuestionInline,
    )


@admin.register(Interview)
class InterviewAdmin(PolymorphicInlineSupportMixin,admin.ModelAdmin):
    inlines = (QuestionInline,)


@admin.register(ChoiceVariations)
class ChoiceVariationsAdmin(admin.ModelAdmin):
    pass


@admin.register(MultiChoicesVariations)
class ChoiceVariationsAdmin(admin.ModelAdmin):
    pass


@admin.register(TextQuestion)
class TextQuestionAdmin(PolymorphicChildModelAdmin):
    base_model = TextQuestion


@admin.register(ChoiceQuestion)
class ChoiceQuestionAdmin(PolymorphicChildModelAdmin):
    base_model = ChoiceQuestion


@admin.register(MultiChoicesQuestion)
class MultiChoicesQuestionAdmin(PolymorphicChildModelAdmin):
    base_model = MultiChoicesQuestion


@admin.register(Question)
class QuestionAdmin(PolymorphicParentModelAdmin):
    base_model = Question

    child_models = (TextQuestion, ChoiceQuestion, MultiChoicesQuestion)


@admin.register(TextAnswer)
class TextAnswerAdmin(PolymorphicChildModelAdmin):
    base_model = TextAnswer


@admin.register(ChoiceAnswer)
class ChoiceAnswerAdmin(PolymorphicChildModelAdmin):
    base_model = ChoiceAnswer


@admin.register(MultiChoicesAnswer)
class MultiChoicesAnswerAdmin(PolymorphicChildModelAdmin):
    base_model = MultiChoicesAnswer


@admin.register(Answer)
class AnswerAdmin(PolymorphicParentModelAdmin):
    base_model = Answer

    child_models = (TextAnswer, ChoiceAnswer, MultiChoicesAnswer)


@admin.register(UserAnswerOwner)
class UserAnswerOwnerAdmin(PolymorphicChildModelAdmin):
    base_model = UserAnswerOwner


@admin.register(AnonymousUserAnswerOwner)
class AnonymousUserAnswerOwnerAdmin(PolymorphicChildModelAdmin):
    base_model = AnonymousUserAnswerOwner


@admin.register(AnswerOwner)
class AnswerOwnerAdmin(PolymorphicParentModelAdmin):
    base_model = AnswerOwner

    child_models = (UserAnswerOwner, AnonymousUserAnswerOwner)
