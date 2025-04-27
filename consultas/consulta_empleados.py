from pymongo import MongoClient

# Conexión a la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["zoologico"]  # Cambia "zoologico" por el nombre de tu base de datos si es diferente
empleados_collection = db["empleados"]  # Cambia "empleados" si el nombre de la colección es diferente

# Consulta: empleados mayores de 30 años con salario superior a 7000
resultado = empleados_collection.find({
    "edad": {"$gt": 30},
    "salario": {"$gt": 7000}
})

# Mostrar resultados
print("Empleados mayores de 30 años con salario superior a 7000:")
for empleado in resultado:
    print(f"Nombre: {empleado['nombre']}, Edad: {empleado['edad']}, Salario: {empleado['salario']}")


