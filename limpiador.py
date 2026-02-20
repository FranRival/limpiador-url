import tkinter as tk
from tkinter import scrolledtext
import os
import re
from tkinter import PhotoImage

root = tk.Tk()


import sys
import os

def ruta_recurso(rel_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, rel_path)



# Para ventana (PNG)
icono_png = PhotoImage(file=ruta_recurso("icono.png"))
root.iconphoto(True, icono_png)

# Para ejecutable (ICO)
ruta_icono = ruta_recurso("icono.ico")
try:
    root.iconbitmap(ruta_icono)
except:
    pass

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