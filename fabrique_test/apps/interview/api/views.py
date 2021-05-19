from pprint import pprint

from rest_framework import viewsets, permissions, views, status
from rest_framework.response import Response
from drf_rw_serializers import viewsets as rw_view_set
from .serializers import (
    InterviewSerializer,
    QuestionUnionSerializer,
    question_model_serializer_mapping,
    ChoiceVariationsSerializer,
    MultiChoicesVariationsSerializer,
    AnswerUnionReadSerializer,
    AnswerUnionCreateSerializer,
    answer_model_serializer_mapping,
    answer_owner_model_serializer_mapping,
    AnswerOwnerUnionSerializer,
    UserAnswerOwnerSerializer,
    AnonymousUserAnswerOwnerSerializer,
)
from fabrique_test.apps.interview.models import (
    Interview,
    Question,
    ChoiceVariations,
    MultiChoicesVariations,
    Answer,
    AnswerOwner,
    UserAnswerOwner,
    AnonymousUserAnswerOwner,
)
from fabrique_test.apps.interview.filters import (
    InterviewFilter, QuestionFilter, AnswerFilter, ChoiceVariationsFilter, MultiChoicesVariationsFilter
)


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class AnswerOwnerResourceTypeAPIView(views.APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        keys = [key._meta.object_name for key in answer_owner_model_serializer_mapping.keys()]
        return Response(data=keys, status=status.HTTP_200_OK)


class AnswerOwnerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AnswerOwner.objects.all()
    serializer_class = AnswerOwnerUnionSerializer


class AnswerResourceTypeAPIView(views.APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        keys = [key._meta.object_name for key in answer_model_serializer_mapping.keys()]
        return Response(data=keys, status=status.HTTP_200_OK)


class AnswerViewSet(rw_view_set.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerUnionReadSerializer
    filterset_class = AnswerFilter

    read_serializer_class = AnswerUnionReadSerializer
    write_serializer_class = AnswerUnionCreateSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            owner = UserAnswerOwner.objects.create(user=user)
        else:
            owner = AnonymousUserAnswerOwner.objects.create()
        request.data['owner'] = owner.pk
        pprint(request.data)
        return super().create(request, *args, **kwargs)


class ChoiceVariationsViewSet(viewsets.ModelViewSet):
    queryset = ChoiceVariations.objects.all()
    serializer_class = ChoiceVariationsSerializer
    filterset_class = ChoiceVariationsFilter


class MultiChoicesVariationsViewSet(viewsets.ModelViewSet):
    queryset = MultiChoicesVariations.objects.all()
    serializer_class = MultiChoicesVariationsSerializer
    filterset_class = MultiChoicesVariationsFilter


class QuestionResourceTypeAPIView(views.APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        keys = [key._meta.object_name for key in question_model_serializer_mapping.keys()]
        return Response(data=keys, status=status.HTTP_200_OK)


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions | ReadOnly]
    serializer_class = QuestionUnionSerializer
    queryset = Question.objects.select_related('interview').all()

    filterset_class = QuestionFilter


class InterviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions | ReadOnly]

    serializer_class = InterviewSerializer
    queryset = Interview.objects.all()
    filterset_class = InterviewFilter
