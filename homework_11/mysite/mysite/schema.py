import graphene

from mycourse.schema import Query as CourseQuery


class Query(CourseQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
