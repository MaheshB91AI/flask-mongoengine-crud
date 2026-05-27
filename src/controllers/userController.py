from flask import request
import services

def add_user():
    data = request.get_json()
    name = data.get("name")
    return services.add_user_service(name)
def get_user():
    return services.get_users_service()
def get_user_by_id():
    user_id = request.args.get("userId")
    return services.get_user_by_id_service(user_id)