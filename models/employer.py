from db import db

class EmployerModel(db.Model)
    __tablename__ = "employers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    jobs = db.relationship("JobModel", back_populates="employers", lazy="dynamic", cascade="all, delete")