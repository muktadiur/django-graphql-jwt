import graphene
from books.schema import Query as BookQuery

class Query(BookQuery, graphene.ObjectType):
    pass

SCHEMA = graphene.Schema(query=Query)