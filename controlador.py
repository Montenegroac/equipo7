import sqlite3


def validar_usuario(usuario, password):
    conexion = sqlite3.connect("basededatos.s3db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuario where email = '"+usuario+"' and password = '"+password+"'")
    resultado = cursor.fetchall()
    return resultado