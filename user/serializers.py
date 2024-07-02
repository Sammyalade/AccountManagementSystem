from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


# class UserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username', 'phone', 'password']


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password']
