# Tarea semana 15 - Estudiante
# Tema: Trabajando con Diccionarios en Python

# Paso 1: Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Carolina Elizabeth Balcázar Pardo",
    "edad": 33,
    "ciudad": "Camilo Ponce Enríquez"
}

print("Paso 1: Diccionario inicial")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

# Paso 2a: Acceder y modificar el valor de la clave 'ciudad'
ciudad_actual = informacion_personal["ciudad"]
informacion_personal["ciudad"] = "Machala"

print("\nPaso 2a: Ciudad modificada")
print(f"Ciudad anterior: {ciudad_actual}")
print(f"Ciudad nueva: {informacion_personal['ciudad']}")

# Paso 2b: Agregar nueva clave 'profesión'
informacion_personal["profesión"] = "Auxiliar en farmacia"

print("\nPaso 2b: Se agregó la clave 'profesión'")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

# Paso 3: Verificar si existe la clave 'telefono'
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0990001122"  # Número ficticio

print("\nPaso 3: Verificación de 'telefono'")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

# Paso 4: Eliminar la clave 'edad'
informacion_personal.pop("edad")

print("\nPaso 4: Se eliminó la clave 'edad'")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")

# Paso 5: Imprimir el diccionario final
print("\nPaso 5: Diccionario final")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")