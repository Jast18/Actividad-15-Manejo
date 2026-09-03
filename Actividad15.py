#Grupo 1 Plataforma de streaming: películas, series, descripción, reparto, géneros,
#duración, clasificación y comentarios.
#Manejo e implementacion de archivo

def main():
    while True:
        print("\n---- PLATAFORMA DE STREAMING ----")
        print("1. Registrar Película")
        print("2. Registrar Serie")
        print("3. Leer todos los registros (Datos, Bytes y Posiciones)")
        print("4. Buscar registro por ID")
        print("5. Buscar Película por Nombre")
        print("6. Buscar Serie por Nombre")
        print("7. Mostrar Tamaño Total del Archivo")
        print("8. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            id = int(input("Ingrese ID de la película: "))
            tipo = input("Ingrese tipo (Película): ")
            titulo = input("Ingrese título: ")
            descripcion = input("Ingrese descripción: ")
            genero = input("Ingrese género: ")
            clasificacion = input("Ingrese clasificación: ")

            pelicula = Pelicula(id, tipo, titulo, descripcion, genero, clasificacion)
            manejo_streaming.registrar_pelicula(pelicula)
            print("Película registrada correctamente.")

        elif opcion == "2":
            id = int(input("Ingrese ID de la serie: "))
            tipo = input("Ingrese tipo (Serie): ")
            titulo = input("Ingrese título: ")
            descripcion = input("Ingrese descripción: ")
            genero = input("Ingrese género: ")
            clasificacion = input("Ingrese clasificación: ")

            serie = Serie(id, tipo, titulo, descripcion, genero, clasificacion)
            manejo_streaming.registrar_serie(serie)
            print("Serie registrada correctamente.")

        elif opcion == "3":
            manejo_streaming.leer_todos()

        elif opcion == "4":
            id_buscado = int(input("Ingrese el ID a buscar: "))
            manejo_streaming.buscar_por_id(id_buscado)


        elif opcion =="5":
            nombre_buscado = input("Ingrese el nombre de la película a buscar: ")
            manejo_streaming.buscar_pelicula_por_nombre(nombre_buscado)

        elif opcion == "6":
            nombre_buscado = input("Ingrese el nombre de la serie a buscar: ")
            manejo_streaming.buscar_serie_por_nombre(nombre_buscado)

        elif opcion == "7":
            manejo_streaming.mostrar_tamaño_total()

        elif opcion == "8":
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    main()

#ID, Tipo, titulo, Descripci+ón, genero, clasificación
class Pelicula:
    def __init__(self, id, tipo, titulo, descripcion, genero, clasificacion):
        self.id = id
        self.tipo = tipo
        self.titulo = titulo
        self.descripcion = descripcion
        self.genero = genero
        self.clasificacion = clasificacion

    def __str__(self):
        return f"ID: {self.id}\nTipo: {self.tipo}\nTitulo: {self.titulo}\nDescripcion: {self.descripcion}\nGenero: {self.genero}\nClasificacion: {self.clasificacion}"


class Serie:
    def __init__(self, id, tipo, titulo, descripcion, genero, clasificacion):
        self.id = id
        self.tipo = tipo
        self.titulo = titulo
        self.descripcion = descripcion
        self.genero = genero
        self.clasificacion = clasificacion

    def __str__(self):
        return f"ID: {self.id}\nTipo: {self.tipo}\nTitulo: {self.titulo}\nDescripcion: {self.descripcion}\nGenero: {self.genero}\nClasificacion: {self.clasificacion}"

class Manejo_Streaming:
    def __init__(self, archivo):
        self.archivo = archivo

    def registrar_pelicula(self, pelicula):
        with open(self.archivo, "ab") as archivo:
            datos = struct.pack(
                "<i20s100s20s10s",
                pelicula.id,
                pelicula.tipo.encode("utf-8"),
                pelicula.titulo.encode("utf-8"),
                pelicula.descripcion.encode("utf-8"),
                pelicula.genero.encode("utf-8"),
                pelicula.clasificación.encode("utf-8")
            )
            archivo.write(datos)

    def registrar_serie(self, serie):
        with open(self.archivo, "ab") as archivo:
            datos = struct.pack(
                "<i20s100s20s10s",
                serie.id,
                serie.tipo.encode("utf-8"),
                serie.titulo.encode("utf-8"),
                serie.descripcion.encode("utf-8"),
                serie.genero.encode("utf-8"),
                serie.clasificación.encode("utf-8")
            )
            archivo.write(datos)

    def leer_todos(self):
        with open(self.archivo, "rb") as archivo:
            while True:
                datos == arechivo.read(100) #Lee 100 bytes
                if not datos:
                    break
                print(datos)

    def buscar__por_id(self, id_buscado):
        with open(self.archivo, "rb") as archivo:
            while True:
                datos = archivo.read(100)
                if not datos:
                    break
                id = struct.unpack("<i", datos[:4] )[0]
                if id == id_buscado:
                    print(datos)
                    return

    def buscar_pelicula_por_nombre(self, nombre_buscado):
        with open(self.archivo, "rb") as archivo:
            while True:
                datos = archivo.read(100)
                if not datos:
                    break
                nombre = struct.unpack("<20s", datos[4:24])[0].decode("utf-8").strip()
                if nombre == nombre_buscado:
                    print(datos)
                    return

    def buscar_serie_por_nombre(self, nombre_buscado):
        with open(self.archivo, "rb") as archivo:
            while True:
                datos = archivo.read(100)
                if not datos:
                    break
                nombre = struct.unpack("<20s", datos[4:24])[0].decode("utf-8").strip()
                if nombre == nombre_buscado:
                    print(datos)
                    return
    
    def mostrar_tamaño_total(self):
        with open(self.archivo, "rb") as archivo:
            archivo.seek(0, 2) #Mover el puntero hasta el final del archivo
            tamaño_total = archivo.tell() #Obtener la posicion actual
            print(f"Tamaño total del archivo: {tamaño_total} bytes")





#Registrar información.
#2. Leer todos los registros.
#3. Mostrar los datos recuperados correctamente.
#4. Buscar un registro por su identificador.
#5. Mostrar la posición inicial de cada registro.
#6. Mostrar cuántos bytes ocupa cada registro.
#7. Mostrar el tamaño total del archivo.