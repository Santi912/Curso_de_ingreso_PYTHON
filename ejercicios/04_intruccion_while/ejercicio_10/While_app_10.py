import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Santiago
Apellido: Decibe
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los positivos
    La suma acumulada de los negativos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        titulo = 'Ejercicio 10 - While'
        pedido = 'Ingrese un número: '
        cantidad_ceros       = 0
        acumulador_positivos = 0
        acumulador_negativos = 0
        contador_positivos   = 0
        contador_negativos   = 0
        diferencia_cantidad  = 0

        while True:
            numero = prompt(titulo, pedido)
            
            if numero == None:
                break
            numero = int(numero)

            if numero > 0:
                acumulador_positivos += numero
                contador_positivos   += 1
            elif numero < 0:
                acumulador_negativos += numero
                contador_negativos   += 1
            else:
                cantidad_ceros += 1

        diferencia_cantidad = contador_positivos - contador_negativos

        alert('Ej 10 - While', f'''Suma positivos: {acumulador_positivos}.\nSuma negativos: {acumulador_negativos}.\n
                Cantidad de positivos ingresados: {contador_positivos}.\nCantidad de negativos ingresados: {contador_negativos}\n
                Cantidad de ceros: {cantidad_ceros}.\nDiferencia entre la cantidad de positivos y negativos: {diferencia_cantidad}.''')

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
