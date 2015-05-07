import settings

import os
from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from db_create import *
#import db_migrate


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
db = SQLAlchemy(app)

#--- TABLAS DE LA BASE DE DATOS
# Usuarios
class User(db.Model):
    __tablename__ = 'usuarios'
    fullname = db.Column(db.String(50), unique = True)
    username = db.Column(db.String(16), primary_key = True)
    password = db.Column(db.String(16), unique = True)
    email = db.Column(db.String(30), unique = True)
    iddpt = db.Column(db.Integer, db.ForeignKey('dpt.iddpt'))
    idrole = db.Column(db.Integer, db.ForeignKey('role.idrole'))

    def __init__(self, fullname, username, password, email, iddpt, idrole):
        '''
        Constructor
        '''
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        self.iddpt = iddpt
        self.idrole = idrole

    def __repr__(self):
        return '<User %r>' % self.username

# Departamentos
class Dpt(db.Model):
    __tablename__ = 'departamentos'
    iddpt = db.Column(db.Integer, primary_key = True)
    namedpt = db.Column(db.String(50), unique = True)
    user_dpt = db.relationship('user', backref = 'dpt', lazy = 'dynamic')

    def __init__(self, iddpt, namedpt):
        '''
        Constructor
        '''
        self.iddpt = iddpt
        self.namedpt = namedpt
        self.user_dpt = user_dpt

    def __repr__(self):
        return '<User %r>' % self.iddpt
        
# Roles
class Role(db.Model):
    __tablename__ = 'roles'
    idrole = db.Column(db.Integer, primary_key = True)
    namerole = db.Column(db.String(50), unique = True)
    user_role = db.relationship('user', backref = 'role', lazy = 'dynamic')

    def __init__(self, idrole, namerole):
        '''
        Constructor
        '''
        self.idrole = idrole
        self.namerole = namerole
        self.user_role = user_role

    def __repr__(self):
        return '<User %r>' % self.idrole
