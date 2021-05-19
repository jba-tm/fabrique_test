from rest_framework import serializers

from rest_polymorphic.serializers import PolymorphicSerializer
from fabrique_test.apps.interview.models import (
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


class ChoiceVariationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceVariations
        fields = '__all__'


class MultiChoicesVariationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultiChoicesVariations
        fields = '__all__'


class AnswerOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerOwner
        fields = '__all__'


class UserAnswerOwnerSerializer(AnswerOwnerSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault)

    class Meta:
        model = UserAnswerOwner
        # fields = '__all__'

        exclude = 'polymorphic_ctype',


class AnonymousUserAnswerOwnerSerializer(AnswerOwnerSerializer):
    class Meta:
        model = AnonymousUserAnswerOwner
        # fields = '__all__'
        exclude = 'polymorphic_ctype',


answer_owner_model_serializer_mapping = {
    # AnswerOwner: AnswerOwnerSerializer,
    UserAnswerOwner: UserAnswerOwnerSerializer,
    AnonymousUserAnswerOwner: AnonymousUserAnswerOwnerSerializer
}


class AnswerOwnerUnionSerializer(PolymorphicSerializer):
    model_serializer_mapping = answer_owner_model_serializer_mapping


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class TextQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextQuestion
        exclude = 'polymorphic_ctype',


class ChoiceQuestionSerializer(serializers.ModelSerializer):
    variations = ChoiceVariationsSerializer(many=True, read_only=True)

    class Meta:
        model = ChoiceQuestion
        exclude = 'polymorphic_ctype',


class MultiChoicesQuestionSerializer(serializers.ModelSerializer):
    variations = MultiChoicesVariationsSerializer(many=True, read_only=True)

    class Meta:
        model = MultiChoicesQuestion
        exclude = 'polymorphic_ctype',


question_model_serializer_mapping = {
    # Question: QuestionSerializer,
    TextQuestion: TextQuestionSerializer,
    ChoiceQuestion: ChoiceQuestionSerializer,
    MultiChoicesQuestion: MultiChoicesQuestionSerializer
}


class QuestionUnionSerializer(PolymorphicSerializer):
    model_serializer_mapping = question_model_serializer_mapping


class AnswerReadSerializer(serializers.ModelSerializer):
    owner = AnswerOwnerUnionSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'


class TextAnswerReadSerializer(AnswerReadSerializer):
    # question = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = TextAnswer
        fields = '__all__'


class ChoiceAnswerReadSerializer(AnswerReadSerializer):
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    answer = ChoiceVariationsSerializer(read_only=True)

    class Meta:
        model = ChoiceAnswer
        fields = '__all__'
        # exclude = 'polymorphic_ctype',


class MultiChoicesAnswerReadSerializer(AnswerReadSerializer):
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    answer = MultiChoicesVariationsSerializer(many=True, read_only=True)

    class Meta:
        model = MultiChoicesAnswer
        fields = '__all__'
        # exclude = 'polymorphic_ctype',


class AnswerCreateSerializer(serializers.ModelSerializer):
    # owner = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Answer
        fields = '__all__'


class TextAnswerCreateSerializer(AnswerCreateSerializer):
    class Meta:
        model = TextAnswer
        fields = '__all__'


class ChoiceAnswerCreateSerializer(AnswerCreateSerializer):
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    answer = ChoiceVariationsSerializer(read_only=True)

    class Meta:
        model = ChoiceAnswer
        fields = '__all__'
        # exclude = 'polymorphic_ctype',


class MultiChoicesAnswerCreateSerializer(AnswerCreateSerializer):
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    answer = MultiChoicesVariationsSerializer(many=True, read_only=True)

    class Meta:
        model = MultiChoicesAnswer
        fields = '__all__'
        # exclude = 'polymorphic_ctype',


answer_model_serializer_mapping = {
    # Answer: AnswerSerializer,
    TextAnswer: TextAnswerReadSerializer,
    ChoiceAnswer: ChoiceAnswerReadSerializer,
    MultiChoicesAnswer: MultiChoicesAnswerReadSerializer,
}
answer_create_model_serializer_mapping = {
    # Answer: AnswerSerializer,
    TextAnswer: TextAnswerCreateSerializer,
    ChoiceAnswer: ChoiceAnswerCreateSerializer,
    MultiChoicesAnswer: MultiChoicesAnswerCreateSerializer,
}


class AnswerUnionReadSerializer(PolymorphicSerializer):
    model_serializer_mapping = answer_model_serializer_mapping


class AnswerUnionCreateSerializer(PolymorphicSerializer):
    model_serializer_mapping = answer_create_model_serializer_mapping


class InterviewSerializer(serializers.ModelSerializer):
    questions = QuestionUnionSerializer(read_only=True, many=True)

    class Meta:
        model = Interview
        fields = '__all__'


class InterviewUpdateSerialize(serializers.ModelSerializer):
    class Meta:
        model = Interview
        exclude = 'start_at',
