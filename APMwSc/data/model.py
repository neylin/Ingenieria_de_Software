'''
    Universidad Simon Bolivar.
    Ingenieria de Software I
    Integrantes:
        *.- Neylin Belisario. Carnet: 09-10093 
        *.- Oriana Graterol.  Carnet: 10-11248
    Equipo: SoftDev
    Trimestre Abril - Julio 2015
'''

# --------------------- IMPORTACIONES --------------------- #

import settings

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, Text, Float
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy.engine.url import URL

# --------------------------------------------------------- #

engine = create_engine(URL(**settings.DATABASE))    
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

db = declarative_base()
db.query = session.query_property()

class User(db):
    __tablename__ = 'user'
    fullname = Column(String(50), unique = True)
    username = Column(String(16), primary_key = True)
    password = Column(String(16), unique = True)
    email = Column(String(30), unique = True)
    iddpt = Column(Integer, ForeignKey('dpt.iddpt'))
    idrole = Column(Integer,ForeignKey('role.idrole'))

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
    __tablename__ = 'dpt'
    iddpt = Column(Integer, primary_key = True)
    namedpt = Column(String(50), unique = True)
    user_dpt = relationship('user', backref = 'dpt', lazy = 'dynamic')

    def __init__(self, iddpt, namedpt):
        '''
        Constructor
        '''
        self.iddpt = iddpt
        self.namedpt = namedpt
        
# Roles
class Role(db):
    __tablename__ = 'role'
    idrole = Column(Integer, primary_key = True)
    namerole = Column(String(50), unique = True)
    user_role = relationship('user', backref = 'role', lazy = 'dynamic')

    def __init__(self, idrole, namerole):
        '''
        Constructor
        '''
        self.idrole = idrole
        self.namerole = namerole

def create_tables():
    db.metadata.create_all(engine)

def main():
    create_tables()

if __name__ == "__main__":
    main()
