from flask import Flask, request
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore
from flask_security import Security

import flask_postgresql
import psycopg2



app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


###ADMIN###
from models import *
admin = Admin(app)
admin.add_view(ModelView(Post,db.session))
admin.add_view(ModelView(Tag,db.session))
admin.add_view(ModelView(Block,db.session))
admin.add_view(ModelView(Plat,db.session))

### flask-security###
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)