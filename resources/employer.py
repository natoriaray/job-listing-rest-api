from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import EmployerModel

blp = Blueprint("employer", __name__, description="Operation on employer")

@blp.route("/employer")
class EmployerList(MethodView):
    def get(self):
        return EmployerModel.query.all()
    
    def post(self, employer_data):
        employer = EmployerModel(**employer_data)

        try:
            db.session.add(employer)
            db.session.commit()
        except IntegrityError:
            abort(message="An employer with that name already exists")
        except SQLAlchemyError:
            abort(message="There was an error when creating the employer")
            

@blp.route("/employer/<int:employer_id>")
class Employer(MethodView):
    def get(self, employer_id):
        employer = EmployerModel.query.get_or_404(employer_id)
        return employer

    def delete(self, employer_id):
        employer = EmployerModel.query.get_or_404(employer_id)
        db.session.delete(employer)
        db.session.commit()
        return {"message": "Employer deleted"}

        
