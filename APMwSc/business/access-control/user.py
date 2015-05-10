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
import os
import sys

# Esto permite usar model.py
sys.path.append('../../data')
import model

from login import clsLogin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# --------------------------------------------------------- #

# -- BD a usar -- #
DB_session = sessionmaker(bind = model.engine)
session = DB_session()


class clsUser():
        
    # -- Insertar Usuario -- #
    def insert_user(self, fullname, username, password, email, iddpt, idrole):
        usuario = model.User(fullname,username,password,email,iddpt,idrole)
        session.add(usuario)
        session.commit()

    
    # -- Buscar Usuario -- #
    def find_user(self, username):       
        usuario = session.query(model.User).filter(model.User.username == username).all()
        return usuario


    # -- Modificar Usuario -- #
    def modify_user_fullname(self, fullname, new):
        session.query(model.User).filter(model.User.fullname == fullname).update({'fullname':(new)})
        session.commit()
        return True
    
    def modify_user_username(self, username, new):
        if (username != None):
            session.query(model.User).filter(model.User.username == username).update({'username':(new)})
            session.commit()
            return True
        return None
    
    def modify_user_email(self, email, new):
        if (email != None):
            session.query(model.User).filter(model.User.email == email).update({'email':(new)})
            session.commit()
            return True
        return None
    
    def modify_user_iddpt(self, iddpt, new):
        if (iddpt != None):
            session.query(model.User).filter(model.User.iddpt == iddpt).update({'iddpt':(new)})
            session.commit()
            return True
        return None
    
    def modify_user_idrole(self, idrole, new):
        if (idrole != None):
            session.query(model.User).filter(model.User.idrole == idrole).update({'idrole':(new)})
            session.commit()
            return True
        return None
    
    
    # -- Borrar Usuario -- #
    def delete_user(self, username):
        if (username != None):
            session.query(model.User).filter(model.User.username == username).delete()
            session.commit()
            return True
        return None
    
