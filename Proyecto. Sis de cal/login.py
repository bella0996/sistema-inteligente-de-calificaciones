import tkinter as tk
from tkinter import messagebox

from database import cursor3
from interfaz import abrir_sistema


def entrar(login, usuario, password):

    cursor3.execute(
        """
        SELECT *
        FROM usuarios
        WHERE usuario=? AND password=?
        """,
        (
            usuario,
            password
        )
    )

    datos = cursor3.fetchone()

    if datos:

        login.destroy()

        abrir_sistema()

    else:

        messagebox.showerror(
            "ERROR",
            "Usuario o contraseña incorrectos"
        )


def iniciar_login():

    login = tk.Tk()

    login.title(
        "Inicio de Sesión"
    )

    login.geometry("500x350")

    login.config(bg="#0f172a")

    card = tk.Frame(
        login,
        bg="#111827",
        width=320,
        height=240
    )

    card.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    tk.Label(
        card,
        text="INICIAR SESIÓN",
        bg="#111827",
        fg="white",
        font=("Segoe UI", 16, "bold")
    ).pack(pady=20)

    tk.Label(
        card,
        text="Usuario",
        bg="#111827",
        fg="white"
    ).pack(anchor="w", padx=25)

    entry_usuario = tk.Entry(card)

    entry_usuario.pack(
        padx=25,
        pady=5,
        fill="x"
    )

    tk.Label(
        card,
        text="Contraseña",
        bg="#111827",
        fg="white"
    ).pack(anchor="w", padx=25)

    entry_password = tk.Entry(
        card,
        show="*"
    )

    entry_password.pack(
        padx=25,
        pady=5,
        fill="x"
    )

    tk.Button(
        card,
        text="INGRESAR",
        bg="#7c3aed",
        fg="white",
        command=lambda:
        entrar(
            login,
            entry_usuario.get(),
            entry_password.get()
        )
    ).pack(
        padx=25,
        pady=20,
        fill="x"
    )

    login.mainloop()