from pymongo import MongoClient

import json

# Leer configuración desde el archivo JSON
with open("./config/config.json", "r") as config_file:
    config = json.load(config_file)

# Conexión a la base de datos MongoDB
client = MongoClient(config["mongo_uri"])
db = client[config["database"]]
empleados_collection = db["empleados"]  # Cambia "empleados" si el nombre de la colección es diferente

# Consulta: obtener el promedio de salario por cargo
resultado = empleados_collection.aggregate([
    {"$group": {"_id": "$rol", "promedio_salario": {"$avg": "$salario"}}}
])

# Convertir el cursor en una lista para evitar problemas de consumo
resultado = list(resultado)

# Mostrar resultados
print("Promedio de salario por cargo:")
for cargo in resultado:
    promedio = cargo.get("promedio_salario")
    if promedio != None:
        print(f"Cargo: {cargo['_id']}, Promedio de salario: {promedio:.2f}")
    else:
        print(f"Cargo: {cargo['_id']}, No hay datos de salario disponibles")