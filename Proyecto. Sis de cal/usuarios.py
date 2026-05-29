from tkinter import messagebox
from database import cursor3, conexion3

def agregar_usuario(usuario, password):

    if not usuario or not password:

        messagebox.showerror(
            "ERROR",
            "Completa todos los campos"
        )

        return

    try:

        cursor3.execute(
            """
            INSERT INTO usuarios(
            usuario,
            password
            )
            VALUES(?,?)
            """,
            (usuario, password)
        )

        conexion3.commit()

        messagebox.showinfo(
            "ÉXITO",
            "Usuario agregado"
        )

    except:

        messagebox.showerror(
            "ERROR",
            "El usuario ya existe"
        )