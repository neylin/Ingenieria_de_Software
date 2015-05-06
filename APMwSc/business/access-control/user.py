 '''
Created on May 1, 2015

@author: Neylin Belisario
         Oriana Graterol
'''
from login import clsLogin

class clsUser(db.Model):
    __tablename__ = 'users'
    fullname = db.Column(db.String(50),primary_key=True)
    username = db.Column(db.String(16), unique=True)
    password = db.Column(db.String(16),unique=True)
    email = db.Column(db.String(30), unique=True)
    iddpt = db.Column(db.Integer,db.ForeignKey('clsdpt.iddpt'))
    idrole = db.Column(db.Integer,db.ForeignKey('clsrole.idrole'))

    def __init__(self, fullname, username, password, email, iddpt, idrole):
        '''
        Constructor
        '''
        self.fullname = fullname
        self.username = username
        self.password = password
        self.email = email
        
    def insert_user(self, fullname, username, password, email, iddpt, idrole):
        if (len(fullname)<= 50) and (len(username)<= 16) and (len(password)<= 16) and (len(email)<= 30) and isinstance(iddpt,int) and isinstance(idrole, int) :
            if ((fullname != None) && (username != None)):
                password_constructor =clsLogin()
                oPassworkEncript = password_constructor.encript(password)
                if oPassworkEncript:
                    print('El Password almacenado en la memoria es: ' + oPassworkEncript)
                
                    #Para validar el passwork introducido
                    oCheckPassword = input('Para verificar su password, ingreselo nuevamente: ')
                    if password_constructor.check_password(oPassworkEncript, oCheckPassword):
                        print('Ha introducido el password correcto')
                        usuario = clsUser(fullname,username,password_prueba,email,iddpt,idrole)
                        db.session.add(usuario)
                        db.session.commit()
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


    def find_user(self, fullname): 
        if ((len(fullname)<=50) && (fullname != None)):       
            usuario = clsUser.query.filter_by(fullname).first()
            return usuario
        return None


    def modify_user(self,fullname):
        if ((len(fullname)<=50) && (fullname != None)):
            usuario = clsUser(fullname)
            db.session.add(usuario)
            db.session.commit()
            return True
        return None
        
        
    def delete_user(self, fullname):
        if ((len(fullname)<=50) && (fullname != None)):
            usuario = clsUser(fullname)
            db.session.delete(usuario)
            db.session.commit()
            return True
        return None
        