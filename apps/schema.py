import graphene

from .account.graphql import query


class Query(
    query.Query
):
    pass


schema = graphene.Schema(query=Query)

