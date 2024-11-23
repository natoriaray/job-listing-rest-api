from db import db

class ApplicantModel(db.Model):
    __tablename__ = "applicants"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, unique=False, nullable=False)
    last_name = db.Column(db.String, unique=False, nullable=False)
    applied_jobs = db.relationship("JobModel", back_populates="applicants", secondary="applied")
