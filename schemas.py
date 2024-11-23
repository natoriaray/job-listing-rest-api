from marshmallow import Schema, fields
from marshmallow.validate import OneOf

states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", 
    "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", 
    "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", 
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", 
    "WI", "WY"
]

class EmployerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class JobSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    salary = fields.Int(required=True)
    city = fields.Str(required=True)
    state = fields.Str(required=True, validate=OneOf(states))
    employer_id = fields.Int(required=True, load_only=True)
    employer = fields.Nested(EmployerSchema(), dump_only=True)

class FullEmployerSchema(EmployerSchema):
    jobs = fields.List(fields.Nested(JobSchema), dump_only=True)
