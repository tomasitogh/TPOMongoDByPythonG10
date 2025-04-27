# Primero, muy importante, instalar la librería faker:
# pip install faker
# Luego, ejecutar el script para generar el dataset en formato JSON


from faker import Faker
import json
import random

fake = Faker()

# Definir cantidades
CANT_ANIMALES = 250
CANT_CUIDADORES = 50
CANT_EMPLEADOS = 100
CANT_SHOWS = 40
CANT_HABITATS = 20
CANT_EDIFICIOS = 10
CANT_ZONAS = 10

# Listas de referencia
nombres_zonas = [f"zona_{fake.word()}" for _ in range(CANT_ZONAS)]
nombres_habitats = [f"habitat_{fake.word()}" for _ in range(CANT_HABITATS)]
nombres_edificios = [f"edificio_{fake.word()}" for _ in range(CANT_EDIFICIOS)]

# Zonas
zonas = []
for nombre in nombres_zonas:
    zonas.append({
        "_id": nombre,
        "nombre": fake.word().capitalize() + " " + fake.word().capitalize(),
        "descripcion": fake.sentence()
    })

# Hábitats
habitats = []
for nombre in nombres_habitats:
    habitats.append({
        "_id": nombre,
        "nombre": fake.word().capitalize() + " de " + fake.word().capitalize(),
        "tipo": random.choice(["Semi-abierto", "Cerrado", "Acuático"]),
        "zona_id": random.choice(nombres_zonas),
        "capacidad": random.randint(3, 10)
    })

# Edificios
edificios = []
for nombre in nombres_edificios:
    edificios.append({
        "_id": nombre,
        "nombre": fake.company(),
        "tipo": random.choice(["Centro Médico", "Área de espectáculos", "Administrativo", "Tienda", "Restaurante"]),
        "zona_id": random.choice(nombres_zonas)
    })

# Empleados
empleados = []
nombres_empleados = []
for i in range(CANT_EMPLEADOS):
    empleado_id = f"empleado_{i}"
    empleados.append({
        "_id": empleado_id,
        "nombre": fake.name(),
        "rol": random.choice(["Cuidador de carnívoros", "Veterinario", "Guía de visitantes", "Especialista en aves"]),
        "zona_asignada": random.choice(nombres_zonas),
        "especialidad": random.choice(["Felinos grandes", "Aves tropicales", "Reptiles venenosos", "Mamíferos acuáticos"])
    })
    nombres_empleados.append(empleado_id)

# Cuidadores
cuidadores = []
empleados_cuidadores = random.sample(empleados, CANT_CUIDADORES)
for empleado in empleados_cuidadores:
    cuidadores.append({
        "_id": empleado["_id"],
        "empleado_id": empleado["_id"],
        "animales_asignados": [],
        "certificaciones": [fake.job(), fake.catch_phrase()]
    })

# Animales
animales = []
for i in range(CANT_ANIMALES):
    nombre_animal = fake.first_name()
    habitat_id = random.choice(nombres_habitats)
    posibles_cuidadores = [c["_id"] for c in cuidadores]
    cuidadores_ids = random.sample(posibles_cuidadores, k=random.randint(1, 2))
    animales.append({
        "nombre": nombre_animal,
        "especie": fake.word().capitalize() + " " + fake.word().capitalize(),
        "edad": random.randint(1, 20),
        "habitat_id": habitat_id,
        "cuidadores_ids": cuidadores_ids
    })
    # Asignar el animal a los cuidadores
    for cuidador in cuidadores:
        if cuidador["_id"] in cuidadores_ids:
            cuidador["animales_asignados"].append(nombre_animal)

# Shows
shows = []
for _ in range(CANT_SHOWS):
    shows.append({
        "_id": {"$oid": fake.uuid4()},
        "nombre": fake.catch_phrase(),
        "descripcion": fake.sentence(),
        "edificio_id": random.choice(nombres_edificios),
        "animales_participantes": random.sample([a["nombre"] for a in animales], k=random.randint(1, 3)),
        "empleados_responsables": random.sample(nombres_empleados, k=random.randint(1, 2)),
        "horario": f"{random.randint(10,18)}:{random.choice(['00', '30'])}"
    })

# Dataset final
dataset = {
    "animales": animales,
    "cuidadores": cuidadores,
    "habitats": habitats,
    "edificios": edificios,
    "empleados": empleados,
    "shows": shows,
    "zonas": zonas
}

# Guardar en archivo
with open('ZoologicoGrupo10.json', 'w', encoding='utf-8') as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print("¡Dataset de zoológico (~400 registros) generado exitosamente!")