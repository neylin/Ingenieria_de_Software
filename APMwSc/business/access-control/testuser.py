# -*- coding: utf-8 -*-. 
"""
    Universidad Simon Bolivar.
    Ingenieria de Software I
    Integrantes:
        *.- Neylin Belisario. Carnet: 09-10093 
        *.- Oriana Graterol.  Carnet: 10-11248
    Equipo: SoftDev
    Trimestre Abril - Julio 2015
    """

import unittest
from user import clsUser
from test.test_keyword import NONEXISTENT_FILE
from tkinter.constants import INSERT

class TestUser(unittest.TestCase):
    
    ''' Casos de insert'''
    
    
    def test1InsertValido(self):
        user = clsUser()
        resultado = user.insert("Oriana Graterol","oggs22",12345678*A," oggs22@gmail.com",11,2)
        self.assertTrue(resultado)
        
    def test6InsertValidoFullName1(self):
        user = clsUser()
        resultado = user.insert("a","oggs22",12345678*A," oggs22@gmail.com",11,"as2")
        self.assertTrue(resultado)
    
    def test2InsertInvalidoIDdptString(self):
        user = clsUser()
        resultado = user.insert("Oriana Graterol","oggs22",12345678*A," oggs22@gmail.com","a11",2)
        self.assertFalse(resultado)
        
    def test3InsertInvalidoIDrolString(self):
        user = clsUser()
        resultado = user.insert("OrianaGraterol","oggs22",12345678*A," oggs22@gmail.com",11,"as2")
        self.assertFalse(resultado)
        
    def test4InsertInvalidoFullName51(self):
        user = clsUser()
        resultado = user.insert("qwertyuiopaOrianaGraterolGGDJDGJSsgdhsafsyw8t743yuy","oggs22",12345678*A," oggs22@gmail.com",11,"as2")
        self.assertTrue(resultado)
        
    def test5InsertInvalidoFullNameEmpty (self):
        user = clsUser()
        resultado = user.insert("","oggs22",12345678*A," oggs22@gmail.com",11,"as2")
        self.assertTrue(resultado)
    
    def test7InsertIn
        
    