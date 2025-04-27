from pymongo import MongoClient

# Conexión a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["zoologico"]  # Cambia "zoologico" por el nombre de tu base de datos si es diferente
empleados_collection = db["empleados"]  # Cambia "empleados" si el nombre de la colección es diferente

# Consulta: contar cuántos empleados hay en cada cargo
resultado = empleados_collection.aggregate([
    {"$group": {"_id": "$rol", "cantidad": {"$sum": 1}}}
])

# Mostrar resultados
print("Cantidad de empleados por cargo:")
for cargo in resultado:
    print(f"Cargo: {cargo['_id']}, Cantidad: {cargo['cantidad']}")