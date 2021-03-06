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


class TestUser(unittest.TestCase):
    
    ''' Casos de insert'''
    
    
    def test1_userExist(self):
        tempUser = clsUser()
        self.assertIsNotNone( tempUser )
        session.query( model.User ).delete()
        
        
    ### CASOS VALIDOS( Casos Interiores ).
        # Test 2: Insertar un usuario que no existe.
        
    def test2_insert_dptNoExist(self):
        session.query(model.User).delete()  # Se limpia la base de datos.
        tempUser = clsUser()
        newFullname = 'Luis Perez'
        newUsername = 'luisp'
        newPassword = 'luis3p5'
        newEmail = 'luisperez@gmail.com'
        newIddpt = 'dpt2.0'
        newIdrole = 'role1.0'
        result = tempUser.insert_user( newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole )
        self.assertTrue(result)
        
        # Test 3: Insertar un usuario que ya existe.
    def test3_insert_dptExist(self):
        tempUser = clsUser()
        newFullname = 'Luis Perez'
        newUsername = 'luisp'
        newPassword = 'luis3p5'
        newEmail = 'luisperez@gmail.com'
        newIddpt = 'dpt2.0'
        newIdrole = 'role1.0'
        result = tempUser.insert_user( newFullname, newUsername, newPassword, newEmail, newIddpt, newIdrole )
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
    

