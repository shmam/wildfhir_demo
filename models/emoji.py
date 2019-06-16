from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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