'''
Created on May 1, 2015

@author: neylin
'''

class clsDpt(object):
    iddpt = db.Column(db.Integer, primary_key=True)
    namedpt = db.Column(db.String(50), unique=True)
    user_dpt = db.relationship('clsuser', backref='clsdpt', lazy='dynamic')

    def __init__(self, iddpt, namedpt):
        self.iddpt = iddpt #departamento
        self.namedpt = namedpt
        
    def insert_dpt(self):
        '''
        Constructor
        '''
        
    def find_dpt(self):        
        '''
        Constructor
        '''
        
    def modify_dpt(self):
        '''
        Constructor
        '''
        
    def delete_dpt(self):
        '''
        Constructor
        '''