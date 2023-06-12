from django.shortcuts import render
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.serializers import User
from rest_framework import status


# Create your views here.
class UserRegisterAPIView(APIView):
    permission_classes = (AllowAny)
    def post(self, request):
        requested_data = request.data
        # import pdb; pdb.set_trace()
        try:
            if User.objects.filter(username=requested_data.get("username")):
                return Response({"message":"user already exists", "status": False}, status=status.HTTP_302_FOUND)
            serializer = UserSerializer(data=requested_data)
            if serializer.is_valid(raise_exception=True):
                serializer.create(validated_data=requested_data)
                return Response({"message":" user registrations successful", "status": True}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message":"user already register","status":False}, status=status.HTTP_302_FOUND)


