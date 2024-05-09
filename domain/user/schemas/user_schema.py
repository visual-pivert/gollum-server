from apiflask import Schema
from apiflask.fields import String, Email, List, Nested


class UserInputSchema(Schema):
    username = String(required=True)


class UserOutputSchema(Schema):
    username = String()
    email = Email()
    slug = String()


class UserListSchema(Schema):
    users = List(Nested(UserOutputSchema))
