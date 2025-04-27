from pymongo import MongoClient
import json

import json

# Leer configuración desde el archivo JSON
with open("./config/config.json", "r") as config_file:
    config = json.load(config_file)

# Conexión a la base de datos MongoDB
client = MongoClient(config["mongo_uri"])
db = client[config["database"]]

# 2. Cargar el JSON grande
with open('JSONs\ZoologicoGrupo10.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

# 3. Insertar en cada colección (eliminando el campo _id)
for coleccion, documentos in dataset.items():
    # Eliminar el campo _id de cada documento
    for doc in documentos:
        if "_id" in doc:
            del doc["_id"]
    
    print(f"Insertando en colección '{coleccion}'...")
    # Insertar los documentos sin el campo _id
    db[coleccion].insert_many(documentos)

print("✅ ¡Datos importados exitosamente!")