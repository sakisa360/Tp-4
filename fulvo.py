class JugadorDeFutbol:
    def __init__(self, nombre, edad, posicion, equipo, pais, numero_camiseta):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.equipo = equipo
        self.pais = pais
        self.numero_camiseta = numero_camiseta
        self.goles = 0
        self.asistencias = 0
        self.tarjetas_amarillas = 0
        self.tarjetas_rojas = 0
        self.premios = []

    def actualizar_informacion(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.actualizacion_estadisticas()

    def calcular_promedio_goles(self, partidos_jugados):
        if partidos_jugados > 0:
            return self.goles / partidos_jugados
        return 0

    def es_goleador(self, umbral=20):
        return self.goles >= umbral

    def agregar_premio(self, premio):
        self.premios.append(premio)

    def eliminar_premio(self, premio):
        if premio in self.premios:
            self.premios.remove(premio)

    def actualizacion_estadisticas(self):
        print(f"Estadísticas de {self.nombre} actualizadas.")

    def mostrar_informacion(self):
        info = (f"Nombre: {self.nombre}\nEdad: {self.edad}\nPosición: {self.posicion}\n"
                f"Equipo: {self.equipo}\nPaís: {self.pais}\nNúmero de Camiseta: {self.numero_camiseta}\n"
                f"Goles: {self.goles}\nAsistencias: {self.asistencias}\n"
                f"Tarjetas Amarillas: {self.tarjetas_amarillas}\nTarjetas Rojas: {self.tarjetas_rojas}\n"
                f"Premios: {', '.join(self.premios) if self.premios else 'Ninguno'}")
        print(info)

def menu():
    jugadores = {}

    while True:
        print("\n--- Menú de Interacción ---")
        print("1. Crear un nuevo jugador de fútbol")
        print("2. Mostrar la información de un jugador existente")
        print("3. Actualizar la información de un jugador existente")
        print("4. Calcular el promedio de goles por partido de un jugador")
        print("5. Verificar si un jugador es un goleador")
        print("6. Agregar un premio o reconocimiento a un jugador")
        print("7. Eliminar un premio o reconocimiento de un jugador")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            posicion = input("Posición: ")
            equipo = input("Equipo: ")
            pais = input("País: ")
            numero_camiseta = input("Número de Camiseta: ")
            jugadores[nombre] = JugadorDeFutbol(nombre, edad, posicion, equipo, pais, numero_camiseta)

        elif opcion == '2':
            nombre = input("Nombre del jugador: ")
            if nombre in jugadores:
                jugadores[nombre].mostrar_informacion()
            else:
                print("Jugador no encontrado.")

        elif opcion == '3':
            nombre = input("Nombre del jugador: ")
            if nombre in jugadores:
                campos = ["edad", "posicion", "equipo", "pais", "numero_camiseta", "goles", "asistencias", "tarjetas_amarillas", "tarjetas_rojas"]
                cambios = {}
                for campo in campos:
                    valor = input(f"{campo.capitalize()} (dejar en blanco para no cambiar): ")
                    if valor:
                        cambios[campo] = int(valor) if campo in ["edad", "goles", "asistencias", "tarjetas_amarillas", "tarjetas_rojas"] else valor
                jugadores[nombre].actualizar_informacion(**cambios)
            else:
                print("Jugador no encontrado.")

        elif opcion == '4':
            nombre = input("Nombre del jugador: ")
            if nombre in jugadores:
                partidos_jugados = int(input("Número de partidos jugados: "))
                promedio = jugadores[nombre].calcular_promedio_goles(partidos_jugados)
                print(f"Promedio de goles por partido: {promedio:.2f}")
            else:
                print("Jugador no encontrado.")

        elif opcion == '5':
            nombre = input("Nombre del jugador: ")
            if nombre in jugadores:
                if jugadores[nombre].es_goleador():
                    print(f"{nombre} es un goleador.")
                else:
                    print(f"{nombre} no es un goleador.")
            else:
                print("Jugador no encontrado.")

        elif opcion == '6':
            nombre = input("Nombre del jugador: ")
            if nombre in jugadores:
                premio = input("Nombre del premio: ")
                jugadores[nombre].agregar_premio(premio)
            else:
                print("Jugador no encontrado.")

        elif opcion == '7':
            nombre = input("Nombre del jugador: ")
            if nombre in jugadores:
                premio = input("Nombre del premio: ")
                jugadores[nombre].eliminar_premio(premio)
            else:
                print("Jugador no encontrado.")

        elif opcion == '8':
            break

        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
