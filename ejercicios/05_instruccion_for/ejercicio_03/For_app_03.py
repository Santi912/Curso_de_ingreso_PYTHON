import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Santiago
Apellido: Decibe
Enunciado:
Al presionar el botón Mostrar tomar del campo de texto cantidad de veces que se desea
repetir el mensaje "Hola UTN FRA" (utilizando el Dialog Alert)
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_repetir = customtkinter.CTkEntry(master=self)
        self.txt_repetir.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        i = self.txt_repetir.get()
        i = int(i)

        for i in range(1,i + 1,1):    #Nos pide ingresar la cantidad de veces que queremos que se repita, por eso, en el limite es i + 1 (es excluyente)
            alert('Ej 03 - For', i)


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()