from rest_framework.authentication import BaseAuthentication
from user.models import User
from rest_framework import exceptions
import jwt


class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        print(request.headers)

        if ("Authorization") not in request.headers.keys():
            raise exceptions.AuthenticationFailed("Authorization Required")

        if not request.headers["Authorization"]:
            raise exceptions.AuthenticationFailed("USER TOKEN IS REQUIRED")

        token = request.headers["Authorization"].split(" ")[1]

        if not token:
            raise exceptions.AuthenticationFailed("prefix missing")

        try:
            payload = jwt.decode(token, "hypernym%lifemaster", algorithms="HS256")

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("TOKEN EXPIRED")

        except jwt.InvalidTokenError:
            raise exceptions.NotAcceptable("INVALID TOKEN")

        user = User.objects.filter(email=payload["email"]).first()

        if not user:
            if not payload["password"]:
                user = User(email=payload["email"])
                user.username = payload["username"] if payload["username"] else payload["email"]
                user.first_name = payload["first_name"] if payload["first_name"] else None
                user.last_name = payload["last_name"] if payload["last_name"] else None
                user.status = "1"
                user.save()

        return (user, None)