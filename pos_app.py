import flask
from flask import request,render_template
from pos import pos_tag
from flask import jsonify

# Initialize the app

app = flask.Flask(__name__,template_folder='templates')

# An example of routing:
# If they go to the page "/" (this means a GET request
# to the page http://127.0.0.1:5000/), return a simple
# page that says the site is up!


@app.route("/")
def home():
	return render_template('home_page.html')

@app.route("/", methods=["POST"])	
def print_tags():
    if request.form['mes']:
        msg = request.form['mes']
        print(msg)
        output = pos_tag(str(msg))
        return render_template('home_page.html',
                                prediction_text = output)

if __name__=="__main__":
	app.run(debug=True)