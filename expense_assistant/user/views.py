from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from django.middleware import csrf
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.conf import settings

from user.models import User
from user.serializers import UserDataSerializer, SignSerializer
from user.utilities import get_user_token


class UserDataViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserDataSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.filter(is_active=True)

        return User.objects.filter(id=self.request.user.id, is_active=True)


class SignView(APIView):
    def post(self, request):
        serializer = SignSerializer(data=request.data)
        serializer.is_valid()
        response = Response()

        if not serializer.data:
            return Response({'data': 'Bad request.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])

        if user is not None:
            data = get_user_token(user)
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=data['access'],
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
            )
            csrf.get_token(request)
            response.data = {'Success': 'Sign in successfully', 'data': data}

            return response
        else:
            return Response({'data': 'Invalid credentials.'}, status=status.HTTP_404_NOT_FOUND)
