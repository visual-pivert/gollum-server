from apiflask import Schema
from apiflask.fields import String


class AccessSchema(Schema):
    username = String(required=True)
    password = String(required=True)
