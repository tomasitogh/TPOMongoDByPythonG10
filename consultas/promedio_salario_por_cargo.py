from pymongo import MongoClient

# Conexión a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["zoologico"]  # Cambia "zoologico" por el nombre de tu base de datos si es diferente
empleados_collection = db["empleados"]  # Cambia "empleados" si el nombre de la colección es diferente

# Consulta: obtener el promedio de salario por cargo
resultado = empleados_collection.aggregate([
    {"$group": {"_id": "$rol", "promedio_salario": {"$avg": "$salario"}}}
])

# Mostrar resultados
print("Promedio de salario por cargo:")
for cargo in resultado:
    print(f"Cargo: {cargo['_id']}, Promedio de salario: {cargo['promedio_salario']:.2f}")