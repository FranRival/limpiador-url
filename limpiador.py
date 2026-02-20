import tkinter as tk
from tkinter import scrolledtext
import os
import re

def limpiar_rutas(texto):
    lineas = texto.strip().splitlines()
    resultado = []

    for linea in lineas:
        linea = linea.strip().replace('"', '')
        if linea:
            nombre = os.path.basename(linea)
            resultado.append(nombre)

    return "\n".join(resultado)


def limpiar_embeds(texto):
    # Extrae todas las URLs dentro de src=""
    urls = re.findall(r'src="([^"]+)"', texto)
    return "\n".join(urls)


def procesar():
    texto = entrada.get("1.0", tk.END)

    if modo.get() == "ruta":
        resultado = limpiar_rutas(texto)
    elif modo.get() == "embed":
        resultado = limpiar_embeds(texto)
    else:
        resultado = ""

    salida.delete("1.0", tk.END)
    salida.insert(tk.END, resultado)


# UI
root = tk.Tk()
root.title("Extractor PRO")

modo = tk.StringVar(value="ruta")

frame_top = tk.Frame(root)
frame_top.pack()

tk.Radiobutton(frame_top, text="Ruta", variable=modo, value="ruta").pack(side="left")
tk.Radiobutton(frame_top, text="Embed", variable=modo, value="embed").pack(side="left")

entrada = scrolledtext.ScrolledText(root, width=70, height=15)
entrada.pack()

btn = tk.Button(root, text="Procesar", command=procesar)
btn.pack()

salida = scrolledtext.ScrolledText(root, width=70, height=15)
salida.pack()

root.mainloop()