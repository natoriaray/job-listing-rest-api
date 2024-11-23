from db import db

class AppliedModel(db.Model):
    __tablename__ = "applied"
    id = db.Column(db.Integer, primary_key=True)
    applicant_id = db.Column(db.Integer, db.ForeignKey("applicants.id"))
    job_id = db.Column(db.Integer, db.ForeignKey("job.id"))