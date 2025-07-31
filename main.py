import flask
import sys
from flask_frozen import Freezer


app = flask.Flask(__name__)
freezer = Freezer(app)

@app.route("/")
def index():
    return flask.render_template("home.html")

@app.route("/about")
def about():
    return flask.render_template("about.html")

@app.route("/research")
def research():
    return flask.render_template("research.html")

# @app.route("/contact")
# def contact():
#     return flask.render_template("contact.html")



if __name__ == "__main__":
    
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)
