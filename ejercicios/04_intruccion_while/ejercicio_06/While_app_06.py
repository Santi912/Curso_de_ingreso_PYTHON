import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Santiago
Apellido: Decibe
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar 5 números mediante prompt. 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        titulo   = 'Ejercicio 06 - While'
        pedido   = 'Ingrese un número: '
        promedio = None
        suma     = 0
        iterable = 0

        while iterable < 5:
            numeros = prompt(titulo, pedido)
            iterable += 1
            #validación
            #si numero ingresado es None o tiene letras, pide otra vez numero
            while numeros == None or numeros.isdigit() == False:
                numeros = prompt(titulo, pedido)
            suma += int(numeros)
            

        promedio = suma / 5

        self.txt_suma_acumulada.delete(0,1000000)
        self.txt_suma_acumulada.insert(0,suma)
        self.txt_promedio.delete(0,1000000)
        self.txt_promedio.insert(0,promedio)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
