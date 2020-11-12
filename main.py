from flask import Flask, render_template, request, session

# ROUTER IMPORTS
from routers.auth import authRoute

app = Flask(__name__)
app.secret_key = "menudocs"

# REGISTER ROUTERS
app.register_blueprint(authRoute, url_prefix="/auth")

@app.route('/', methods=["GET"])
def index_route():
	if "user" in session:
		if session["user"] == "vex":
			return render_template("index.html", content="You are logged in!")
		else:
			return render_template("index.html", content="Please log in to view this page!")
	else:
		return render_template("index.html", content="Please log in to view this page!")


if __name__ == "__main__":
	app.run(debug=True)

