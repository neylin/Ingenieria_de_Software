'''
Created on May 1, 2015
@author: Neylin Belisario
         Oriana Graterol
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
# --------------------------------------------------------- #

# -- BD a usar -- #
DB_session = sessionmaker(bind = model.engine)
session = DB_session()


class clsRole():
        
    # -- Insertar Rol -- #
    def insert_role(self, idrole, namerole):
        rol = model.Role(idrole, namerole)
        session.add(rol)
        session.commit()
    
    
    # -- Buscar Rol -- #
    def find_role(self, idrole):        
        if (idrole != None):       
            rol = session.query(model.Role).filter(model.Role.idrole == idrole).all()
            return rol
        return None
        
        
    # -- Modificar Rol -- #
    def modify_role_idrole(self, idrole, new):
        if (idrole != None):
            session.query(model.Role).filter(model.Role.idrole == idrole).update({'idrole':(new)})
            session.commit()
            return True
        return None
    
    def modify_role_namerole(self, namerole, new):
        if (namerole != None):
            session.query(model.Role).filter(model.Role.namerole == namerole).update({'namerole':(new)})
            session.commit()
            return True
        return None
        
        
    # -- Borrar Rol -- #
    def delete_role(self, idrole):
        if (idrole != None):
            session.query(model.Role).filter(model.Role.idrole == idrole).delete()
            session.commit()
            return True
        return None