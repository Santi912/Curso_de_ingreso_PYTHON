import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Santiago
Apellido: Decibe
Al presionar el botón 'SUMATORIA' se analizará el vector lista_datos a efectos de calcular 
la suma de todos los valores, la cual deberá ser informada utilizando Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="SUMATORIA", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        suma_total = 0
        for num in self.lista_datos:
            suma_total += num

        alert('Ej 05 - Listas', suma_total )
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()