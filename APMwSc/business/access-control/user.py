  '''
Created on May 1, 2015

@author: neylin
'''

class clsUser(db.Model):
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
        usuario = clsUser(fullname, username, password, email, iddpt, idrole)
        db.session.add(usuario)
        db.session.commit()
        
    def find_user(self, fullname):        
        usuario = clsUser.query.filter_by(fullname).first()
        
    def modify_user(self):
        pass
        #db.session.modify()
        
    def delete_user(self, fullname):
        usuario = clsUser(fullname)
        db.session.delete(usuario)
        db.session.commit()
        