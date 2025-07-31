import flask
import sys
from flask_frozen import Freezer


app = flask.Flask(__name__)
app.config["FREEZER_USE_DEFAULT_EXT"] = True
app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'
freezer = Freezer(app)

#app.config['FREEZER_RELATIVE_URLS'] = True


@app.route("/")
@app.route("/index.html")
def index():
    return flask.render_template("index.html")

@app.route("/about.html")
def about():
    return flask.render_template("about.html")

@app.route("/research.html")
def research():
    return flask.render_template("research.html")

# @app.route("/contact.html")
# def contact():
#     return flask.render_template("contact.html")




if __name__ == "__main__":
    
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(debug=True)
