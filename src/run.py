from app import app
import routes


app.register_blueprint(routes.user_blueprint, url_prefix="/user")
app.run(host="0.0.0.0", debug=False)