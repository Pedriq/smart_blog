from djoser.serializers import UserCreateSerializer
from apps.users.models import User

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('username','email', 'first_name', 'last_name', 'password')
