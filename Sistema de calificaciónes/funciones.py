from tkinter import messagebox
from database import (
    cursor1,
    cursor2,
    conexion1,
    conexion2
)
import datetime


def calcular_promedio(c1, c2, c3):

    return round(
        (c1 + c2 + c3) / 3,
        2
    )


def registrar(
    nombre,
    c1,
    c2,
    c3,
    asistencia,
    tareas
):

    if not nombre.strip():

        messagebox.showerror(
            "ERROR",
            "Ingresa un nombre"
        )

        return False

    if not all(
        c.isalpha() or c.isspace()
        for c in nombre
    ):

        messagebox.showerror(
            "ERROR",
            "El nombre solo puede contener letras"
        )

        return False

    # VALIDACIONES

    if c1 < 0 or c1 > 10:
        raise ValueError(
            "La calificación 1 debe estar entre 0 y 10"
        )

    if c2 < 0 or c2 > 10:
        raise ValueError(
            "La calificación 2 debe estar entre 0 y 10"
        )

    if c3 < 0 or c3 > 10:
        raise ValueError(
            "La calificación 3 debe estar entre 0 y 10"
        )

    if asistencia < 0 or asistencia > 100:
        raise ValueError(
            "La asistencia debe estar entre 0 y 100"
        )

    if tareas < 1 or tareas > 10:
        raise ValueError(
            "Las tareas deben estar entre 1 y 10"
        )

    promedio = calcular_promedio(
        c1,
        c2,
        c3
    )

    fecha = datetime.datetime.now().strftime(
        "%d/%m/%Y"
    )

    cursor1.execute(
        """
        INSERT INTO alumnos(
            nombre,
            cal1,
            cal2,
            cal3,
            asistencia,
            tareas,
            promedio,
            fecha
        )
        VALUES(?,?,?,?,?,?,?,?)
        """,
        (
            nombre,
            c1,
            c2,
            c3,
            asistencia,
            tareas,
            promedio,
            fecha
        )
    )

    conexion1.commit()

    cursor2.execute(
        """
        INSERT INTO reportes(
            alumno,
            promedio,
            fecha
        )
        VALUES(?,?,?)
        """,
        (
            nombre,
            promedio,
            fecha
        )
    )

    conexion2.commit()

    return promedio


def obtener_alumnos():

    cursor1.execute(
        "SELECT * FROM alumnos"
    )

    return cursor1.fetchall()


def buscar_alumno(nombre):

    cursor1.execute(
        """
        SELECT * FROM alumnos
        WHERE nombre LIKE ?
        """,
        (f"%{nombre}%",)
    )

    return cursor1.fetchall()


def eliminar_alumno(id_alumno):

    cursor1.execute(
        """
        DELETE FROM alumnos
        WHERE id=?
        """,
        (id_alumno,)
    )

def promedio_grupo():

    cursor1.execute("""
    SELECT AVG(promedio)
    FROM alumnos
    """)

    resultado = cursor1.fetchone()[0]

    if resultado is None:
        return 0

    return round(resultado, 2)

    conexion1.commit()