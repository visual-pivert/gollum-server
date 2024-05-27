from apiflask import Schema
from apiflask.fields import String, List, Nested, Integer


class ContribInputSchema(Schema):
    username = String(required=True)


class ContribOutputSchema(Schema):
    username = String()
    status_code = Integer()
    message = String()


class ContribListSchema(Schema):
    datas = List(Nested(ContribOutputSchema))
    status_code = Integer()
    message = String()