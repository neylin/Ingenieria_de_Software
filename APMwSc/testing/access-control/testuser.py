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
    
# --------------------- IMPORTACIONES --------------------- #
import unittest

import os
import sys

# Esto permite usar user.py
sys.path.append('../../business/access-control')
import user

from test.test_keyword import NONEXISTENT_FILE
from tkinter.constants import INSERT
# --------------------------------------------------------- #


class TestUser(unittest.TestCase):
    
    ''' Casos de insert'''
    
    
    def test1InsertValido(self):
        usuario = clsUser()
        resultado = usuario.insert_user("OrianaGraterol","oggs22",12345678*A," oggs22@gmail.com",11,2)
        self.assertTrue(resultado)
        
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
    
    
