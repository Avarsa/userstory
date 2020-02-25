from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def root_handler():
	return render_template("index.html")


if __name__ == "__main__":
	#setting host to '0.0.0.0' is mandatory to run the app in repl.it
	app.run(host='0.0.0.0', port=8080, debug=True)
