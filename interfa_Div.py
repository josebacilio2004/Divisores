import tkinter as tk
from tkinter import messagebox

def Calcular_Divisores():
    try:
        numNat = int(entry.get())
        if numNat < 1:
            raise ValueError("El número debe ser un natural.")
        divisores = [i for i in range(1, numNat + 1) if numNat % i == 0]
        messagebox.showinfo("Divisores", f"Los divisores de {numNat} son: {divisores}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Calculadir de Divisores")

label = tk.Label(root, text = "Ingrese un número natural:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text= "Calcular Divisores", command = Calcular_Divisores)
button.pack()

root.mainloop()


