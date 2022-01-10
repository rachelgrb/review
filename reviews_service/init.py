# Service initializations

import random
import string
import datetime
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# generate random secret key for JWT (will invalidate logged users upon service restart)
app.config['JWT_SECRET_KEY'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(64))

# expiration time for the API
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=24)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=3)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'

jwt = JWTManager(app)
db = SQLAlchemy(app)

