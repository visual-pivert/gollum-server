from apiflask import Schema
from apiflask.fields import String, List, Nested


class ContribInputSchema(Schema):
    username = String(required=True)


class ContribOutputSchema(Schema):
    username = String()


class ContribListSchema(Schema):
    contributors = List(Nested(ContribOutputSchema))
