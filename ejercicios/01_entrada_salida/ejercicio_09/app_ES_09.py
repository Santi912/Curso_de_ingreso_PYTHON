import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Decibe
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón  'Calcular', se deberán obtener los valores contenidos en las cajas de texto (txtSueldo y txtIncremento), 
transformarlos en números y mostrar el importe de sueldo actualizado con el incremento porcentual utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="% de Incremento")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_incremento = customtkinter.CTkEntry(master=self)
        self.txt_incremento.grid(row=1, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        sueldo     = float(self.txt_sueldo.get())
        incremento = float(self.txt_incremento.get())
        sueldo_actualizado = sueldo * (incremento / 100 + 1)  # De esta manera sacamos un incremento sin la posibilidad de poner sueldo * 1."porcentaje de incremento".
                                            #Para informarle al usuario cuanto le descontamos/recargamos sobre el precio final, deberiamos poner la regla de 3 simples en una variable.
        
        alert(title="Ejercicio 09",message=f'El sueldo actualizado es {round(sueldo_actualizado,2)}')
                                             #También podemos utilizar .format() al final del string, poniendo entre llaves desde el 0 en adelante, dependiendo la cantidad de variables usadas.
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()