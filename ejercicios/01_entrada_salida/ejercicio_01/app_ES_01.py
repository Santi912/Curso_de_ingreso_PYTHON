import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Santiago
apellido: Decibe
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        #Agregué una línea
        alert(title='Ejercicio 01', message='Esto no anda, funciona')  #Sin los atributos, por defecto primero se pone el titulo y despues message.
                                                         #Con los atributos, podemos escribirlos en cualquier orden.

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
