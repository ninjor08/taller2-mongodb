from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Base de datos
db = client["petroleo_db"]

# Colección
coleccion = db["exploraciones"]

# Consulta
resultados = coleccion.find()

print("=== DATOS DE EXPLORACIONES ===")

# Mostrar resultados
for doc in resultados:
    print(doc)