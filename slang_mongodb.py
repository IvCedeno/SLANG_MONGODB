import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['slang_mongodb']
col = db['palabras']

def agregarPalabra(palabra, significado):
    p = {
        "palabra": palabra,
        "significado": significado
    }
    col.insert_one(p)
    print("Palabra agregada!\n")

def editarPalabra(palabra, significado):
    query = {"palabra": palabra}
    update = {"$set": {"significado": significado}}
    col.update_one(query, update)
    print("Palabra actualizada!\n")

def eliminarPalabra(palabra):
    query = {"palabra": palabra}
    col.delete_one(query)
    print("Palabra eliminada!\n")
    
def listarPalabras():
    palabras = col.find()
    for p in palabras:
        print("- " + p['palabra'] + ": " + p['significado'])

def buscarPalabra(palabra):
    query = {"palabra": palabra}
    p = col.find_one(query)
    print("- " + p['palabra'] + ": " + p['significado'] + "\n")


while True:
    print("Seleccione una opcion:")
    print("1. Agregar nueva palabra")
    print("2. Editar palabra existente")
    print("3. Eliminar palabra existente")
    print("4. Ver listado de palabras")
    print("5. Buscar significado de palabra")
    print("6. Salir")
    opcion = int(input())

    if opcion == 1:
        print("\nAgregar nueva palabra")
        palabra = input("Nueva palabra: ")
        significado = input("Significado: ")
        agregarPalabra(palabra, significado)
    elif opcion == 2:
        print("\nEditar palabra existente")
        palabra = input("Palabra: ")
        significado = input("Nuevo significado: ")
        editarPalabra(palabra, significado)
    elif opcion == 3:
        print("\nEliminar palabra existente")
        palabra = input("Palabra: ")
        eliminarPalabra(palabra)
    elif opcion == 4:
        print("\nListado de palabras")
        listarPalabras()
        print()
    elif opcion == 5:
        print("\nBuscar significado de palabra")
        palabra = input("Palabra: ")
        buscarPalabra(palabra)
    elif opcion == 6:
        print("\nHasta la proxima!!\n")
        break
    else:
        print("\nOpcion invalida! Intente nuevamente\n")