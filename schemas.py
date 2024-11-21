from marshmallow import Schema, fields

class EmployerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class JobSchema(Schema):
    title = fields.Str(required=True)

class FullEmployerSchema(EmployerSchema):
    jobs = fields.List(fields.Nested(JobSchema), dump_only=True)