from apiflask import Schema
from apiflask.fields import String, Nested, List, Integer


class RepoOutputSchema(Schema):
    repo_path = String()
    status_code = Integer()


class RepoInputSchema(Schema):
    repo_path = String(required=True)


class RepoListSchema(Schema):
    repos = List(Nested(RepoOutputSchema))
    status_code = Integer()
