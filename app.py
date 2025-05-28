from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Conexión con MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["zoologico"]

# Definir todas las colecciones
animales_collection = db["animales"]
cuidadores_collection = db["cuidadores"]
edificios_collection = db["edificios"]
empleados_collection = db["empleados"]
habitats_collection = db["habitats"]
shows_collection = db["shows"]
zonas_collection = db["zonas"]

@app.route('/animales', methods=['GET'])
def get_animales():
    animales = list(animales_collection.find({}, {"_id": 0}))
    return jsonify(animales)

@app.route('/cuidadores', methods=['GET'])
def get_cuidadores():
    cuidadores = list(cuidadores_collection.find({}, {"_id": 0}))
    return jsonify(cuidadores)

@app.route('/edificios', methods=['GET'])
def get_edificios():
    edificios = list(edificios_collection.find({}, {"_id": 0}))
    return jsonify(edificios)

@app.route('/empleados', methods=['GET'])
def get_empleados():
    empleados = list(empleados_collection.find({}, {"_id": 0}))
    return jsonify(empleados)

@app.route('/habitats', methods=['GET'])
def get_habitats():
    habitats = list(habitats_collection.find({}, {"_id": 0}))
    return jsonify(habitats)

@app.route('/shows', methods=['GET'])
def get_shows():
    shows = list(shows_collection.find({}, {"_id": 0}))
    return jsonify(shows)

@app.route('/zonas', methods=['GET'])
def get_zonas():
    zonas = list(zonas_collection.find({}, {"_id": 0}))
    return jsonify(zonas)

if __name__ == '__main__':
    app.run(debug=True, port=5001)