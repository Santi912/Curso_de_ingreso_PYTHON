import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nombre: Santiago
Apellido: Decibe
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_divisores = 0
        numero = prompt('Ej 08 - For','Ingrese un número: ')
        numero = int(numero)
        lista = []
        
        for i in range(1,numero + 1,1):
            if numero % i == 0:
                contador_divisores += 1
                lista.append(i)
        
        for elemento in lista:
            print(i)

        alert('Ej 07 - For', f'La cantidad de divisores que tiene {numero} es {contador_divisores}.')
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()