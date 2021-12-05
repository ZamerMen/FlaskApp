from flask import Flask, request, url_for, redirect
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security, current_user

import flask_postgresql
import psycopg2



app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


###ADMIN###
from models import *


class AdminMixin():
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass

admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name='Home'))
admin.add_view(AdminView(Post,db.session))
admin.add_view(AdminView(Tag,db.session))
# admin.add_view(AdminView(Block,db.session))
# admin.add_view(AdminView(Plat,db.session))

### flask-security###
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)