from flask import Flask, render_template, request, session

# ROUTER IMPORTS
from routers.auth import auth_route
from routers.lights import light_route

app = Flask(__name__)
app.secret_key = "menudocs"

# REGISTER ROUTERS
app.register_blueprint(auth_route, url_prefix="/auth")
app.register_blueprint(light_route, url_prefix="/api/")

@app.route('/', methods=["GET"])
def index_route():
    content = "Please login to view this page!"
    if session.get("user") != "vex":
        return redirect("/auth")

    return render_template('index.html', content=content)


if __name__ == "__main__":
	app.run(debug=True)

