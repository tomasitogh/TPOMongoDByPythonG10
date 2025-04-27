from pymongo import MongoClient
import json

# 1. Conexión a MongoDB
cliente = MongoClient("mongodb://localhost:27017/")  # Cambia si tu Mongo no es local
db = cliente["zoologico"]

# 2. Cargar el JSON grande
with open('ZoologicoGrupo10.json', 'r', encoding='utf-8') as f:
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