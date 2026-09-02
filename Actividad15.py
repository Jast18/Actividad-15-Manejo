#Grupo 1 Plataforma de streaming: películas, series, descripción, reparto, géneros,
#duración, clasificación y comentarios.
#Manejo e implementacion de archivo

def main():
    while True:
        print("----Plataforma de Streaming ----")
        print("1. Registrar Pelicula")
        print("2. Registrar Serie")
        print("3. Mostrar Peliculas")
        print("4. Mostrar Series")
        print("5. Buscar Pelicula por nombre")
        print("6. Buscar serie por nombre")
        print("7. Salir ...")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            RegistrarPelicula()
            pass
        elif opcion == "2":
            registrarSerie()
            pass
        elif opcion == "3":
            MostrarPelicula()
            pass
        elif opcion == "4":
            MostrarSerie()
            pass
        elif opcion == "5":
            BuscarPeli_Nombre()
            pass
        elif opcion == "6":
            BuscarSerie_Nombre()
            pass
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción invalida")

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

