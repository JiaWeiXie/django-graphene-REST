import graphene

from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from rest_framework import exceptions, permissions

from django.contrib.auth.models import User, Group

from gql import scalars, object_types
from gql.decorators import rest_permission


class UserNode(DjangoObjectType):
    date_joined = graphene.Field(scalars.DateTime)
    last_login = graphene.Field(scalars.DateTime)

    @rest_permission([permissions.IsAdminUser])
    def resolve_is_superuser(parent, info):
        return parent.is_superuser

    class Meta:
        model = User
        filter_fields = ['id', 'username', 'email']
        exclude = ('user_permissions', 'password')
        interfaces = (object_types.IDNode, )


class GroupNode(DjangoObjectType):

    class Meta:
        model = Group
        filter_fields = ['id', 'name']
        exclude = ('permissions',)
        interfaces = (object_types.IDNode,)


class Query(graphene.ObjectType):
    user = object_types.IDNode.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)

    group = object_types.IDNode.Field(GroupNode)
    all_groups = DjangoFilterConnectionField(GroupNode)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    @rest_permission([permissions.IsAdminUser])
    def resolve_all_groups(self, info, **kwargs):
        return Group.objects.all()