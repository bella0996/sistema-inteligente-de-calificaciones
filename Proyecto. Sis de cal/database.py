import sqlite3

# =========================
# CONEXIONES
# =========================

conexion1 = sqlite3.connect("alumnos.db")
cursor1 = conexion1.cursor()

conexion2 = sqlite3.connect("reportes.db")
cursor2 = conexion2.cursor()

conexion3 = sqlite3.connect("usuarios.db")
cursor3 = conexion3.cursor()

# =========================
# TABLA ALUMNOS
# =========================

cursor1.execute("""
CREATE TABLE IF NOT EXISTS alumnos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    cal1 REAL,
    cal2 REAL,
    cal3 REAL,
    asistencia INTEGER,
    tareas INTEGER,
    promedio REAL,
    fecha TEXT
)
""")

# =========================
# TABLA REPORTES
# =========================

cursor2.execute("""
CREATE TABLE IF NOT EXISTS reportes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    alumno TEXT,
    promedio REAL,
    fecha TEXT
)
""")

# =========================
# TABLA USUARIOS
# =========================

cursor3.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE,
    password TEXT
)
""")

cursor3.execute("""
INSERT OR IGNORE INTO usuarios
(id,usuario,password)
VALUES
(1,'admin','1234')
""")

conexion1.commit()
conexion2.commit()
conexion3.commit()