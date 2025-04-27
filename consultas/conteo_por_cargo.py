from pymongo import MongoClient

import json

# Leer configuración desde el archivo JSON
with open("./config/config.json", "r") as config_file:
    config = json.load(config_file)

# Conexión a la base de datos MongoDB
client = MongoClient(config["mongo_uri"])
db = client[config["database"]]
empleados_collection = db["empleados"]  # Cambia "empleados" si el nombre de la colección es diferente

# Consulta: contar cuántos empleados hay en cada cargo
resultado = empleados_collection.aggregate([
    {"$group": {"_id": "$rol", "cantidad": {"$sum": 1}}}
])

# Mostrar resultados
print("Cantidad de empleados por cargo:")
for cargo in resultado:
    print(f"Cargo: {cargo['_id']}, Cantidad: {cargo['cantidad']}")