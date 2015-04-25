'''
Created on Apr 23, 2015

@author: Neylin Belisario
        Andres Hernandez
'''
import unittest
from mdlaccesscontrol import clsAccessControl

class Test(unittest.TestCase):
    '''
        CASOS DEL ENCRIPT
    '''  
    ''' VALIDOS '''
    def testSinMinuscula(self):
        acceso = clsAccessControl()
        value = "@HOLA1234"
        self.assertNotEqual(acceso.encript(value),"")
        print('CORRECTO')
        
    def testCombinacion(self):
        acceso = clsAccessControl()
        value = "A1.b2C#d!E"
        self.assertNotEqual(acceso.encript(value),"")
        print('CORRECTO')
        
    ''' NO VALIDOS '''
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
    ''' VALIDOS '''
    #Se prueba que los passwords son iguales  
    def testCheckPassword1(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@Hola1234") 
        oCheckPassword = "@Hola1234"
        self.assertTrue(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('CORRECTO')
        
    #Se prueba que los passwords son iguales  
    def testCheckPassword2(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript(".abd#ABC$123") 
        oCheckPassword = ".abd#ABC$123"
        self.assertTrue(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('CORRECTO')
        
    ''' NO VALIDOS '''
    #Se prueba que los password son diferentes por 1 NUMERO        
    def testCheckPassword3(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@Hola1234") 
        oCheckPassword = "@Hola1235"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por 1 numero')
    
    #Se prueba que los password son diferentes por 1 LETRA MAYUSCULA
    def testCheckPassword4(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@HolaS1234") 
        oCheckPassword = "@Hola1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por 1 letra mayuscula demas')
        
    #Se prueba que los password son diferentes por 1 LETRA MINUSCULA
    def testCheckPassword5(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@Hola1234") 
        oCheckPassword = "@Holas1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por 1 letra minuscula demas')
        
    #Se prueba que los password son diferentes por todas las letras en mayusculas
    def testCheckPassword6(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@Hola1234") 
        oCheckPassword = "@HOLA1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por todas las letras cambiadas a mayusculas')
    
    #Se prueba que los password son diferentes por todas las letras en minusculas
    def testCheckPassword7(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@HOLA1234") 
        oCheckPassword = "@Hola1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por todas las letras cambiadas a minusculas')
        
    #Se prueba que los password son diferentes por todas las letras en mayusculas
    def testCheckPassword8(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("@Hola1234") 
        oCheckPassword = "@HOLA1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales por todas las letras cambiadas a mayusculas')
        
    #Se prueba que los password son diferentes. Se le cambia el caracter especial por otro
    def testCheckPassword9(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("Hola@1234") 
        oCheckPassword = "Hola!1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales. Se cambia el caracter especial')
        
    #Se prueba que los password son diferentes. Se cambian de lugar las letras.
    def testCheckPassword10(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript("1234@Hola") 
        oCheckPassword = "Hola@1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales. Se cambian de lugar las letras.')
        
    #Se prueba que los password son diferentes. Se cambiaron las mayusculas por las minusculas.
    def testCheckPassword11(self):
        acceso = clsAccessControl()
        oPassworkEncript = acceso.encript(".AbCd.1234") 
        oCheckPassword = ".aBcD.1234"
        self.assertFalse(acceso.check_password(oPassworkEncript, oCheckPassword))
        print('No son iguales. Se cambiaron las mayusculas por las minusculas.')
        
        
    '''
        CASOS DEL LENGTH_PASSWORD
    '''
    ''' VALIDOS '''
    def testLengthPassword1(self):
        acceso = clsAccessControl()
        user_password = ".aBcD.123"
        self.assertTrue(8 <= acceso.length_password(user_password) <= 16)
        print('CORRECTO. 9')
        
    def testLengthPassword2(self):
        acceso = clsAccessControl()
        user_password = "abC#123!"
        self.assertTrue(8 <= acceso.length_password(user_password) <= 16)
        print('CORRECTO. 8')
        
    def testLengthPassword3(self):
        acceso = clsAccessControl()
        user_password = ".abC#123!.567$Ab"
        self.assertTrue(8 <= acceso.length_password(user_password) <= 16)
        print('CORRECTO. 16')
        
    def testLengthPassword4(self):
        acceso = clsAccessControl()
        user_password = ".abC#123!.567$b"
        self.assertTrue(8 <= acceso.length_password(user_password) <= 16)
        print('CORRECTO. 15')
        
        
    ''' NO VALIDOS '''
    def testLengthPassword5(self):
        acceso = clsAccessControl()
        user_password = "aBcD.12"
        self.assertFalse(8 <= acceso.length_password(user_password) <= 16)
        print('No esta en el rango. 7')
        
    def testLengthPassword6(self):
        acceso = clsAccessControl()
        user_password = "aBcD.1234@567.EfG"
        self.assertFalse(8 <= acceso.length_password(user_password) <= 16)
        print('No esta en el rango. 17')
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
