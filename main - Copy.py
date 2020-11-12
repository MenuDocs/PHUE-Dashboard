from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index_route():
	return 'Hello World!'

@app.route('/auth', methods=["GET", "POST"])
def auth_route():
	if request.method == "GET":
		return render_template('login.html')
	elif request.method == "POST":
		return 'POST Method!'

if __name__ == "__main__":
	app.run(debug=True)

