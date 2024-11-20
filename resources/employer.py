from flask import request
from flask.views import Methodview
from flask_smorest import Blueprint, abort

blp = Blueprint("employer", __name__, description="Operation on employer")

@blp.route("/employer")
class EmployerList(Methodview):
    def get(self):
        pass

@blp.route("employer/<int:employer_id>")
class Employer(Methodview):
    def get(self):
        pass
