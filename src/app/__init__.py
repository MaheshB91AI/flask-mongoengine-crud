import flask
from flask_mongoengine import MongoEngine
import os
from dotenv import load_dotenv
# from werkzeug.urls import url_quote
app = flask.Flask(__name__)

load_dotenv()


print("Connecting to Mongo.....")
app.config["MONGODB_HOST"] = os.getenv("MONGO_URI")
db = MongoEngine(app)
print("Connected to Mongo")