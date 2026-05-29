import csv
import os
from tkinter import messagebox
from database import cursor1, cursor2

def exportar_csv_alumnos():

    cursor1.execute(
        "SELECT * FROM alumnos"
    )

    datos = cursor1.fetchall()

    archivo = "Reporte_Alumnos.csv"

    with open(
        archivo,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:

        escritor = csv.writer(f)

        escritor.writerow([
            "ID",
            "Nombre",
            "C1",
            "C2",
            "C3",
            "Asistencia",
            "Tareas",
            "Promedio",
            "Fecha"
        ])

        escritor.writerows(datos)

    try:
        os.startfile(archivo)
    except:
        pass

    messagebox.showinfo(
        "CSV",
        "Archivo exportado"
    )


def exportar_csv_promedios():

    cursor2.execute(
        "SELECT * FROM reportes"
    )

    datos = cursor2.fetchall()

    archivo = "Reporte_Promedios.csv"

    with open(
        archivo,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:

        escritor = csv.writer(f)

        escritor.writerow([
            "ID",
            "Alumno",
            "Promedio",
            "Fecha"
        ])

        escritor.writerows(datos)

    try:
        os.startfile(archivo)
    except:
        pass

    messagebox.showinfo(
        "CSV",
        "Archivo exportado"
    )