import tkinter as tk
from tkinter import scrolledtext
import os

def limpiar_rutas(texto):
    lineas = texto.strip().splitlines()
    resultado = []

    for linea in lineas:
        linea = linea.strip().replace('"', '')
        if linea:
            nombre = os.path.basename(linea)
            resultado.append(nombre)

    return "\n".join(resultado)

def procesar():
    texto = entrada.get("1.0", tk.END)
    resultado = limpiar_rutas(texto)

    salida.delete("1.0", tk.END)
    salida.insert(tk.END, resultado)


root = tk.Tk()
root.title("Extractor de nombres")

entrada = scrolledtext.ScrolledText(root, width=60, height=15)
entrada.pack()

btn = tk.Button(root, text="Procesar", command=procesar)
btn.pack()

salida = scrolledtext.ScrolledText(root, width=60, height=15)
salida.pack()

root.mainloop()