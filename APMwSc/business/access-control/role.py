'''
Created on May 1, 2015

@author: neylin
'''

class clsRole(db.Model):
    idrole = db.Column(db.Integer, primary_key=True)
    namerole = db.Column(db.String(50), unique=True)
    user_role = db.relationship('clsuser', backref='clsrole', lazy='dynamic')

    def __init__(self, idrole, namerole):
        self.idrole = idrole #departamento
        self.namerole = namerole
        
    def insert_role(self):
        '''
        Constructor
        '''
        
    def find_role(self):        
        '''
        Constructor
        '''
        
    def modify_role(self):
        '''
        Constructor
        '''
        
    def delete_role(self):
        '''
        Constructor
        '''