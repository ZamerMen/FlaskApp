from flask import Flask, request
from flask import render_template, url_for
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
import flask_postgresql
import psycopg2





app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


#
