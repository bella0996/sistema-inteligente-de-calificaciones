# -------- LIBRERÍAS --------
import statistics
import random
import datetime
import time
import turtle

# -------- FUNCIONES --------q


def pedir_nombre():
    return input("\nNombre del alumno: ")

def pedir_calificaciones():
    lista = []
    for i in range(3):
        while True:
            try:
                cal = float(input(f"Calificación {i+1}: "))
                if 0 <= cal <= 10:
                    lista.append(cal)
                    break
                else:
                    print("Rango inválido (0-10)")
            except ValueError:
                print("Error, ingresa número válido")
    return lista

def pedir_asistencia():
    while True:
        try:
            a = int(input("Asistencia (0-100): "))
            if 0 <= a <= 100:
                return a
            else:
                print("Rango inválido")
        except ValueError:
            print("Error")

def pedir_tareas():
    while True:
        try:
            t = int(input("Tareas (0-10): "))
            if 0 <= t <= 10:
                return t
            else:
                print("Rango inválido")
        except ValueError:
            print("Error")

def calcular_promedio(lista):
    return sum(lista) / len(lista)

def promedio_ponderado(prom, asis, tareas):
    return round((prom * 0.6) + (asis / 10 * 0.25) + (tareas * 0.15), 2)

def evaluar(prom_final):
    if prom_final >= 6:
        return "APROBADO"
    else:
        return "REPROBADO"

def nivel_rendimiento(prom):
    if prom >= 9:
        return "Excelente"
    elif prom >= 7:
        return "Bueno"
    elif prom >= 6:
        return "Regular"
    else:
        return "Deficiente"

def mensaje():
    mensajes = ["Sigue así 💪", "Puedes mejorar 🚀", "Excelente ⭐", "No te rindas"]
    return random.choice(mensajes)

def recomendacion(prom, asis, tareas):
    if asis < 80:
        return "⚠ Mejora tu asistencia"
    elif tareas < 7:
        return "📚 Entrega más tareas"
    elif prom < 6:
        return "📖 Estudia más"
    else:
        return "🌟 Excelente desempeño"

def guardar_archivo(nombre, prom):
    with open("historial.txt", "a") as f:
        f.write(f"{nombre} - {round(prom,2)}\n")

def mostrar_datos(nombre, prom, prom_pond, estado):
    print("\n----- RESULTADOS -----")
    print("Alumno:", nombre)
    print("Promedio:", round(prom, 2))
    print("Promedio ponderado:", prom_pond)
    print("Estado:", estado)
    print("Nivel:", nivel_rendimiento(prom))
    print("Mensaje:", mensaje())

def animacion():
    print("\nProcesando", end="")
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print()

def estadisticas(lista):
    print("\n--- ESTADÍSTICAS ---")
    print("Promedio general:", round(statistics.mean(lista), 2))
    print("Mayor:", max(lista))
    print("Menor:", min(lista))

def ranking(alumnos, promedios):
    ordenados = sorted(zip(promedios, alumnos), reverse=True)
    print("\n🏆 RANKING DE ALUMNOS")
    for i, (p, n) in enumerate(ordenados, 1):
        print(f"{i}. {n} — {round(p,2)}")

# -------- SCRIPT GRÁFICO --------

def hoja_examen(nombre, promedio, estado):
    screen = turtle.Screen()
    screen.bgcolor("#0d0d0d")

    t = turtle.Turtle()
    t.speed(3)
    t.pensize(3)

    def linea(x1, y1, x2, y2):
        t.penup()
        t.goto(x1, y1)
        t.pendown()
        t.goto(x2, y2)

    # marco
    t.color("white")
    linea(-200, 200, 200, 200)
    linea(200, 200, 200, -200)
    linea(200, -200, -200, -200)
    linea(-200, -200, -200, 200)

    # título
    t.penup()
    t.goto(-120, 150)
    t.color("#cc00ff")
    t.write("HOJA DE RESULTADOS", font=("Arial", 16, "bold"))

    # datos
    t.penup()
    t.goto(-150, 100)
    t.color("white")
    t.write(f"Alumno: {nombre}", font=("Arial", 12, "bold"))

    t.goto(-150, 70)
    t.write(f"Promedio ponderado: {round(promedio,2)}", font=("Arial", 12, "bold"))

    t.goto(-150, 40)
    if estado == "APROBADO":
        t.color("#00ff99")
    else:
        t.color("red")
    t.write(f"Estado: {estado}", font=("Arial", 12, "bold"))

    # círculo
    t.penup()
    t.goto(50, 20)
    t.pendown()

    if estado == "APROBADO":
        t.color("#00ff99")
        letra = "A+"
    else:
        t.color("red")
        letra = "F"

    t.circle(50)

    t.penup()
    t.goto(65, 40)
    t.color("white")
    t.write(letra, font=("Arial", 20, "bold"))

    t.hideturtle()
    turtle.done()

# -------- ARREGLOS --------
alumnos = []
promedios = []

# -------- PROGRAMA --------
print("===== SISTEMA INTELIGENTE DE CALIFICACIONES =====")

while True:
    try:
        nombre = pedir_nombre()
        calif = pedir_calificaciones()
        asis = pedir_asistencia()
        tareas = pedir_tareas()

        animacion()

        prom = calcular_promedio(calif)
        prom_pond = promedio_ponderado(prom, asis, tareas)
        estado = evaluar(prom_pond)

        mostrar_datos(nombre, prom, prom_pond, estado)
        print("Recomendación:", recomendacion(prom, asis, tareas))

        alumnos.append(nombre)
        promedios.append(prom)

        guardar_archivo(nombre, prom)

        continuar = input("\n¿Otro alumno? (si/no): ").lower()
        if continuar != "si":
            break

    except Exception as e:
        print("Error:", e)

# estadísticas
if len(promedios) > 0:
    estadisticas(promedios)
    ranking(alumnos, promedios)

print("\nSistema finalizado:", datetime.datetime.now())

input("\nPresiona ENTER para ver la hoja de examen...")
hoja_examen(nombre, prom_pond, estado)
