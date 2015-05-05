'''
Created on May 1, 2015

@author: neylin
'''

class clsDpt(db.Model):
    iddpt = db.Column(db.Integer, primary_key=True)
    namedpt = db.Column(db.String(50), unique=True)
    user_dpt = db.relationship('clsuser', backref='clsdpt', lazy='dynamic')

    def __init__(self, iddpt, namedpt):
        '''
        Constructor
        '''
        self.iddpt = iddpt
        self.namedpt = namedpt
        
    def insert_dpt(self, iddpt, namedpt, user_dpt):
        dpto = clsDpt(iddpt, namedpt, user_dpt)
        db.session.add(dpto)
        db.session.commit()
        
    def find_dpt(self, iddpt):        
        dpto = clsDpt.query.filter_by(iddpt).first()
        
    def modify_dpt(self):
        pass
        
    def delete_dpt(self, iddpt):
        dpto = clsDpt(iddpt)
        db.session.delete(dpto)
        db.session.commit()