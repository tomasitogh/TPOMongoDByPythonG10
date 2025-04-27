from pymongo import MongoClient
import json

# Leer configuración desde el archivo JSON
with open("./config/config.json", "r") as config_file:
    config = json.load(config_file)

# Conexión a la base de datos MongoDB
client = MongoClient(config["mongo_uri"])
db = client[config["database"]]
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


