from apiflask import Schema
from apiflask.fields import String, Email
from apiflask.validators import ValidationError
from marshmallow import validates_schema


class AccountSchema(Schema):
    username = String(required=True)
    email = Email(required=True)
    cpassword = String(required=True)
    password = String(required=True)

    @validates_schema
    def validate_passwords(self, data, **kwargs):
        if data.get('password') != data.get('cpassword'):
            raise ValidationError('Passwords do not match.', field_names=['password', 'cpassword'])