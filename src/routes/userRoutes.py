from flask import Blueprint
import controllers

user_blueprint = Blueprint('user_bp',__name__)
user_blueprint.route("/add", methods=['POST'])(controllers.add_user)
user_blueprint.route("/all", methods=['GET'])(controllers.get_user)
user_blueprint.route("/get", methods=['GET'])(controllers.get_user_by_id)