import random               # for the random number endpoint
import os                   # for opening file paths

from flask import Flask     # Flask functionality
from flask import request   # handles more than just GET
from flask import Response  # using status codes

from flask_sqlalchemy import SQLAlchemy

HTTP_GOOD = 200
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_INTERNAL_ERR = 405



#-------------------------------------------------------------------
# we figure out where our project path is and set up a database file
# with its full path and the sqlite:/// prefix to tell SQLAlchemy
# which database engine we're using.
#-------------------------------------------------------------------
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "emojidatabase.db"))


app = Flask(__name__)
# we tell our web application where our database will be stored.
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

# we initialize a connection to the database and keep this in
# the db variable. We'll use this to interact with our database.
db = SQLAlchemy(app)


#-------------------------------------------------------------------
# we create a new class which inherits from a basic database model,
# provided by SQLAlchemy. This will also make SQLAlchemy create a table
# called emoji, which it will use to store our Emoji objects.
#-------------------------------------------------------------------
class emoji(db.Model):

    # we create an attribute of our emoji called val. SQLAlchemy will use
    # this as a column name in our emoji table. We say that a val consists
    # of a String of at most 3 unicode characters, that we should never store
    # two or more emoji with the same value (should be unique),
    # that every emoji needs to have a value (the val isn't nullable),
    # and that the val is the main way that we identify a specific emoji
    # in our database (the val is the primary_key).
    val = db.Column(db.String(3), unique=True, nullable=False, primary_key=True)

    # How we represent our emoji as a string
    def __repr__(self):
        return "{}".format(self.val)




@app.route("/", methods=["GET"])
def hello():
    emojis = emoji.query.all()

    list = ''
    for i in range(len(emojis)):
        list += (str(emojis[i]) + "<br/>")

    return Response("Hey welcome to my site! <br/>" + list, status=HTTP_GOOD)


@app.route("/add", methods=["POST"])
def addPOST():
    # if the request.form is not null we recieved a post, print the response
    if request.form:
        # adding emoji to the DB
        if request.form['value'] != '':
            e = emoji(val=request.form['value'])
            try:
                db.session.add(e)
                db.session.commit()
                return Response("Thanks for this cool emoji: " + request.form['value'], status=HTTP_GOOD)
            except Exception as e:
                return Response("ERROR: failed to add emoji: " + request.form['value'], status=HTTP_INTERNAL_ERR)
        else:
            return Response("Sorry, you cant enter a blank value", status=HTTP_FORBIDDEN)
    else:
        return Response("Error: empty response form", status=HTTP_INTERNAL_ERR)


@app.route("/add", methods=["GET"])
def addGET():
    # If the request is a GET, it will return this html instead
    return Response("""
        <html>
            <body>
                <h3> add your favorite emoji to my site </h3>
                <form method="POST" action="/add">
                <input type="text" name="value">
                <input type="submit" value="Add">
                </form>
            </body>
        </html>
        """, status=HTTP_GOOD)


@app.route("/<name>", methods=["GET"])
def helloName(name):
    return Response("hey whats up hows it going " + name, status=HTTP_GOOD)


@app.route("/random", methods=["GET"])
def randomNumGen():
    return Response(str(random.randint(0,100)), status=HTTP_GOOD)


if __name__ == "__main__":

    db.create_all()
    app.run(debug=True)