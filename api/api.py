from flask import Flask, request, jsonify, abort
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
    """
    address2, phone2, and email2 are optional
    """
    orgID = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String(255), unique = True, nullable = False)
    address1 = db.Column(db.String(255), nullable = False)
    address2 = db.Column(db.String(255))
    city = db.Column(db.String(255), nullable = False)
    state = db.Column(db.String(2), nullable = False)
    zipCode = db.Column(db.Integer, nullable = False)
    country = db.Column(db.String(2), nullable = False)
    phone1 = db.Column(db.BigInteger, nullable = False)
    phone2 = db.Column(db.BigInteger)
    email1 = db.Column(db.String(255), nullable = False)
    email2 = db.Column(db.String(255))
    primaryContact = db.Column(db.String(255), nullable = False)

    def __init__(self, orgID, name, address1, address2, city, state, zipCode, 
                 country, phone1, phone2, email1, email2, primaryContact):
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

    def toJSON(self):
        """
        Create a serializable representation of our data, so we can return
        JSON from our DB queries
        """
        return {
            "orgID": self.orgID,
            "name": self.name,
            "address1": self.address1,
            "address2": self.address2,
            "city": self.city,
            "state": self.state,
            "zipCode": self.zipCode,
            "country": self.country,
            "phone1": self.phone1,
            "phone2": self.phone2,
            "email1": self.email1,
            "email2": self.email2,
            "primaryContact": self.primaryContact
        }


class users(db.Model):
    userID = db.Column(db.Integer, primary_key = True, unique = True)
    firstName = db.Column(db.String(255))
    lastName = db.Column(db.String(255))
    username = db.Column(db.String(255))
    salt = db.Column(db.String(255))
    password = db.Column(db.String(255))
    privLevel = db.Column(db.Integer)
    orgID = db.Column(db.Integer)

    def __init__(self, userID, firstName, lastName, username, salt, 
                 password, privLevel, orgID):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.salt = salt
        self.password = password
        self.privLevel = privLevel
        self.orgID = orgID

    def toJSON(self):
        """
        Create a serializable representation of our data, so we can return
        JSON from our DB queries
        """
        return {
            "userID": self.userID,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "username": self.username,
            "salt": self.salt,
            "password": self.password,
            "privLevel": self.privLevel,
            "orgID": self.orgID
        }


@app.route("/api/organizations", methods=["POST"])
def createOrg():
    """
    Create organizations. Ensure that we recieve a JSON request, and that it
    contains the mandatory fields. address2, phone2, and email2 are optional.
    Return a 400 Bad Request code if there's a problem.
    We'll return a 201 Created code for a successful creation. 
    """
    # mandatory = ["name", "address1", "city", "state", "zipCode", "country", 
    #              "phone1", "email1", "primaryContact"]

    #if not request.json or not all(mandatory) in request.json:
    if not request.json:
        abort(400)

    incoming = request.get_json()
    mandatory = [incoming.get("name"), incoming.get("address1"),
                 incoming.get("city"), incoming.get("state"), incoming.get("zipCode"),
                 incoming.get("country"), incoming.get("phone1"),
                 incoming.get("email1"), incoming.get("primaryContact")]
    if None in mandatory:
        abort(400)

    org = organizations(None, incoming.get("name"), incoming.get("address1"), incoming.get("address2"),
                        incoming.get("city"), incoming.get("state"), incoming.get("zipCode"),
                        incoming.get("country"), incoming.get("phone1"), incoming.get("phone2"),
                        incoming.get("email1"), incoming.get("email2"), incoming.get("primaryContact"))

    db.session.add(org)
    db.session.commit()
    return jsonify({"organization": org.toJSON()}), 201


@app.route("/api/organizations/<int:id>", methods=["PUT"])
def updateOrg(id):
    """
    Update organization info. Return 200 OK code for success
    """
    org = organizations.query.get(id)
    incoming = request.get_json()

    org.name = incoming.get("name")
    org.address1 = incoming.get("address1")
    org.address2 = incoming.get("address2")
    org.city = incoming.get("city")
    org.state = incoming.get("state")
    org.zipCode = incoming.get("zipCode")
    org.country = incoming.get("country")
    org.phone1 = incoming.get("phone1")
    org.phone2 = incoming.get("phone2")
    org.email1 = incoming.get("email1")
    org.email2 = incoming.get("email2")
    org.primaryContact = incoming.get("primaryContact")

    db.session.commit()
    return jsonify({"organization": org.toJSON()}), 200


@app.route("/api/organizations", methods=["GET"])
def getOrgs():
    """
    List all organizations. Return 200 OK for success
    """
    orgs = [o.toJSON() for o in organizations.query.all()]
    return jsonify({"organizations": orgs}), 200


@app.route("/api/organizations/<int:id>", methods=["GET"])
def getOrgByID(id):
    """
    Select organization by id. Return 200 OK for success
    """
    org = organizations.query.get(id).toJSON()
    return jsonify({"organization": org}), 200


@app.route("/api/organizations/<int:id>", methods=["DELETE"])
def deleteOrg(id):
    """
    Delete organization. Return 200 OK code for success
    """
    db.session.delete(organizations.query.get(id))
    db.session.commit()
    return jsonify({"result": True}), 200



if __name__ == "__main__":
    app.run()

