import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Santiago
Apellido: Decibe
Al presionar el botón Mostrar repetir el mensaje “¿Desea continuar?” (utilizando el Dialog QUESTION) 
hasta que el usuario conteste que no (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        for i in range(1,912,1):
            continuar = question('Ejercicio 05 - For', '¿Desea continuar?')
            if continuar == False:
                break



        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()