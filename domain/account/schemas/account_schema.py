from apiflask import Schema
from apiflask.fields import String, Email
from apiflask.validators import ValidationError
from marshmallow import validates_schema


class AccountSchema(Schema):
    username = String(required=True)
    email = Email(required=True)
    password = String(required=True)