from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


# Function for encryption and validation
# password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
# bcrypt.check_password_hash(password_hash, user_input)


# Create the app
app = Flask(__name__)

# Create the API
api = Api(app)

# Setup our Bcrypt encryption
bcrypt = Bcrypt(app)

# Setup database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "localhost"
db = SQLAlchemy(app)

def hello():
    return "Hello!"

if __name__ == "__main__":
    app.run()



