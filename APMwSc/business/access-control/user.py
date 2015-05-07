  '''
Created on May 1, 2015
@author: Neylin Belisario
         Oriana Graterol
'''

import os
from flask import Flask
from model import db
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from login import clsLogin
from model import User

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
db = SQLAlchemy(app)
db.create_all()



class clsUser():
        
    # -- Insertar Usuario -- #
    def insert_user(self, fullname, username, password, email, iddpt, idrole):
        if (len(fullname)<= 50) and (len(username)<= 16) and (len(password)<= 16) and (len(email)<= 30) and isinstance(iddpt,int) and isinstance(idrole, int) :
            if ((fullname != None) and (username != None)):
                        usuario = model.User(fullname,username,password,email,iddpt,idrole)
                        db.session.add(usuario)
                        db.session.commit()
                        return True
    
            else:
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
        
#Se pide info al usuario 
newFullname = input('Por favor ingrese su nombre: ')
newUsername = input('Por favor ingrese su usuario: ')
newPassword = input('Por favor ingrese su password: ')

password_constructor = clsLogin()
oPassworkEncript = password_constructor.encript(newPassword)
if oPassworkEncript:
    print('El Password almacenado en la memoria es: ' + oPassworkEncript)

    #Para validar el passwork introducido
    oCheckPassword = input('Para verificar su password, ingreselo nuevamente: ')
    if password_constructor.check_password(oPassworkEncript, oCheckPassword):
        print('Ha introducido el password correcto')
        newEmail = input('Por favor ingrese su email: ')
        newIddpt = input('Por favor ingrese su iddpt: ')
        newIdrole = input('Por favor ingrese su idrole: ')
        #Se crea un objeto tipo clsAccessControl
        usuario = clsUser()
        insertar_usuario = usuario.insert_user(newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole)
    else:
        print('El password es diferente')
else:
    print('El Password suministrado NO ES CORRECTO. \n'
          'Considere que debe contener al menos: \n'
          '- 1 letra mayuscula y 1 minuscula \n'
          '- 1 numero \n'
          '- 1 caracter especial: @ . # $ + * ! \n'
          '- Intente nuevamente.')  
