'''
Created on May 1, 2015

@author: neylin
'''
from flask import Flask
from Flask.migrate import Migrate
from Flask.script import Manager
from Flask.sqlalchemy import SQLAlchemy

app = flask(_name_)
manager = Manager(app) 
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

class clsRole(db.Model):
    __tablename__ = 'roles'
    idrole = db.Column(db.Integer, primary_key=True)
    namerole = db.Column(db.String(50), unique=True)
    user_role = db.relationship('clsuser', backref='clsrole', lazy='dynamic')

    def __init__(self, idrole, namerole):
        '''
        Constructor
        '''
        self.idrole = idrole
        self.namerole = namerole
        
    def insert_role(self, idrole, namerole, user_role):
        rol = clsRole(idrole, namerole, user_role)
        db.session.add(rol)
        db.session.commit()
        
    def find_role(self):        
        rol = clsRole.query.filter_by(idrole).first()
        
    def modify_role(self,idrole):
        rol = clsRole(idrole)
        db.session.add(rol)
        db.session.commit()
        
    def delete_role(self, idrole):
        rol = clsRole(idrole)
        db.session.delete(rol)
        db.session.commit()
