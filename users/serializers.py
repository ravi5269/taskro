from rest_framework import serializers
from users.models import User

# from users.views import UserAPIView


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get("username"),
        )
        user.set_password(validated_data.get("password"))
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def update(self, instance, validated_data):
        password = validated_data.get("password", instance.password)
        if password:
            instance.set_password(password)
        instance.username = validated_data.get("username", instance.username)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)
        instance.role_title = validated_data.get("role_title", instance.role_title)
        instance.name = validated_data.get("name", instance.name)
        instance.location = validated_data.get("location", instance.location)
        instance.dept = validated_data.get("dept", instance.dept)

        instance.save()

        return instance
