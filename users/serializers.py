from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get("username"),
        )
        user.set_password(validated_data.get("password"))
        user.save()
        return user


    # def validate(self, data):       
    #    name = data.get("name",None)

    #    if name is None:
    #         raise serializers.ValidationError(
    #             'An name address is required to log in.')
                                                            
