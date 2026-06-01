import tkinter as tk
from PIL import Image, ImageTk


def mostrar_bienvenida(callback):

    ventana = tk.Tk()

    ventana.title("Bienvenido")

    ventana.geometry("700x500")

    ventana.config(bg="white")

    ventana.resizable(False, False)

    imagen = Image.open("Logo.jpeg")
    imagen = imagen.resize((350, 350))

    logo = ImageTk.PhotoImage(imagen)

    lbl_logo = tk.Label(
        ventana,
        image=logo,
        bg="white"
    )

    lbl_logo.image = logo

    lbl_logo.pack(pady=20)

    tk.Label(
        ventana,
        text="BIENVENIDO AL SISTEMA",
        bg="white",
        fg="#1e3a8a",
        font=("Segoe UI", 20, "bold")
    ).pack()

    tk.Label(
        ventana,
        text="Cargando...",
        bg="white",
        fg="gray",
        font=("Segoe UI", 12)
    ).pack(pady=10)

    def continuar():

        ventana.destroy()

        callback()

    ventana.after(
        3000,
        continuar
    )

    ventana.mainloop()