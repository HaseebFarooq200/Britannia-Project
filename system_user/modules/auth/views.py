from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import views, status, permissions
from rest_framework.response import Response
from system_user.modules.auth.serializer import CustomUserSerializer


class RegisterAPI(views.APIView):
    permission_classes = []

    def post(self, request):
        user = CustomUserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(
                data={
                    "Status": "success",
                    "Message": "Registered Successfully. please login.",
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            data={"Status": "failed", "Message": "Please provide valid details"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class LoginAPI(views.APIView):
    permission_classes = []

    def post(self, request):
        email = request.data["Email"]
        password = request.data["password"]

        user = authenticate(request, username=email, password=password)
        print("USER", user)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            auth_data = {
                "RefreshToken": str(refresh),
                "AccessToken": str(refresh.access_token),
            }

            return Response(
                data={"Status": "success", "Result": auth_data},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data={"Status": "failed", "Message": "User record doesnot exist."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class LogoutAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(
            data={"Status": "success", "Message": "Successfully Logged out!"},
            status=status.HTTP_200_OK,
        )
