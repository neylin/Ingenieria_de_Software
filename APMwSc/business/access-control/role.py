'''
Created on May 1, 2015

@author: Neylin Belisario
         Oriana Graterol
'''

class clsRole():
        
    def insert_role(self, idrole, namerole, user_role):
        rol = clsRole(idrole, namerole, user_role)
        db.session.add(rol)
        db.session.commit()
        
    def find_role(self):        
        rol = clsRole.query.filter_by(idrole).first()
        
    def modify_role(self,idrole):
        rol = clsRole(idrole)
        db.session.add(rol)
        db.session.commit()
        
    def delete_role(self, idrole):
        rol = clsRole(idrole)
        db.session.delete(rol)
        db.session.commit()
