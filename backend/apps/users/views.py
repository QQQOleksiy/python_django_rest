from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from core.permission import IsAdminOrWriteOnly, IsSuperUser
from core.services.email_service import EmailService

from apps.users.filters import UserFilter
from apps.users.models import UserModel as User
from apps.users.serializers import UserSerializer

from .serializers import AvatarSerializer

UserModel: User = get_user_model()


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all_with_profiles()
    filterset_class = UserFilter
    permission_classes = (IsAdminOrWriteOnly,)

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)


class AddAvatarView(UpdateAPIView):
    serializer_class = AvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return UserModel.objects.all_with_profiles().get(pk=self.request.user.pk).profile

    def perform_update(self, serializer):
        self.get_object().avatar.delete()
        super().perform_update(serializer)


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class AdminToUserView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class BlockUserView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class UnBlockUserView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)


class BlockAdminUserView(BlockUserView):
    permission_classes = (IsSuperUser,)


class UnBlockAdminUserView(UnBlockUserView):
    permission_classes = (IsSuperUser,)


class TestEmailView(GenericAPIView):
    permission_classes = (AllowAny,)
    def get(self, *args, **kwargs):
        EmailService.test_email()
        return Response('ok', status.HTTP_200_OK)
