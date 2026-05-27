from flask import request
import models
import json
from bson import json_util

def add_user_service(name):
    user = models.User(name=name)
    user.save()
    return "user saved"

def get_users_service():
    users = models.User.objects()
    user_list = [user.to_mongo().to_dict() for user in users]
    return json.dumps(user_list, default=json_util.default)
def get_user_by_id_service(user_id):
    user = models.User.objects(_id=str(user_id)).first()
    if not user:
        return json.dumps({
            "message":"User not found"
        }),404
    return json.dumps(user.to_mongo().to_dict(), default=json_util.default)




