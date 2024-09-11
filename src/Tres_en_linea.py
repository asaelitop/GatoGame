import tkinter as tk
from tkinter import messagebox

class Tres_en_linea:
    def __init__(self, master):
        self.master = master
        self.master.title("Tres en Línea")
        self.master.geometry("400x450")
        self.master.configure(bg='#263238')

        self.player = "X"
        self.game_over = False # Estado del juego

        # Crea un marco para contener los botones del tablero
        self.frame = tk.Frame(master, bg='#263238') 
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        self.buttons = [[tk.Button(self.frame, text='', font='normal 20 bold', width=5, height=2, bg='#263238', fg='white',
                                    command=lambda row=row, col=col: self.boton_click(row, col))
                         for col in range(3)] for row in range(3)]

        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col, padx=10, pady=10)

        self.reset_button = tk.Button(master, text='Reiniciar', font='normal 15 bold', command=self.reset_game, bg='#546E7A', fg='white')
        self.reset_button.place(relx=0.5, rely=0.9, anchor='center')# Coloca el botón en la parte inferior

    def verificar_ganador(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != '':  #Verifica si hay un ganador por filas
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != '':  #Verifica si hay un ganador por columnas 
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':   #Verifiva si hay un ganador en diagonal primaria
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':  #Verifica si hay un ganador en diagonal secundaria
            return True
        return False

    def boton_click(self, row, col): # Método que se ejecuta al hacer clic en un botón
        if self.buttons[row][col]['text'] == '' and not self.game_over: # Si el botón está vacío y el juego no ha terminado
            self.buttons[row][col]['text'] = self.player # Asigna el símbolo del jugador al botón
            self.buttons[row][col]['bg'] = '#37474F' if self.player == 'X' else '#455A64' # Cambia el color de fondo
            if self.verificar_ganador():
                messagebox.showinfo("3 en Línea", f"¡Jugador {self.player} gana!")
                self.game_over = True
            elif all(self.buttons[r][c]['text'] != '' for r in range(3) for c in range(3)):
                messagebox.showinfo("3 en Línea", "¡Es un empate!")
                self.game_over = True
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def reset_game(self):
        self.player = 'X' # Restablece el jugador a 'X'
        self.game_over = False
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]['text'] = ''# Limpia el texto de los botones
                self.buttons[row][col]['bg'] = '#263238'


if __name__ == "__main__":
    root = tk.Tk()
    game = Tres_en_linea(root)
    root.mainloop()