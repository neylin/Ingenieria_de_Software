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


class clsUser():
        
    # -- Insertar Usuario -- #
    def insert_user(self, fullname, username, password, email, iddpt, idrole):
        if (len(fullname)<= 50) and (len(username)<= 16) and (len(password)<= 16) and (len(email)<= 30) and isinstance(iddpt,int) and isinstance(idrole, int) :
            if ((fullname != None) and (username != None)):
                password_constructor = clsLogin()
                oPassworkEncript = password_constructor.encript(password)
                if oPassworkEncript:
                    print('El Password almacenado en la memoria es: ' + oPassworkEncript)
                
                    #Para validar el passwork introducido
                    oCheckPassword = input('Para verificar su password, ingreselo nuevamente: ')
                    if password_constructor.check_password(oPassworkEncript, oCheckPassword):
                        print('Ha introducido el password correcto')
                        usuario = model.User(fullname,username,password,email,iddpt,idrole)
                        session.add(usuario)
                        session.commit()
                        return True
    
                    else:
                        print('El password es diferente')
                else:
                    print('El Password suministrado NO ES CORRECTO. \n'
                          'Considere que debe contener al menos: \n'
                          '- 1 letra mayuscula y 1 minuscula \n'
                          '- 1 numero \n'
                          '- 1 caracter especial: @ . # $ + * ! \n')
                    return None

    
    # -- Buscar Usuario -- #
    def find_user(self, username): 
        if ((len(username)<=16) and (username != None)):       
            usuario = session.query(model.User).filter(model.User.username == username).all()
            return usuario
        return None


    # -- Modificar Usuario -- #
    def modify_user_fullname(self, fullname, new):
        if (fullname != None):
            session.query(model.User).filter(model.User.fullname == fullname).update({'fullname':(new)})
            session.commit()
            return True
        return None
    
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
        