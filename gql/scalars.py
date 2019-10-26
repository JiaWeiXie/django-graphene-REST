import datetime
from graphene.types import Scalar
from graphql.language import ast


class DateTime(Scalar):
    """DateTime Scalar Description"""

    @staticmethod
    def serialize(dt):
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def parse_literal(node):
        if isinstance(node, ast.StringValue):
            return datetime.datetime.strptime(
                node.value, "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def parse_value(value):
        return datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
