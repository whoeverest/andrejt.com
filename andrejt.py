from flask import Flask, render_template
from subprocess import call

app = Flask(__name__)
# app.debug = True

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/update')
def update():
	call(['git', 'pull'])
	return "Success."

if __name__ == "__main__":
	app.run("0.0.0.0", port=80, use_reloader=True)