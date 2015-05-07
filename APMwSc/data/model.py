'''
Created on May 1, 2015

@author: Neylin Belisario
         Oriana Graterol
'''

'''
from flask import Flask
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask.ext.sqlalchemy import SQLAlchemy

manager = Manager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db) 
manager.add_command('db',MigrateCommand)

def create_app(config_name):
    app = Flask(__name__)
    #app.config.from.object(config[config_name])
    config[config_name].init_app(app)
    
    db.init_app(app)
'''
import settings


#--- BASE DE DATOS
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import relationship, backref

# Se declara la dase de datos
db = declarative_base()


#--- TABLAS DE LA BASE DE DATOS
# Usuarios
class User(db):
    __tablename__ = 'usuarios'
    fullname = Column(String(50), unique = True)
    username = Column(String(16), primary_key = True)
    password = Column(String(16), unique = True)
    email = Column(String(30), unique = True)
    iddpt = Column(Integer, ForeignKey('dpt.iddpt'))
    idrole = Column(Integer, ForeignKey('role.idrole'))

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

# Departamentos
class Dpt(db):
    __tablename__ = 'departamentos'
    iddpt = Column(Integer, primary_key = True)
    namedpt = Column(String(50), unique = True)
    user_dpt = relationship('user', backref = 'dpt', lazy = 'dynamic')

    def __init__(self, iddpt, namedpt):
        '''
        Constructor
        '''
        self.iddpt = iddpt
        self.namedpt = namedpt
        self.user_dpt = user_dpt
        
# Roles
class Role(db):
    __tablename__ = 'roles'
    idrole = Column(Integer, primary_key = True)
    namerole = Column(String(50), unique = True)
    user_role = relationship('user', backref = 'role', lazy = 'dynamic')

    def __init__(self, idrole, namerole):
        '''
        Constructor
        '''
        self.idrole = idrole
        self.namerole = namerole
        self.user_role = user_role


#--- CARGA A LA BASE DE DATOS
engine = create_engine(URL(**settings.DATABASE))

db.metadata.create_all(engine)



    
    
    

