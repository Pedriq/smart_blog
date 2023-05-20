from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from apps.users.models import User

class UserCreateSerializer(UserCreateSerializer):
    """
    The serializer for the User model.

    Added 'password_confirmation' field which is not a model field
    for the field in the registration form 'repeat password'
    """
    
    password_confirmation = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'password', 'password_confirmation')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError("Passwords do not match.")
        del attrs['password_confirmation']
        return attrs
