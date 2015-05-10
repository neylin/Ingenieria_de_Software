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
# --------------------------------------------------------- #

# -- BD a usar -- #
DB_session = sessionmaker(bind = model.engine)
session = DB_session()


class clsDpt():
        
    # -- Insertar Departamento -- #
    def insert_dpt(self, iddpt, namedpt):
        
        dpto = model.Dpt(iddpt, namedpt)
        session.add(dpto)
        session.commit()
        
        
    # -- Buscar Departamento -- #
    def find_dpt(self, iddpt): 
        if (iddpt != None):       
            dpto = session.query(model.Dpt).filter(model.Dpt.iddpt == iddpt).all()
            return dpto
        return None
    
    
    # -- Modificar Departamento -- #
    def modify_dpt_iddpt(self, iddpt, new):
        if (iddpt != None):
            session.query(model.Dpt).filter(model.Dpt.iddpt == iddpt).update({'iddpt':(new)})
            session.commit()
            return True
        return None
    
    def modify_dpt_namedpt(self, namedpt, new):
        if (namedpt != None):
            session.query(model.Dpt).filter(model.Dpt.namedpt == namedpt).update({'namedpt':(new)})
            session.commit()
            return True
        return None
        
        
    # -- Borrar Departamento -- #
    def delete_dpt(self, iddpt):
        if (iddpt != None):
            session.query(model.Dpt).filter(model.Dpt.iddpt == iddpt).delete()
            session.commit()
            return True
        return None