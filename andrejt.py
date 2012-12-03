from flask import Flask, render_template
from subprocess import call

app = Flask(__name__)
# app.debug = True

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/update', methods=['POST'])
def update():
	call(['git', 'pull'])
	return "Success."

@app.route('/dali_mi_raboti_sajtot_na_internet_explorer')
def ie():
	return "Ne."

if __name__ == "__main__":
	app.run("0.0.0.0", port=80, use_reloader=True)