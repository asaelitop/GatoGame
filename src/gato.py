import tkinter as tk

class Jugador:
    def __init__(self, nombre, ficha):
        self.nombre = nombre
        self.ficha = ficha

class Tablero:
    def __init__(self):
        self.celdas = [[" " for _ in range(3)] for _ in range(3)]

    def marcar_celda(self, fila, columna, ficha):
        if self.celdas[fila][columna] == " ":
            self.celdas[fila][columna] = ficha
            return True
        else:
            return False

class Juego:
    def __init__(self):
        self.jugador1 = Jugador("Jugador 1", "X")
        self.jugador2 = Jugador("Jugador 2", "O")
        self.tablero = Tablero()
        self.jugador_actual = self.jugador1
        self.ventana = tk.Tk()
        self.ventana.title("3 en Raya")
        self.botones = []
        self.mensaje_ganador = tk.Label(self.ventana, text="", font=("Helvetica", 10))
        self.mensaje_ganador.grid(row=3, column=0, columnspan=3)
        self.crear_interfaz()

    def crear_interfaz(self):
        for i in range(3):
            fila_botones = []
            for j in range(3):
                boton = tk.Button(self.ventana, text=" ", width=5, height=2,
                                  command=lambda row=i, col=j: self.marcar_celda_gui(row, col))
                boton.grid(row=i, column=j)
                fila_botones.append(boton)
            self.botones.append(fila_botones)

    def marcar_celda_gui(self, fila, columna):
        if self.tablero.marcar_celda(fila, columna, self.jugador_actual.ficha):
            self.botones[fila][columna].config(text=self.jugador_actual.ficha)
            if self.hay_ganador(self.jugador_actual.ficha):
                self.mensaje_ganador.config(text=f"Gana el {self.jugador_actual.nombre}")
                for fila_botones in self.botones:
                    for boton in fila_botones:
                        boton.config(state=tk.DISABLED)
            else:
                self.cambiar_jugador()
        else:
            print("La celda ya está ocupada. Intenta otra vez.")

    def cambiar_jugador(self):
        if self.jugador_actual == self.jugador1:
            self.jugador_actual = self.jugador2
        else:
            self.jugador_actual = self.jugador1

    def hay_ganador(self, ficha):
        for i in range(3):
            if all(self.tablero.celdas[i][j] == ficha for j in range(3)):
                return True
            if all(self.tablero.celdas[j][i] == ficha for j in range(3)):
                return True
        if all(self.tablero.celdas[i][i] == ficha for i in range(3)):
            return True
        if all(self.tablero.celdas[i][2-i] == ficha for i in range(3)):
            return True
        return False

    def reiniciar(self):
        """Reinicia el juego."""
        self.tablero = Tablero()
        self.jugador_actual = 0
        self.ganador = None
        print("El juego ha sido reiniciado.")

    def jugar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    juego = Juego()
    juego.jugar()
    juego.reiniciar()