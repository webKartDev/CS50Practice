#importing flask module
from flask import Flask , render_template

#Create a new web app which is a flask app, '__name__' shows the name of the file
app = Flask(__name__)

#Example 1 - Returning / Printing on Main Page
"""
# '/' represents default page of the website, flask is designed in terms of routes
# So when it goes to '/' the function below is run
@app.route("/")
def index():
    return "Hello, World!"
"""
#export FLASK_APP=application.py -->runs flask from application.py
#Example 2 - add another route, we can add more routes like this
"""
@app.route("/karthik")
def karthik():
    return "Hello, Karthik!"
"""
#Example 3 - Running a generalized route --> if we want to make sure run a set of routes
"""
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return "Hello, {}!".format(name)

#for python 3.0+ use
# f"Hello, {name}!"
"""
#Example 4 - Using HTML Tags
"""
@app.route("/<string:name>")
def helloheading(name):
    name = name.capitalize()
    return "<h1>Hello, {}!</h1>".format(name)
"""
#Example 5 - Using Html pages
"""
import render_template from flask lib
create the html file in the folder 'templates'
@app.route("/")
def index():
    return render_template("index.html")
"""
#Example 6 - Using placeholders
"""
@app.route("/")
def index():
    headline = "Hello, Karthik!"
    return render_template("index.html", headline=headline) #passing a template using Jinja2

@app.route("/bye")
def indexbye():
    headline = "Goodbye, Karthik!"
    return render_template("index.html", headline=headline) #passing a template using Jinja2
"""
#Example 7 - Using loops on Ginger 2 - creating isitnewyear website
"""
import datetime

@app.route("/")
def isitnewyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day ==1
    return render_template("newyear.html",new_year=new_year)
"""
#Example 7 - loops in Ginger 2
#export FLASK_DEBUG=1 -->runs flask continously updating
"""
@app.route("/")
def namesindex():
    names = ["Ram","Shaam","Bhaam","Tom","Dick","Harry Potter"]
    return render_template("names.html",names=names)
"""
#Example 7 : urls --> linking different pages
"""
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/isitnewyear")
def isitnewyear():
    return render_template("newyear.html")
    """
#Example 8 : template inheritance --> use a template to put common stuff
"""
@app.route("/")
def page1():
    return render_template("page1.html")

@app.route("/2")
def page2():
    return render_template("page2.html")
"""
#Example 9 : Use data from forms
"""
from flask import request
@app.route("/")
def form():
    return render_template("form.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html",name=name)
"""
#Example 10 : Notes application, defining notes as a global variable
"""
from flask import request, session
from flask_session import Session

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes=[]
@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("notes.html",notes=notes)
"""
#Example 11 : Notes application, Using Dictionary

from flask import request, session
from flask_session import Session

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET","POST"])
def index():
    if session.get("notes") is None:
        session["notes"]=[]
    if request.method=="POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("notes.html",notes=session["notes"])
