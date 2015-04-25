# -*- coding: utf-8 -*-. 
'''
Created on 24/9/2014

@author: Jean Carlos
@modified: Neylin Belisario
           Andres Hernandez
'''
import uuid
import hashlib
import re
#from asyncio.tasks import sleep
 
class clsAccessControl(object):
    def __init__(self):
        #ohast=''
        
        self.ExpresionRegular = ('([a-z]*([A-Z][a-zA-Z0-9\@\!\.\#\$\*\+]*[0-9][a-zA-Z0-9\@\!\.\#\$\*\+]*[\@\!\.\#\$\*\+][a-zA-Z0-9\@\!\.\#\$\*\+]*))|'
                                 '([a-z]*([A-Z][a-zA-Z0-9\@\!\.\#\$\*\+]*[\@\!\.\#\$\*\+][a-zA-Z0-9\@\!\.\#\$\*\+]*[0-9][a-zA-Z0-9\@\!\.\#\$\*\+]*))|'
                                 '([a-z]*([0-9][a-zA-Z0-9\@\!\.\#\$\*\+]*[\@\!\.\#\$\*\+][a-zA-Z0-9\@\!\.\#\$\*\+]*[A-Z][a-zA-Z0-9\@\!\.\#\$\*\+]*))|'
                                 '([a-z]*([0-9][a-zA-Z0-9\@\!\.\#\$\*\+]*[A-Z][a-zA-Z0-9\@\!\.\#\$\*\+]*[\@\!\.\#\$\*\+][a-zA-Z0-9\@\!\.\#\$\*\+]*))|'
                                 '([a-z]*([\@\!\.\#\$\*\+][a-zA-Z0-9\@\!\.\#\$\*\+]*[A-Z][a-zA-Z0-9\@\!\.\#\$\*\+]*[0-9][a-zA-Z0-9\@\!\.\#\$\*\+]*))|'
                                 '([a-z]*([\@\!\.\#\$\*\+][a-zA-Z0-9\@\!\.\#\$\*\+]*[0-9][a-zA-Z0-9\@\!\.\#\$\*\+]*[A-Z][a-zA-Z0-9\@\!\.\#\$\*\+]*))'
                                )
        
    def encript(self, value):
        # Verificar la longitud del password
        oHash=""
        olength_password=self.length_password(value)
        if olength_password>=8 and olength_password<=16:
            is_expReg = re.match(self.ExpresionRegular, value)
            if (is_expReg):
                # uuid es usado para generar numeros random
                salt = uuid.uuid4().hex
                # hash
                oHash= hashlib.sha256(salt.encode() + value.encode()).hexdigest() + ':' + salt
            #else:
                #print('El Password suministrado NO ES CORRECTO. \n'
                #     'Considere que debe contener al menos: \n'
                #     '- 1 letra mayuscula y 1 minuscula \n'
                #     '- 1 numero \n'
                #     '- 1 caracter especial: @ . # $ + * ! \n')
        else:
            print('El Password debe contener entre 8 y 16 caracteres')
        return oHash   
    
    def check_password(self, oPassworkEncript, oCheckPassword):
        # Verificar la longitud del password
        olength_password=self.length_password(oCheckPassword)
        if olength_password>=8 and olength_password<=16: 
            is_expReg = re.match(self.ExpresionRegular, oCheckPassword)
            if (is_expReg):
                # uuid es usado para generar numeros random
                oPassworkEncript, salt = oPassworkEncript.split(':')
                return oPassworkEncript == hashlib.sha256(salt.encode() + oCheckPassword.encode()).hexdigest()
            #else:
                #print('El Password no corresponde con lo requerido')
        else:
            print('El Password no posee la cantidad de caracteres requerida')
            return False
    
    def length_password(self, user_password):
        # uuid es usado para generar numeros random
        return len(user_password)
        
'''
#Para encriptar un passwork  
oPassword = input('Por favor ingrese su password: ')
#Se crea un objeto tipo clsAccessControl
oAccessControl=clsAccessControl()
oPassworkEncript = oAccessControl.encript(oPassword)
if oPassworkEncript:
    print('El Password almacenado en la memoria es: ' + oPassworkEncript)

    #Para validar el passwork introducido
    oCheckPassword = input('Para verificar su password, ingreselo nuevamente: ')
    if oAccessControl.check_password(oPassworkEncript, oCheckPassword):
        print('Ha introducido el password correcto')
    else:
        print('El password es diferente')
else:
    print('El Password suministrado NO ES CORRECTO. \n'
          'Considere que debe contener al menos: \n'
          '- 1 letra mayuscula y 1 minuscula \n'
          '- 1 numero \n'
          '- 1 caracter especial: @ . # $ + * ! \n')
'''

