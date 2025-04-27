from pymongo import MongoClient
import json

# Leer configuración desde el archivo JSON
with open("./config/config.json", "r") as config_file:
    config = json.load(config_file)

# Conexión a la base de datos MongoDB
client = MongoClient(config["mongo_uri"])
db = client[config["database"]]
shows_collection = db["shows"]  # Cambia "shows" si el nombre de la colección es diferente

# Consulta: cantidad de shows por edificio
resultado = shows_collection.aggregate([
    {"$group": {"_id": "$edificio_id", "cantidad_shows": {"$sum": 1}}}
])

# Convertir el cursor en una lista para evitar problemas de consumo
resultado = list(resultado)

# Mostrar resultados
print("Cantidad de shows por edificio:")
for edificio in resultado:
    cantidad = edificio.get("cantidad_shows", 0)  # Manejar valores None
    print(f"Edificio: {edificio['_id']}, Cantidad de shows: {cantidad}")