from flask import Flask,make_response,render_template
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('resume.html')

if __name__ == '__main__':
	app.run()
