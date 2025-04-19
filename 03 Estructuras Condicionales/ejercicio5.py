#Escribir un programa que permita introducir
#contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario
#ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje 
#"Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla 
#"Por favor, ingrese una contraseña de entre 8 y 14 caracteres".


ingrese_cont = input("Ingrese una contraseña entre 8 y 14 caracteres: ");
if len(ingrese_cont) >= 8 and len(ingrese_cont) <= 14:
    print("Ha ingresado una contraseña correcta");
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")