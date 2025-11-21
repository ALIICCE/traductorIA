"""
Algoritmo que analiza el texto insertado por el usuario,
para determinar la relevancia de un texto en un tema en concreto.
En mi caso Contabilidad
"""

import re
from functools import lru_cache
import nltk
from nltk.corpus import stopwords
from rapidfuzz import fuzz, process
from db_connection import conectar_db

try:
    _ = stopwords.words('spanish')
except (LookupError, OSError):
    nltk.download('stopwords', quiet=True)

STOP_WORDS = set(stopwords.words('spanish'))

@lru_cache(maxsize=1)
def obtener_diccionario_palabras():
    """
    Carga las palabras de la base de datos.
    """
    conn = conectar_db()
    if not conn:
        return {}, []

    cur = conn.cursor()
    cur.execute("SELECT palabra, porcentaje_identidad, sinonimos FROM palabras_contabilidad;")
    datos = cur.fetchall()
    conn.close()

    exact_map = {}

    for palabra, porcentaje, sinonimos in datos:
        porcentaje = float(porcentaje)
        palabra_clean = palabra.lower().strip()

        exact_map[palabra_clean] = (porcentaje, 1.0)

        if sinonimos:
            for sin in sinonimos.split(","):
                s_clean = sin.strip().lower()
                if s_clean and s_clean not in exact_map:
                    exact_map[s_clean] = (porcentaje, 0.9)

    fuzzy_candidates = list(exact_map.keys())
    return exact_map, fuzzy_candidates

def limpiar_texto(texto_entrada):
    """
    Normaliza el texto, es decir, convierte todo a minusculas, elimina acentos y stopwords.
    """
    if not texto_entrada:
        return []

    texto_entrada = texto_entrada.lower()
    texto_entrada = re.sub(r"[^a-záéíóúüñ\s]", "", texto_entrada)

    palabras = texto_entrada.split()
    return [p for p in palabras if p not in STOP_WORDS and len(p) > 3]

def clasificar_texto(texto_analizar, umbral_similitud=80):
    """
    Analiza el texto y calcula el porcentaje de coincidencia con el tema Contabilidad.
    """
    exact_map, fuzzy_candidates = obtener_diccionario_palabras()

    if not exact_map:
        return {"error": "Error DB"}

    palabras_texto = limpiar_texto(texto_analizar)
    total_palabras = len(palabras_texto)

    if total_palabras == 0:
        return {"tema": "Desconocido", "coincidencia": 0, "detalles": []}

    score_acumulado = 0
    palabras_encontradas = []

    for palabra_input in palabras_texto:
        match_info = None
        match_word = ""

        if palabra_input in exact_map:
            match_info = exact_map[palabra_input]
            match_word = palabra_input
        else:
            resultado = process.extractOne(
                palabra_input,
                fuzzy_candidates,
                scorer=fuzz.WRatio,
                score_cutoff=umbral_similitud
            )

            if resultado:
                match_word = resultado[0]
                match_info = exact_map[match_word]

        if match_info:
            peso_base, multiplicador = match_info
            score_acumulado += peso_base * multiplicador
            palabras_encontradas.append({
                "original": palabra_input,
                "match_db": match_word
            })

    cant_encontradas = len(palabras_encontradas)

    if cant_encontradas == 0:
        return {"tema": "Desconocido", "coincidencia": 0}

    promedio_calidad = score_acumulado / cant_encontradas

    densidad = cant_encontradas / total_palabras

    factor_relevancia = min(densidad * 3.0, 1.0)

    porcentaje_final = round(promedio_calidad * factor_relevancia, 2)

    return {
        "tema": "Contabilidad",
        "coincidencia": porcentaje_final,
        "densidad_detectada": round(densidad * 100, 1),
        "palabras_clave_encontradas": cant_encontradas,
        "total_palabras_analizadas": total_palabras,
        "detalles": palabras_encontradas
    }

if __name__ == "__main__":
    print("Analizando texto...\n")
