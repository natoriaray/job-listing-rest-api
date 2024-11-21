from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import JobModel

blp = Blueprint("job", __name__, description="Operations on jobs")

@blp.route("/job")
class JobList(MethodView):
    def get(self):
        return JobModel.query.all()
    
    def post(self, job_data):
        pass

@blp.route("/job/<int:job_id>")
class Job(MethodView):
    def get(self, job_id):
        pass

    def put(self, job_id):
        pass

    def delete(self, job_id):
        pass


@blp.route("/employer/<int:employer_id>/job")
class JobWithEmployer(MethodView):
    def get(self, employer_id):
        pass


