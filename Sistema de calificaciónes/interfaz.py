import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from funciones import (
    registrar,
    obtener_alumnos,
    buscar_alumno,
    eliminar_alumno,
    promedio_grupo
)

from exportaciones import (
    exportar_csv_alumnos,
    exportar_csv_promedios
)

from usuarios import agregar_usuario

tabla = None
ventana = None

entry_nombre = None
entry_c1 = None
entry_c2 = None
entry_c3 = None
entry_asistencia = None
entry_tareas = None

resultado = None

def mostrar_datos(datos=None):

    tabla.delete(*tabla.get_children())

    if datos is None:
        datos = obtener_alumnos()

    for fila in datos:

        promedio = fila[7]

        color = (
            "aprobado"
            if promedio >= 6
            else "reprobado"
        )

        tabla.insert(
            "",
            tk.END,
            values=fila,
            tags=(color,)
        )

def limpiar():

    entry_nombre.delete(0, tk.END)

    entry_c1.delete(0, tk.END)
    entry_c2.delete(0, tk.END)
    entry_c3.delete(0, tk.END)

    entry_asistencia.delete(0, tk.END)
    entry_tareas.delete(0, tk.END)

def registrar_gui():

    try:

        promedio = registrar(
            entry_nombre.get(),
            float(entry_c1.get()),
            float(entry_c2.get()),
            float(entry_c3.get()),
            int(entry_asistencia.get()),
            int(entry_tareas.get())
        )

        mostrar_datos()

        limpiar()

        resultado.config(
            text=f"Promedio: {promedio}"
        )

        messagebox.showinfo(
            "Éxito",
            "Alumno registrado"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

def buscar_gui():

    nombre = entry_nombre.get()

    datos = buscar_alumno(nombre)

    mostrar_datos(datos)

def eliminar_gui():

    seleccionado = tabla.selection()

    if not seleccionado:

        messagebox.showwarning(
            "Aviso",
            "Selecciona un alumno"
        )

        return

    item = tabla.item(seleccionado)

    id_alumno = item["values"][0]

    eliminar_alumno(id_alumno)

    mostrar_datos()

def mostrar_promedio_grupo():

    promedio = promedio_grupo()

    messagebox.showinfo(
        "Promedio General",
        f"Promedio del grupo: {promedio}"
    )

def ventana_usuario():

    ventana = tk.Toplevel()

    ventana.title(
        "Agregar Usuario"
    )

    ventana.geometry("300x200")

    tk.Label(
        ventana,
        text="Usuario"
    ).pack(pady=5)

    usuario = tk.Entry(ventana)
    usuario.pack()

    tk.Label(
        ventana,
        text="Contraseña"
    ).pack(pady=5)

    password = tk.Entry(
        ventana,
        show="*"
    )

    password.pack()

    tk.Button(
        ventana,
        text="Guardar",
        command=lambda:
        agregar_usuario(
            usuario.get(),
            password.get()
        )
    ).pack(pady=20)

def abrir_sistema():

    global ventana

    global tabla

    global entry_nombre
    global entry_c1
    global entry_c2
    global entry_c3
    global entry_asistencia
    global entry_tareas

    global resultado

    ventana = tk.Tk()

    ventana.title(
        "Sistema Avanzado de Calificaciones"
    )

    ventana.geometry(
        "1000x560"
    )

    ventana.config(
        bg="#0f172a"
    )

    style = ttk.Style()

    style.theme_use("clam")

    style.configure(
        "Treeview",
        background="#1e293b",
        foreground="white",
        rowheight=24,
        fieldbackground="#1e293b"
    )

    style.configure(
        "Treeview.Heading",
        background="#7c3aed",
        foreground="white"
    )

    header = tk.Frame(
        ventana,
        bg="#111827",
        height=60
    )

    header.pack(
        fill="x"
    )

    tk.Label(
        header,
        text="SISTEMA AVANZADO DE CALIFICACIONES",
        bg="#111827",
        fg="white",
        font=("Segoe UI", 16, "bold")
    ).place(
        x=20,
        y=16
    )

    panel = tk.Frame(
        ventana,
        bg="#1e293b",
        width=280
    )

    panel.pack(
        side="left",
        fill="y",
        padx=12,
        pady=12
    )

    tk.Label(
        panel,
        text="Nombre",
        bg="#1e293b",
        fg="white"
    ).pack(anchor="w", padx=15)

    entry_nombre = tk.Entry(panel)
    entry_nombre.pack(
        padx=15,
        pady=5,
        fill="x"
    )

    tk.Label(panel,text="Calificación 1 (0-10)",
             bg="#1e293b",fg="white").pack(anchor="w",padx=15)

    entry_c1 = tk.Entry(panel)
    entry_c1.pack(padx=15,pady=5,fill="x")

    tk.Label(panel,text="Calificación 2 (1-10)",
             bg="#1e293b",fg="white").pack(anchor="w",padx=15)

    entry_c2 = tk.Entry(panel)
    entry_c2.pack(padx=15,pady=5,fill="x")

    tk.Label(panel,text="Calificación 3 (1-10)",
             bg="#1e293b",fg="white").pack(anchor="w",padx=15)

    entry_c3 = tk.Entry(panel)
    entry_c3.pack(padx=15,pady=5,fill="x")

    tk.Label(panel,text="Asistencia (1-100)",
             bg="#1e293b",fg="white").pack(anchor="w",padx=15)

    entry_asistencia = tk.Entry(panel)
    entry_asistencia.pack(padx=15,pady=5,fill="x")

    tk.Label(panel,text="Tareas (1-10)",
             bg="#1e293b",fg="white").pack(anchor="w",padx=15)

    entry_tareas = tk.Entry(panel)
    entry_tareas.pack(padx=15,pady=5,fill="x")
    
    tk.Button(
        panel,
        text="REGISTRAR",
        command=registrar_gui,
        bg="#22c55e",
        fg="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat"
    ).pack(
        padx=15,
        pady=5,
        fill="x",
        ipady=6
    )

    tk.Button(
        panel,
        text="BUSCAR",
        command=buscar_gui,
        bg="#3b82f6",
        fg="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat"
    ).pack(
        padx=15,
        pady=5,
        fill="x",
        ipady=6
    )

    tk.Button(
        panel,
        text="ELIMINAR",
        command=eliminar_gui,
        bg="#ef4444",
        fg="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat"
    ).pack(
        padx=15,
        pady=5,
        fill="x",
        ipady=6
    )

    tk.Button(
        panel,
        text="AGREGAR USUARIO",
        command=ventana_usuario,
        bg="#8b5cf6",
        fg="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat"
    ).pack(
        padx=15,
        pady=5,
        fill="x",
        ipady=6
    )

    tk.Button(
        panel,
        text="CSV ALUMNOS",
        command=exportar_csv_alumnos,
        bg="#06b6d4",
        fg="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat"
    ).pack(
        padx=15,
        pady=5,
        fill="x",
        ipady=6
    )

    tk.Button(
        panel,
        text="CSV PROMEDIOS",
        command=exportar_csv_promedios,
        bg="#14b8a6",
        fg="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat"
    ).pack(
        padx=15,
        pady=5,
        fill="x",
        ipady=6
    )

    tk.Button(
        panel,
        text="PROMEDIO GRUPO",
        command=mostrar_promedio_grupo,
        bg="#f59e0b",
        fg="white",
        font=("Segoe UI", 9, "bold"),
        relief="flat"
    ).pack(
        padx=15,
        pady=5,
        fill="x",
        ipady=6
    )

    resultado = tk.Label(
        panel,
        text="",
        bg="#1e293b",
        fg="white"
    )

    resultado.pack(
        pady=10
    )

    frame_tabla = tk.Frame(
        ventana
    )

    frame_tabla.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    columnas = (
        "ID",
        "Nombre",
        "C1",
        "C2",
        "C3",
        "Asistencia",
        "Tareas",
        "Promedio",
        "Fecha"
    )

    tabla = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings"
    )

    for col in columnas:

        tabla.heading(
            col,
            text=col
        )

        tabla.column(
            col,
            width=90,
            anchor="center"
        )

    tabla.tag_configure(
        "aprobado",
        foreground="#22c55e"
    )

    tabla.tag_configure(
        "reprobado",
        foreground="#ef4444"
    )

    tabla.pack(
        fill="both",
        expand=True
    )

    mostrar_datos()

    ventana.mainloop()