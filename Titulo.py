# SEMANA 06
# Jorge ALberto Bravo Veintemilla
# Importamos la libreria

import camelcase

nombre = "jorge alberto bravo veintemilla"

print(nombre.upper())
print(nombre.title())


#Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con camelcase....")

# imprimimos el nombre en formato título
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'flor' y 'león' 
cam2 = camelcase.CamelCase('jorge','bravo')
print(cam2.hump(nombre))



