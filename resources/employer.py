from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import EmployerModel
from schemas import FullEmployerSchema

blp = Blueprint("employer", __name__, description="Operations on employers")

@blp.route("/employer")
class EmployerList(MethodView):
    @blp.response(200, FullEmployerSchema(many=True))
    def get(self):
        return EmployerModel.query.all()
    
    @blp.arguments(FullEmployerSchema)
    @blp.response(200, FullEmployerSchema)
    def post(self, employer_data):
        employer = EmployerModel(**employer_data)

        try:
            db.session.add(employer)
            db.session.commit()
        except IntegrityError:
            abort(400, message="An employer with that name already exists")
        except SQLAlchemyError:
            abort(500, message="There was an error when creating the employer")
        
        return employer
            

@blp.route("/employer/<int:employer_id>")
class Employer(MethodView):
    @blp.response(200, FullEmployerSchema)
    def get(self, employer_id):
        employer = EmployerModel.query.get_or_404(employer_id)
        return employer

    def delete(self, employer_id):
        employer = EmployerModel.query.get_or_404(employer_id)
        db.session.delete(employer)
        db.session.commit()
        return {"message": "Employer deleted"}

        
