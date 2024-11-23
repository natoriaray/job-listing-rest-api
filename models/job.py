from db import db

class JobModel(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(80), unique=False, nullable=False)
    salary = db.Column(db.Integer, unique=False, nullable=False)
    city = db.Column(db.String(80), unique=False, nullable=False)
    state = db.Column(db.String(80), unique=False, nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey("employers.id"), unique=False, nullable=False)
    employer = db.relationship("EmployerModel", back_populates="jobs")
    applicants = db.relationship("ApplicantModel", back_populates="applied_jobs", secondary="applied")