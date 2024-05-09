from apiflask import Schema
from apiflask.fields import String, Nested, List


class RepoOutputSchema(Schema):
    repo_path = String()


class RepoInputSchema(Schema):
    repo_path = String(required=True)


class RepoListSchema(Schema):
    repos = List(Nested(RepoOutputSchema))
