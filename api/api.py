from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# Functions for encryption and validation
# password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
# bcrypt.check_password_hash(password_hash, user_input)


# Create the app
app = Flask(__name__)

# Create the API
#api = Api(app)

# # Setup our Bcrypt encryption
# bcrypt = Bcrypt(app)

# Setup database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://scopeandtrackAdmin:T@ylor8575@localhost/scopeandtrack"
db = SQLAlchemy(app)


class organizations(db.Model):
    orgID = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String(255), unique = True)
    address1 = db.Column(db.String(255))
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(2))
    zipCode = db.Column(db.Integer)
    country = db.Column(db.String(2))
    phone1 = db.Column(db.BigInteger)
    phone2 = db.Column(db.BigInteger)
    email1 = db.Column(db.String(255))
    email2 = db.Column(db.String(255))
    primaryContact = db.Column(db.String(255))


    def __init__(self, orgID, name, address1, address2, city, state, zipCode, country, phone1, phone2, email1, email2, primaryContact):
        self.orgID = orgID
        self.name = name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.country = country
        self.phone1 = phone1
        self.phone2 = phone2
        self.email1 = email1
        self.email2 = email2
        self.primaryContact = primaryContact



@app.route("/api", methods=["GET"])
def hello():
    return "Hello World!"



@app.route("/api/organizations", methods=["GET"])
def getOrgs():
    orgs = organizations.query.all()
    return jsonify({"organizations": orgs})



if __name__ == "__main__":
    app.run()



