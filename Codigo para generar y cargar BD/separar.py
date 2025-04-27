import json

# Cargar el JSON grande
with open('JSONs\ZoologicoGrupo10.json', 'r', encoding='utf-8') as f:
    dataset = json.load(f)

# Guardar cada colección en su propio archivo
for coleccion, documentos in dataset.items():
    with open(f'JSONs\{coleccion}.json', 'w', encoding='utf-8') as f_out:
        json.dump(documentos, f_out, ensure_ascii=False, indent=2)

print("¡Archivos separados por colección!")