# Trabajo con Archivos de Texto en Python
# Autora: Carolina Elizabeth Balcázar Pardo

# 1. Escritura de archivo
with open('my_notes.txt', 'w') as file:
    file.write("Cada día puede dejar una enseñanza útil.\n")
    file.write("Es importante expresar ideas con claridad.\n")
    file.write("Compartir lo aprendido ayuda a mejorar.\n")

# 2. Lectura de archivo
with open('my_notes.txt', 'r') as file:
    print(" Contenido del archivo 'my_notes.txt':")
    linea = file.readline()
    while linea:
        print(linea.strip())
        linea = file.readline()

# 3. Cierre automático
# El uso de 'with' garantiza el cierre seguro del archivo.
