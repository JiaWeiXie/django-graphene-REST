import graphene
from graphene import Node

from . import scalars


class BaseModelType:
    created = graphene.Field(scalars.DateTime)
    modified = graphene.Field(scalars.DateTime)


class IDNode(Node):
    id = graphene.ID(required=True)

    class Meta:
        name = 'Node'

    @staticmethod
    def to_global_id(type, id):
        return id

    @staticmethod
    def get_node_from_global_id(info, global_id, only_type=None):
        get_node = getattr(only_type, "get_node", None)
        if get_node:
            return get_node(info, global_id)
