from apiflask import Schema
from apiflask.fields import String, Nested, List, Integer


class RepoOutputSchema(Schema):
    repo_path = String()
    status_code = Integer()
    message = String()


class RepoInputSchema(Schema):
    repo_path = String(required=True)


class RepoListSchema(Schema):
    datas = List(Nested(RepoOutputSchema))
    status_code = Integer()
    message = String()
