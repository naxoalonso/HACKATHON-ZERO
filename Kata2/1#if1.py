password = "contrasena"

password_del_usuario = input("Introduzca la contraseña")
password_del_usuario = password_del_usuario.lower()

if password == password_del_usuario:
    print("El password es correcta")
else:
    print("El password no es correcta")