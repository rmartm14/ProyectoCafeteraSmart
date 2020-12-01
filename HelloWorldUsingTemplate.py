from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
	now = datetime.datetime.now()
	timeString = now.strftime("%d-%m-%Y %H:%M")
	templateData = {
	'title' : 'HelloWorld',
	'time': timeString,
	'message' : 'Hello, World'
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)

