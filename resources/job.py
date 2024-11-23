from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import JobModel, EmployerModel
from schemas import JobSchema

blp = Blueprint("job", __name__, description="Operations on jobs")

@blp.route("/job")
class JobList(MethodView):
    @blp.response(200, JobSchema(many=True))
    def get(self):
        return JobModel.query.all()
    
    @blp.arguments(JobSchema)
    @blp.response(200, JobSchema)
    def post(self, job_data):
        job = JobModel(**job_data)

        try:
            db.session.add(job)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="There was an error when creating the employer")

        return job

@blp.route("/job/<int:job_id>")
class Job(MethodView):
    def get(self, job_id):
        job = JobModel.query.get_or_404(job_id)
        return job

    @blp.arguments(JobSchema)
    @blp.response(200, JobSchema)
    def put(self, job_data, job_id):
        job = JobModel.query.get_or_404(job_id)

        job.title = job_data["title"]
        job.description = job_data["description"]
        job.salary = job_data["salary"]
        job.city = job_data["city"]
        job.state = job_data["state"]
        job.employer_id = job_data["employer_id"]

        db.session.commit()
            
        return job

    def delete(self, job_id):
        job = JobModel.query.get_or_404(job_id)

        db.session.delete(job)
        db.session.commit()

        return {"message": "Job deleted"}


@blp.route("/employer/<int:employer_id>/job")
class JobsWithEmployer(MethodView):
    @blp.response(200, JobSchema(many=True))
    def get(self, employer_id):
        employer = EmployerModel.query.get_or_404(employer_id)
        return employer.jobs.all()


