import secrets
import string
import tkinter as tk


minuscula = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
mayuscula =string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros= string.digits           # '0123456789'
simbolos = '!@#$%^&*()-_=+[]{}'

def generate_password(length=12):
    poll = minuscula + mayuscula + numeros+ simbolos
    #join concatena el conjunto de caracteres que se genera en la lista de comprensión en una sola cadena; secrets.choice(poll) elige un carácter aleatorio del conjunto de caracteres definido en poll, y esto se repite length veces para generar la contraseña completa.
    # _ significa N es decir, no necesitamos usar el valor de la variable en la lista de comprensión, solo necesitamos repetir la acción length veces.
    return ''.join(secrets.choice(poll) for _ in range(length))
    

def al_hacer_clic():
    password_var.set(generate_password())


def copiar_al_portapapeles():
    ventana.clipboard_clear()
    ventana.clipboard_append(password_var.get())


ventana = tk.Tk()
ventana.title("Generador de Contraseñas seguras 🔐")
ventana.geometry("400x200")
ventana.background = "#FFC0CB"
ventana.config(bg=ventana.background)   
password_var = tk.StringVar()
tk.Button(
    ventana,
    text="Generar Contraseña",
    background="#FFC0CB",
    relief="solid",              # tipo de borde: "flat", "solid", "raised", "sunken", "groove", "ridge"
    borderwidth=2,                # grosor del borde
    highlightbackground="#FF69B4", # color del borde cuando el botón NO tiene el foco
    highlightthickness=2,          # grosor de ese borde de "highlight"
    command=al_hacer_clic
).pack(pady=20)
tk.Entry(ventana, textvariable=password_var, width=30, justify="center").pack(pady=10)
tk.Button(ventana, text="Copiar al portapapeles", command=copiar_al_portapapeles).pack(pady=10)

ventana.mainloop()