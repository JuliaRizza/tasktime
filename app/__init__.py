# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.models import dbs, forms
from app.routes import index, users, contracts

admin = Admin(app)
admin.add_view(ModelView(dbs.User, db.session))
admin.add_view(ModelView(dbs.Client, db.session))
admin.add_view(ModelView(dbs.Project, db.session))
admin.add_view(ModelView(dbs.Article, db.session))
admin.add_view(ModelView(dbs.Contract, db.session))
admin.add_view(ModelView(dbs.Ticket, db.session))