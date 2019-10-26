from django.contrib.auth.models import User, Group

from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password', 'user_permissions']
        read_only_fields = [
            'id', 'last_login', 'date_joined', 'is_active', 'is_staff', 'is_superuser', 'groups'
        ]


class GroupSerializers(serializers.ModelSerializer):

    class Meta:
        model = Group
        exclude = ['permissions']
        read_only_fields = ['id']

