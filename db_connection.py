import sqlite3
import os

def conectar_db():
    ruta = os.path.join(os.path.dirname(__file__), "contabilidad.db")
    return sqlite3.connect(ruta)
