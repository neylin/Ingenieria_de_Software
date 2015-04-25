'''
Created on Apr 23, 2015

@author: Neylin Belisario
        Andres Hernandez
'''
import unittest
from mdlaccesscontrol import clsAccessControl
#from feedparser import ACCEPT_HEADER

class Test(unittest.TestCase):
    '''
        CASO VALIDO
        Se prueba que el password sea de 8 a 16 caracteres y tenga al menos:
        - 1 letra mayuscula y 1 minuscula
        - 1 numero
        - 1 caracter especial: @ . # $ + * !
    '''
    '''
        CASOS DEL ENCRIPT
    '''  
    def testSinCaracterEspecial(self):
        acceso = clsAccessControl()
        value = "Hola1234"
        self.assertEqual(acceso.encript(value),"")
        print('FALTA el caracter especial...')

    def testSinMayuscula(self):
        acceso = clsAccessControl()
        value = "@hola1234"
        self.assertEqual(acceso.encript(value),"")
        print('FALTA la mayuscula')
        
    def testSinMinuscula(self):
        acceso = clsAccessControl()
        value = "@HOLA1234"
        self.assertNotEqual(acceso.encript(value),"")
        print('CORRECTO')
        
    def testSinNumero(self):
        acceso = clsAccessControl()
        value = "@HolaHola"
        self.assertEqual(acceso.encript(value),"")
        print('FALTA el numero')
        
    def testSinLetras(self):
        acceso = clsAccessControl()
        value = "@1234!567"
        self.assertEqual(acceso.encript(value),"")
        print('FALTAN las letras')
    
    def testSoloCaracterEspecial(self):
        acceso = clsAccessControl()
        value = "@!$.+*!$@#"
        self.assertEqual(acceso.encript(value),"")
        print('Solo hay caracteres especiales')

    def testSoloLetras(self):
        acceso = clsAccessControl()
        value = "HoLaHoLaS"
        self.assertEqual(acceso.encript(value),"")
        print('Solo hay letras')
        
    def testSoloNumero(self):
        acceso = clsAccessControl()
        value = "12345678"
        self.assertEqual(acceso.encript(value),"")
        print('Solo hay numeros')
        
    '''
        CASOS DEL CHECK_PASSWORD
    '''
    #Se prueba que los passwords son iguales  
    def testCheckPassword1(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@Hola1234") 
        oCheckPassword = "@Hola1234"
        self.assertTrue(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('Son iguales')

    #Se prueba que los password son diferentes por 1 NUMERO        
    def testCheckPassword2(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@Hola1234") 
        oCheckPassword = "@Hola1235"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por 1 numero')
    
    #Se prueba que los password son diferentes por 1 LETRA MAYUSCULA
    def testCheckPassword3(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@HolaS1234") 
        oCheckPassword = "@Hola1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por 1 letra mayuscula demas')
        
    #Se prueba que los password son diferentes por 1 LETRA MINUSCULA
    def testCheckPassword4(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@Hola1234") 
        oCheckPassword = "@Holas1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por 1 letra minuscula demas')
        
    #Se prueba que los password son diferentes por todas las letras en mayusculas
    def testCheckPassword5(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@Hola1234") 
        oCheckPassword = "@HOLA1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por todas las letras cambiadas a mayusculas')
    
    #Se prueba que los password son diferentes por todas las letras en minusculas
    def testCheckPassword6(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@HOLA1234") 
        oCheckPassword = "@Hola1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por todas las letras cambiadas a minusculas')
        
    #Se prueba que los password son diferentes por todas las letras en mayusculas
    def testCheckPassword7(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@Hola1234") 
        oCheckPassword = "@HOLA1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por todas las letras cambiadas a mayusculas')
        
    #Se prueba que los password son diferentes por todas las letras en mayusculas
    def testCheckPassword8(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@Hola1234") 
        oCheckPassword = "@HOLA1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por todas las letras cambiadas a mayusculas')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
