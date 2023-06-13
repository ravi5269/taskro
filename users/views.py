from django.shortcuts import render
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from users.serializers import User
from rest_framework import status
from users.admin import User

from rest_framework.generics import get_object_or_404



# Create your views here.
class UserRegisterAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        requested_data = request.data
        try:
            if User.objects.filter(username=requested_data.get("username")):
                return Response(
                    {"message": "user already exists", "status": False},
                    status=status.HTTP_302_FOUND,
                )
            serializer = UserSerializer(data=requested_data)
            if serializer.is_valid(raise_exception=True):
                serializer.create(validated_data=requested_data)
                return Response(
                    {"message": " user registrations successful", "status": True},
                    status=status.HTTP_201_CREATED,
                )
        except Exception as e:
            return Response(
                {"message": "user already register", "status": False},
                status=status.HTTP_302_FOUND,
            )


class UserAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(
                {"message": "success", "status": True},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Exception as e:
            return Response(
                {"message": "user not found ", "status": False},
                status=status.HTTP_302_FOUND,
            )

    def get(self, request, pk=None):
        try:
            if pk:
                user = User.objects.get(id=pk)
                serializer = UserSerializer(user)

                return Response(
                    {"message": "success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )

            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            print(request.user)
            return Response(
                {"message": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"message": "user not found ", "status": False},
                status=status.HTTP_302_FOUND,
            )

    def put(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success", "data": serializer.data})
        else:
            return Response({"message": "Data not found", "data": serializer.errors})
