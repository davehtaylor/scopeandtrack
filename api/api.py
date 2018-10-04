from flask import Flask, request, jsonify, abort
#from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import datetime


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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)



###############################
#                             #
#    Classes for DB tables    #
#                             #
###############################



class organizations(db.Model):
    """
    address2, phone2, and email2 are optional.
    """
    __tablename__ = "organizations"
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
        JSON from our DB queries.
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
    __tablename__ = "users"
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
        JSON from our DB queries.
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



class dsdMachines(db.Model):
    __tablename__ = "dsdMachines"
    machineID = db.Column(db.Integer, primary_key = True, unique = True)
    make = db.Column(db.String(255), nullable = False)
    model = db.Column(db.String(255), nullable = False)
    serial = db.Column(db.String(255), nullable = False)
    nickname = db.Column(db.String(255), unique = True)
    dateLastMaintenance = db.Column(db.DateTime, nullable = False)
    dateNextMaintenance = db.Column(db.DateTime, nullable = False)
    orgID = db.Column(db.Integer, nullable = False)

    def __init__(self, machineID, make, model, serial, nickname,
                 dateLastMaintenance, dateNextMaintenance, orgID):
        self.machineID = machineID
        self.make = make
        self.model = model
        self.serial = serial
        self.nickname = nickname
        self.dateLastMaintenance = dateLastMaintenance
        self.dateNextMaintenance = dateNextMaintenance
        self.orgID = orgID 

    def toJSON(self):
        """
        Create a serializable representation of our data, so we can return
        JSON from our DB queries.
        """
        return {
            "machineID": self.machineID,
            "make": self.make,
            "model": self.model,
            "serial": self.serial,
            "nickname": self.nickname,
            "dateLastMaintenance": str(self.dateLastMaintenance),
            "dateNextMaintenance": str(self.dateNextMaintenance),
            "orgID": self.orgID
        }



class scopes(db.Model):
    """
    inService is an integer, but it's treated as a boolean. Returns 0 or 1.
    """
    __tablename__ = "scopes"
    scopeID = db.Column(db.Integer, primary_key = True, unique = True)
    make = db.Column(db.String(255), nullable = False)
    model = db.Column(db.String(255), nullable = False)
    serial = db.Column(db.String(255), nullable = False)
    nickname = db.Column(db.String(255))
    inService = db.Column(db.Integer, nullable = False)
    orgID = db.Column(db.Integer, nullable = False)

    def __init__(self, scopeID, make, model, serial, nickname, inService, orgID):
        self.scopeID = scopeID
        self.make = make
        self.model = model
        self.serial = serial
        self.nickname = nickname
        self.inService = inService
        self.orgID = orgID 

    def toJSON(self):
        """
        Create a serializable representation of our data, so we can return
        JSON from our DB queries
        """
        return {
            "scopeID": self.scopeID,
            "make": self.make,
            "model": self.model,
            "serial": self.serial,
            "nickname": self.nickname,
            "inService": self.inService,
            "orgID": self.orgID
        }



###############################
#                             #
#   organizations endpoints   #
#                             #
###############################



@app.route("/api/organizations", methods=["POST"])
def createOrg():
    """
    Create organizations. 
    Ensure that we recieve a JSON request, and that it contains the mandatory 
    fields. All fields except address2, phone2, and email2 are mandatory.
    Return 400 Bad Request code if there's a problem.
    Return 201 Created for a successful creation.
    """
    if not request.json:
        abort(400)

    incoming = request.get_json()
    
    mandatory = [incoming.get("name"), incoming.get("address1"),
                 incoming.get("city"), incoming.get("state"), 
                 incoming.get("zipCode"), incoming.get("country"), 
                 incoming.get("phone1"), incoming.get("email1"), 
                 incoming.get("primaryContact")]
    
    if None in mandatory:
        abort(400)

    org = organizations(None, incoming.get("name"), incoming.get("address1"), incoming.get("address2"),
                        incoming.get("city"), incoming.get("state"), incoming.get("zipCode"),
                        incoming.get("country"), incoming.get("phone1"), incoming.get("phone2"),
                        incoming.get("email1"), incoming.get("email2"), incoming.get("primaryContact"))

    db.session.add(org)
    db.session.commit()

    return jsonify({"organization": org.toJSON()}), 201


@app.route("/api/organizations", methods=["GET"])
def getOrgs():
    """
    List all organizations. 
    Return 200 OK for success, 204 No Content if no orgs are found.
    """
    orgs = [o.toJSON() for o in organizations.query.all()]

    if len(orgs) == 0:
        return jsonify({"result": False}), 204

    return jsonify({"organizations": orgs}), 200


@app.route("/api/organizations/<int:id>", methods=["GET"])
def getOrgByID(id):
    """
    Select organization by id. 
    Return 200 OK for success, 204 No Content if id is not found.
    """
    org = organizations.query.get(id)

    if org is None:
        return jsonify({"result": False}), 204

    return jsonify({"organization": org.toJSON()}), 200


@app.route("/api/organizations/<int:id>", methods=["PUT"])
def updateOrg(id):
    """
    Update organization info.
    Return 200 OK code for success, 204 No Content if id is not found.
    """
    org = organizations.query.get(id)

    if org is None:
        return jsonify({"result": False}), 204

    incoming = request.get_json()

    mandatory = [incoming.get("name"), incoming.get("address1"),
                 incoming.get("city"), incoming.get("state"), 
                 incoming.get("zipCode"), incoming.get("country"), 
                 incoming.get("phone1"), incoming.get("email1"), 
                 incoming.get("primaryContact")]
    
    if None in mandatory:
        abort(400)

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


@app.route("/api/organizations/<int:id>", methods=["DELETE"])
def deleteOrg(id):
    """
    Delete organization. 
    Return 200 OK code for success, 204 No Content if id is not found.
    """
    org = organizations.query.get(id)

    if org is None:
        return jsonify({"result": False}), 204

    db.session.delete(org)
    db.session.commit()

    return jsonify({"result": True}), 200



###############################
#                             #
#       users endpoints       #
#                             #
###############################






###############################
#                             #
#       scopes endpoints      #
#                             #
###############################


@app.route("/api/organizations/<int:orgID>/scopes", methods=["POST"])
def createScope(orgID):
    """
    Create a scope for a given organization. 
    Ensure that we recieve a JSON request, and that it contains the mandatory
    fields. nickname and orgID are otpional.
    Return 400 Bad Request code if there's a problem.
    Return 201 Created for a successful creation.
    """
    if not request.json:
        abort(400)

    incoming = request.get_json()

    mandatory = [incoming.get("make"), incoming.get("model"), incoming.get("serial"),
                 incoming.get("inService")]

    if None in mandatory:
        abort(400)

    scope = scopes(None, incoming.get("make"), incoming.get("model"), incoming.get("serial"),
                   incoming.get("nickname"), incoming.get("inService"), orgID)

    db.session.add(scope)
    db.session.commit()

    return jsonify({"scope": scope.toJSON()}), 201


@app.route("/api/scopes", methods=["GET"])
def getScopes():
    """
    Get all scopes. 
    Return 200 OK for success, 204 No Content if no machines are found. 
    """
    scopeList = [s.toJSON() for s in scopes.query.all()]

    if len(scopeList) == 0:
        return jsonify({"result": False}), 204

    return jsonify({"scopes": scopeList}), 200


@app.route("/api/organizations/<int:orgID>/scopes", methods=["GET"])
def getScopesByOrg(orgID):
    """
    Get all scopes for a given organization. 
    Return 200 OK for success, 204 No Content if no scopes are found. 
    """
    scopeList = [s.toJSON() for s in scopes.query.filter(scopes.orgID == orgID)]

    if len(scopeList) == 0:
        return jsonify({"result": False}), 204

    return jsonify({"scopes": scopeList}), 200


@app.route("/api/scopes/<int:scopeID>", methods=["GET"])
def getScopeByID(scopeID):
    """
    Get scope by scopeID.
    Return 200 OK for success, 204 No Content if no scopes are found.
    """
    scope = scopes.query.get(scopeID)

    if scope is None:
        return jsonify({"result": False}), 204

    return jsonify({"scope": scope.toJSON()}), 200


@app.route("/api/scopes/<int:scopeID>", methods=["PUT"])
def updateScope(scopeID):
    """
    Update a scope. 
    Return 200 OK code for success, 204 No Content if id is not found, 
    400 Bad Request if mandatory fields are not present.
    """
    scope = scopes.query.get(scopeID)

    if scope is None:
        return jsonify({"result": False}), 204

    incoming = request.get_json()

    mandatory = [incoming.get("make"), incoming.get("model"), incoming.get("serial"),
                 incoming.get("inService")]

    if None in mandatory:
        abort(400)

    scope.make = incoming.get("make")
    scope.model = incoming.get("model")
    scope.serial = incoming.get("serial")
    scope.nickname = incoming.get("nickname")
    scope.inService = incoming.get("inService")

    db.session.commit()

    return jsonify({"scope": scope.toJSON()}), 200


@app.route("/api/scopes/<int:scopeID>", methods=["DELETE"])
def deleteScope(scopeID):
    """
    Delete a scope. 
    Return 200 OK code for success, 204 No Content if id is not found.
    """
    scope = scopes.query.get(scopeID)

    if scope is None:
        return jsonify({"result": False}), 204

    db.session.delete(scope)
    db.session.commit()

    return jsonify({"result": True}), 200



#####################################
#                                   #
#       dsdMachines endpoints       #
#                                   #
#####################################



@app.route("/api/organizations/<int:orgID>/dsdmachines", methods=["POST"])
def createDSDMachine(orgID):
    """
    Create a DSD machine for a given organization. 
    Ensure that we recieve a JSON request, and that it contains the mandatory
    fields. nickname and orgID are optional.
    Return 400 Bad Request if mandatory fields are not present.
    Return 201 Created for a successful creation.
    """
    if not request.json:
        abort(400)

    incoming = request.get_json()

    mandatory = [incoming.get("make"), incoming.get("model"), incoming.get("serial"), 
                 incoming.get("dateLastMaintenance"), incoming.get("dateNextMaintenance")]

    if None in mandatory:
        abort(400)

    # Make our date string something the query can understand. We have to send
    # a datetime.date object
    dateLast = incoming.get("dateLastMaintenance").split('-')
    dateNext = incoming.get("dateNextMaintenance").split('-')
    
    machine = dsdMachines(None, incoming.get("make"), incoming.get("model"), 
                          incoming.get("serial"), incoming.get("nickname"),
                          datetime.date(int(dateLast[0]), int(dateLast[1]), int(dateLast[2])), 
                          datetime.date(int(dateNext[0]), int(dateNext[1]), int(dateNext[2])), 
                          orgID)

    db.session.add(machine)
    db.session.commit()

    return jsonify({"dsdMachine": machine.toJSON()}), 201
    


@app.route("/api/dsdmachines", methods=["GET"])
def getDSDMachines():
    """
    Get all DSD machines. 
    Return 200 OK for success, 204 No Content if no machines are found. 
    """
    machines = [m.toJSON() for m in dsdMachines.query.all()]

    if len(machines) == 0:
        return jsonify({"result": False}), 204

    return jsonify({"dsdMachines": machines}), 200


@app.route("/api/organizations/<int:orgID>/dsdmachines", methods=["GET"])
def getDSDMachinesByOrg(orgID):
    """
    Get all DSD machines for a given organization.
    Return 200 OK for success, 204 No Content if no machines are found.
    """
    machines = [m.toJSON() for m in dsdMachines.query.filter(dsdMachines.orgID == orgID)]

    if len(machines) == 0:
        return jsonify({"result": False}), 204

    return jsonify({"dsdMachines": machines}), 200


@app.route("/api/dsdmachines/<int:machineID>", methods=["GET"])
def getDSDMachineByID(machineID):
    """
    Get DSD machine by machineID.
    Return 200 OK for success, 204 No Content if no machines are found.
    """
    machine = dsdMachines.query.get(machineID)

    if machine is None:
        return jsonify({"result": False}), 204

    return jsonify({"dsdMachine": machine.toJSON()}), 200


@app.route("/api/dsdmachines/<int:machineID>", methods=["PUT"])
def updateDSDMachine(machineID):
    """
    Update a DSD machine. 
    Return 200 OK code for success, 204 No Content if id is not found, 
    400 Bad Request if mandatory fields are not present.
    """
    machine = dsdMachines.query.get(machineID)

    if machine is None:
        return jsonify({"result": False}), 204

    incoming = request.get_json()

    mandatory = [incoming.get("make"), incoming.get("model"), incoming.get("serial"), 
                 incoming.get("dateLastMaintenance"), incoming.get("dateNextMaintenance")]

    if None in mandatory:
        abort(400)

    machine.name = incoming.get("make")
    machine.model = incoming.get("model")
    machine.serial = incoming.get("serial")
    machine.nickname = incoming.get("nickname")
    machine.dateLastMaintenance = incoming.get("dateLastMaintenance")
    machine.dateNextMaintenance = incoming.get("dateNextMaintenance")

    db.session.commit()

    return jsonify({"machine": machine.toJSON()}), 200


@app.route("/api/dsdmachines/<int:machineID>", methods=["DELETE"])
def deleteDSDMachine(machineID):
    """
    Delete a DSD machine. 
    Return 200 OK code for success, 204 No Content if id is not found.
    """
    machine = dsdMachines.query.get(machineID)

    if machine is None:
        return jsonify({"result": False}), 204

    db.session.delete(machine)
    db.session.commit()

    return jsonify({"result": True}), 200




#####################################
#                                   #
#         main page endpoint        #
#                                   #
#####################################

@app.route('/')
def root():
    return app.send_static_file('index.html')



if __name__ == "__main__":
    app.run()

