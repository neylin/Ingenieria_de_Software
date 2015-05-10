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

class TestDpt(unittest.TestCase):
    
    ''' Casos de role'''
    
    
    def test1_dptExist(self):
        tempDpt = clsDpt()
        self.assertIsNotNone( tempDpt )
        session.query( model.Dpt ).delete()  # Se limpia la base de datos.

    
    ### CASOS VALIDOS( Casos Interiores ).
        # Test 2: Insertar un dpt que no existe.
        
    def test2_insert_dptNoExist(self):
        session.query(model.Dpt).delete()  # Se limpia la base de datos.
        tempDpt = clsDpt()
        newIdDpt = 2
        newNameDpt = 'dpt2.0'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertTrue(result)
        
        # Test 3: Insertar un dpt que ya existe.
    def test3_insert_dptExist(self):
        tempDpt = clsDpt()
        newIdDpt = 2
        newNameDpt = 'dpt2.0'
        result = tempDpt.insert_dpt( newIdDpt, newNameDpt )
        self.assertFalse(result)