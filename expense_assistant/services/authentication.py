from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings


class CustomAuth(JWTAuthentication):
    def auth(self, request):
        headers = self.get_header(request)

        if headers is None:
            token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
        else:
            token = self.get_raw_token(headers)
        if token is None:
            return None

        valid_token = self.get_validated_token(token)

        return self.get_user(valid_token), valid_token