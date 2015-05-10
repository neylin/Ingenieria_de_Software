# -*- coding: utf-8 -*-. 
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
import unittest

import os
import sys

# Esto permite usar user.py
sys.path.append('../../data')
import model

# --------------------------------------------------------- #


class TestRole(unittest.TestCase):
    
    ''' Casos de role'''
    
    
    def test1_roleExist(self):
        tempRole = clsRole()
        self.assertIsNotNone( tempRole )
        session.query( model.Role ).delete()
        
        
    ### CASOS VALIDOS( Casos Interiores ).
        # Test 2: Insertar un role que no existe.
        
    def test2_insert_roleNoExist(self):
        session.query(model.Role).delete()  # Se limpia la base de datos.
        tempRole = clsRole()
        newIdRole = 2
        newNameRole = 'role2.0'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertTrue(result)
        
        # Test 3: Insertar un role que ya existe.
    def test3_insert_dptExist(self):
        tempRole = clsRole()
        newIdRole = 2
        newNameRole = 'role2.0'
        result = tempRole.insert_role( newIdRole, newNameRole )
        self.assertFalse(result)
            
        
        
        
    def test2InsertInvalidoIDdptString(self):
        usuario = clsUser()
        resultado = usuario.insert_user("OrianaGraterol","oggs22",12345678*A," oggs22@gmail.com","a11",2)
        self.assertTrue(resultado)
        
    def test3InsertInvalidoIDrolString(self):
        usuario = clsUser()
        resultado = usuario.insert_user("OrianaGraterol","oggs22",12345678*A," oggs22@gmail.com",11,"as2")
        self.assertTrue(resultado)
        
    def test4InsertInvalidoFullName51(self):
        usuario = clsUser()
        resultado = usuario.insert_user("qwertyuiopaOrianaGraterolGGDJDGJSsgdhsafsyw8t743yuy","oggs22",12345678*A," oggs22@gmail.com",11,"as2")
        self.assertTrue(resultado)


