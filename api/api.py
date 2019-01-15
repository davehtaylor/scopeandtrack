from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import datetime


# Create the app
app = Flask(__name__)


# Setup database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://scopeandtrackAdmin:T@ylor8575@localhost/scopeandtrack"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)



###############################################################################
#                                                                             #
#                            Classes for DB tables                            #
#                                                                             #
###############################################################################



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
    """
    All fields are mandatory
    """
    __tablename__ = "users"
    userID = db.Column(db.Integer, primary_key = True, unique = True)
    firstName = db.Column(db.String(255), nullable = False)
    lastName = db.Column(db.String(255), nullable = False)
    username = db.Column(db.String(255), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    privLevel = db.Column(db.Integer, nullable = False)
    orgID = db.Column(db.Integer, nullable = False)

    def __init__(self, userID, firstName, lastName, username, 
                 password, privLevel, orgID):
        self.userID = userID
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.privLevel = privLevel
        self.orgID = orgID

    def toJSON(self):
        """
        Create a serializable representation of our data, so we can return
        JSON from our DB queries. This will return the user's info without
        password data.
        """
        return {
            "userID": self.userID,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "username": self.username,
            "privLevel": self.privLevel,
            "orgID": self.orgID
        }


class dsdMachines(db.Model):
    """
    nickname is optional
    """
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
    nickname is optional
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


###############################################################################
#                                                                             #
#                           organizations endpoints                           #
#                                                                             #
###############################################################################



@app.route("/api/organizations", methods=["POST", "GET"])
def orgs():
    """
    Create organizations, or list all organizations
    Ensure that we recieve a JSON request, and that it contains the mandatory 
    fields. All fields except address2, phone2, and email2 are mandatory.
    Return 200 OK if orgs are found to list, 201 Created for a successful org 
    creation, or 400 Bad Request otherwise.
    """
    if request.method == "POST":
        if not request.json:
            return jsonify({"error": "No properly formatted JSON request was recieved"}), 400

        incoming = request.get_json()
        
        mandatory = [incoming.get("name"), incoming.get("address1"),
                     incoming.get("city"), incoming.get("state"), 
                     incoming.get("zipCode"), incoming.get("country"), 
                     incoming.get("phone1"), incoming.get("email1"), 
                     incoming.get("primaryContact")]
        
        if None in mandatory:
            return jsonify({"error": "Missing required fields: name, address1, city, state, zipCode, country, phone1, email, or primaryContact"}), 400

        org = organizations(None, incoming.get("name"), incoming.get("address1"), incoming.get("address2"),
                            incoming.get("city"), incoming.get("state"), incoming.get("zipCode"),
                            incoming.get("country"), incoming.get("phone1"), incoming.get("phone2"),
                            incoming.get("email1"), incoming.get("email2"), incoming.get("primaryContact"))

        db.session.add(org)
        db.session.commit()

        return jsonify({"organization": org.toJSON()}), 201

    elif request.method == "GET":
        orgs = [o.toJSON() for o in organizations.query.all()]

        if len(orgs) == 0:
            return jsonify({"result": "No organizations found"}), 200

        return jsonify({"organizations": orgs}), 200

    else:
        return "", 400


@app.route("/api/organizations/<int:id>", methods=["GET", "PUT", "DELETE"])
def orgsByID(orgID):
    """
    Get, update, or delete organization info by ID. 
    Return 200 OK for success, 400 Bad Request otherwise.
    """
    org = organizations.query.get(orgID)

    if org is None:
        return jsonify({"result": "No organization found"}), 200

    if request.method == "GET":
        return jsonify({"organization": org.toJSON()}), 200
    
    elif request.method == "PUT":
        incoming = request.get_json()

        mandatory = [incoming.get("name"), incoming.get("address1"),
                     incoming.get("city"), incoming.get("state"), 
                     incoming.get("zipCode"), incoming.get("country"), 
                     incoming.get("phone1"), incoming.get("email1"), 
                     incoming.get("primaryContact")]
        
        if None in mandatory:
            return jsonify({"error": "Missing required fields: name, address1, city, state, zipCode, country, phone1, email, or primaryContact"}), 400

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
    
    elif request.method == "DELETE":
        db.session.delete(org)
        db.session.commit()
        return jsonify({"result": "Organization " + orgID + " deleted"}), 200
    
    else:
        return "", 400



###############################################################################
#                                                                             #
#                               users endpoints                               #
#                                                                             #
###############################################################################



@app.route("/api/organizations/<int:orgID>/users", methods=["POST"])
def createUser(orgID):
    """
    Create a user for a given organization. 
    Ensure that we recieve a JSON request, and that it contains the mandatory
    fields. nickname and orgID are otpional.
    Return 400 Bad Request code if there's a problem.
    Return 201 Created for a successful creation.
    """
    if not request.json:
        return jsonify({"error": "No properly formatted JSON request was recieved"}), 400

    incoming = request.get_json()

    mandatory = [incoming.get("firstName"), incoming.get("lastName"),
                 incoming.get("username"), ncoming.get("password"),
                 incoming.get("privLevel")]

    if None in mandatory:
        return jsonify({"error": "Missing required fields: firstName, lastName, username, password, or privLevel"}), 400

    user = users(None, incoming.get("firstName"), incoming.get("lastName"),
                 incoming.get("username"), incoming.get("password"),
                 incoming.get("privLevel"), orgID)

    db.session.add(user)
    db.session.commit()

    return jsonify({"user": user.toJSON()}), 201


@app.route("/api/organizations/users", methods=["GET"])
def getUsers():
    """
    Get all users. Return all info except password info. 
    Return 200 OK for success, 204 No Content if no users are found. 
    """
    userList = [u.toJSON() for u in users.query.all()]

    if len(userList) == 0:
        return jsonify({"result": "No users found"}), 200

    return None


@app.route("/api/organizations/<int:orgID>/users", methods=["GET"])
def getUsersByOrg(orgID):
    """
    Get all users for a given organization. Return all info except password info. 
    Return 200 OK for success, 204 No Content if no machines are found. 
    """
    userList = [u.toJSON() for u in users.query.filter(users.orgID == orgID)]

    if len(userList) == 0:
        return jsonify({"result": "No users for organization ID " + orgID + " found"}), 204

    return None


@app.route("/api/users/<int:userID>", methods=["GET", "PUT", "DELETE"])
def userByID(userID):
    """
    Get, update, or delete users by scopeID.
    Return 200 OK for success 400 Bad Request otherwise.
    """
    user = users.query.get(userID)

    if user == None:
        return jsonify({"result": "No user with ID " + userID + " found"})

    if request.method == "GET":
        return jsonify({"user": user.toJSON()}), 200

    elif request.method == "PUT":
        incoming = request.get_json()

        mandatory = [incoming.get("firstName"), incoming.get("lastName"),
                     incoming.get("username"), ncoming.get("password"),
                     incoming.get("privLevel")]

        if None in mandatory:
            return jsonify({"error": "Missing required fields: firstName, lastName, username, password, or privLevel"}), 400

        user.firstName = incoming.get("firstName")
        user.lastName = incoming.get("lastName")
        user.username = incoming.get("username")
        user.password = incoming.get("password")
        user.privLevel = incoming.get("privLevel")

        db.session.commit()

        return jsonify({"user": user.toJSON()}), 200

    elif request.method == "DELETE":
        db.session.delete(userID)
        db.session.commit()

        return jsonify({"result": "User " + userID + " deleted"}), 200

    else:
        return "", 400



###############################################################################
#                                                                             #
#                               scopes endpoints                              #
#                                                                             #
###############################################################################



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
        return jsonify({"error": "No properly formatted JSON request was recieved"}), 400

    incoming = request.get_json()

    mandatory = [incoming.get("make"), incoming.get("model"), incoming.get("serial"),
                 incoming.get("inService")]

    if None in mandatory:
        return jsonify("error": "Missing required fields: make, model, serial, or inService"), 400

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
        return jsonify({"result": "No scopes found"}), 200

    return jsonify({"scopes": scopeList}), 200


@app.route("/api/organizations/<int:orgID>/scopes", methods=["GET"])
def getScopesByOrg(orgID):
    """
    Get all scopes for a given organization. 
    Return 200 OK for success, 204 No Content if no scopes are found. 
    """
    scopeList = [s.toJSON() for s in scopes.query.filter(scopes.orgID == orgID)]

    if len(scopeList) == 0:
        return jsonify({"result": "No scopes for organization ID " + orgID + " found"}), 204

    return jsonify({"scopes": scopeList}), 200


@app.route("/api/scopes/<int:scopeID>", methods=["GET", "PUT", "DELETE"])
def scopeByID(scopeID):
    """
    Get, update, or delete scope by scopeID.
    Return 200 OK for success 400 Bad Request otherwise.
    """
    scope = scopes.query.get(scopeID)

    if scope is None:
        return jsonify({"result": "No scope with ID " + scopeID + " found"}), 200

    if request.method == "GET":
        return jsonify({"scope": scope.toJSON()}), 200

    elif request.method == "PUT":
        incoming = request.get_json()

        mandatory = [incoming.get("make"), incoming.get("model"), incoming.get("serial"),
                     incoming.get("inService")]

        if None in mandatory:
            return jsonify({"error": "Missing required fields: make, model, serial, or inService"}), 400

        scope.make = incoming.get("make")
        scope.model = incoming.get("model")
        scope.serial = incoming.get("serial")
        scope.nickname = incoming.get("nickname")
        scope.inService = incoming.get("inService")

        db.session.commit()

        return jsonify({"scope": scope.toJSON()}), 200

    elif request.method == "DELETE":
        db.session.delete(scopeID)
        db.session.commit()

        return jsonify({"result": "Scope " + scopeID + " deleted"}), 200

    else: 
        return "", 400



###############################################################################
#                                                                             #
#                            dsdMachines endpoints                            #
#                                                                             #
###############################################################################



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
        return jsonify({"error": "No properly formatted JSON request was recieved"}), 400

    incoming = request.get_json()

    mandatory = [incoming.get("make"), incoming.get("model"), incoming.get("serial"), 
                 incoming.get("dateLastMaintenance"), incoming.get("dateNextMaintenance")]

    if None in mandatory:
        return jsonify({"error": "Missing required fields: make, model, serial, dateLastMaintenance, or dateNextMaintenance"}), 400

    # Make our date string something the query can understand. We have to send
    # a datetime.date object
    # dateLast = incoming.get("dateLastMaintenance").split('-')
    # dateNext = incoming.get("dateNextMaintenance").split('-')
    dateLast = datetime.strptime(incoming.get("dateLastMaintenance"), "%y-%m-%d")
    dateNext = datetime.strptime(incoming.get("dateNextMaintenance"), "%y-%m-%d")
    
    # machine = dsdMachines(None, incoming.get("make"), incoming.get("model"), 
    #                       incoming.get("serial"), incoming.get("nickname"),
    #                       datetime.date(int(dateLast[0]), int(dateLast[1]), int(dateLast[2])), 
    #                       datetime.date(int(dateNext[0]), int(dateNext[1]), int(dateNext[2])), 
    #                       orgID)
    machine = dsdMachines(None, incoming.get("make"), incoming.get("model"), 
                          incoming.get("serial"), incoming.get("nickname"),
                          dateLast, dateNext, orgID)

    db.session.add(machine)
    db.session.commit()

    return jsonify({"dsdMachine": machine.toJSON()}), 201


@app.route("/api/dsdmachines", methods=["GET"])
def getDSDMachines():
    """
    Get all DSD machines. 
    Return 200 OK for success. 
    """
    machines = [m.toJSON() for m in dsdMachines.query.all()]

    if len(machines) == 0:
        return jsonify({"result": "No DSD machines found"}), 200

    return jsonify({"dsdMachines": machines}), 200


@app.route("/api/organizations/<int:orgID>/dsdmachines", methods=["GET"])
def getDSDMachinesByOrg(orgID):
    """
    Get all DSD machines for a given organization.
    Return 200 OK for success.
    """
    machines = [m.toJSON() for m in dsdMachines.query.filter(dsdMachines.orgID == orgID)]

    if len(machines) == 0:
        return jsonify({"result": "No machines for organization ID " + orgID + " found"}), 200

    return jsonify({"dsdMachines": machines}), 200


@app.route("/api/dsdmachines/<int:machineID>", methods=["GET", "PUT", "DELETE"])
def dsdMachineByID(machineID):
    """
    Get, update, or delete DSD machine by machineID.
    Return 200 OK for success, 400 Bad Request otherwise
    """
    machine = dsdMachines.query.get(machineID)

    if machine is None:
        return jsonify({"result": "No machine with ID " + machineID + " found"}), 200

    if request.method == "GET":
        return jsonify({"dsdMachine": machine.toJSON()}), 200

    elif request.method == "PUT":
        incoming = request.get_json()

        mandatory = [incoming.get("make"), incoming.get("model"), incoming.get("serial"), 
                     incoming.get("dateLastMaintenance"), incoming.get("dateNextMaintenance")]

        if None in mandatory:
            return jsonify({"error": "Missing required fields: make, model, serial, dateLastMaintenance, or dateNextMaintenance"}), 400

        machine.name = incoming.get("make")
        machine.model = incoming.get("model")
        machine.serial = incoming.get("serial")
        machine.nickname = incoming.get("nickname")
        machine.dateLastMaintenance = incoming.get("dateLastMaintenance")
        machine.dateNextMaintenance = incoming.get("dateNextMaintenance")

        db.session.commit()

        return jsonify({"machine": machine.toJSON()}), 200

    elif request.method == "DELETE":
        db.session.delete(machineID)
        db.session.commit()

        return jsonify({"result": "DSD machine " + machineID + " deleted"}), 200

    else:
        return "", 400



###############################################################################
#                                                                             #
#                             Main page endpoints                             #
#                                                                             #
###############################################################################



@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run()

