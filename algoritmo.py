import re
import nltk
from rapidfuzz import fuzz, process
from functools import lru_cache
from db_connection import conectar_db
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)



# ====== PALABRAS DE LA BASE DE DATOS ======
@lru_cache(maxsize=1)
def obtener_palabras():
    conn = conectar_db()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute("SELECT palabra, porcentaje_identidad, sinonimos FROM palabras_contabilidad;")
    palabras = cur.fetchall()
    conn.close()
    return palabras

# ====== LIMPIA TEXTO======
def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r"[^a-záéíóúüñ\s]", "", texto)

    palabras = texto.split()
    stop_words = set(stopwords.words('spanish'))

    palabras_filtradas = [p for p in palabras if p not in stop_words and len(p) > 3]
    return " ".join(sorted(set(palabras_filtradas)))  # elimina duplicados


# ====== CLASIFICADOR CON RAPIDFUZZ ======
def clasificar_texto(texto, umbral_similitud=80):
    palabras_db = obtener_palabras()
    if not palabras_db:
        return {"error": "No se pudieron cargar las palabras desde la base de datos."}

    texto_limpio = limpiar_texto(texto)
    palabras_texto = set(texto_limpio.split())
    total_palabras = len(palabras_texto)

    coincidencias = 0
    total_peso = 0
    palabras_detectadas = []

    for palabra, porcentaje, sinonimos in palabras_db:
        porcentaje = float(porcentaje)
        palabra = palabra.lower()
        sinonimos_lista = [s.strip().lower() for s in sinonimos.split(",")]

        # ===== Comparación con palabra principal =====
        matches = process.extract(palabra, palabras_texto, scorer=fuzz.ratio, score_cutoff=umbral_similitud)
        if matches:
            coincidencias += porcentaje
            total_peso += 100
            palabras_detectadas.append(palabra)
            continue

        # ===== Comparación con sinónimos =====
        for s in sinonimos_lista:
            matches = process.extract(s, palabras_texto, scorer=fuzz.ratio, score_cutoff=umbral_similitud)
            if matches:
                coincidencias += porcentaje * 0.8
                total_peso += 100
                palabras_detectadas.append(s)
                break

    # ===== Resultados finales =====
    if total_peso == 0 or total_palabras == 0:
        return {"tema": "Desconocido", "coincidencia": 0, "palabras_detectadas": []}

    promedio = coincidencias / total_peso
    # Suaviza penalización para textos largos
    factor_contexto = (len(palabras_detectadas) / total_palabras) ** 0.5
    porcentaje_final = round(promedio * factor_contexto * 100, 2)

    return {
        "tema": "Contabilidad",
        "coincidencia": porcentaje_final,
        "palabras_detectadas": list(set(palabras_detectadas)),
        "total_palabras": total_palabras
    }


# ====== PRUEBA LOCAL ======
if __name__ == "__main__":
    texto = input("Ingresa un texto a analizar: ")
    resultado = clasificar_texto(texto)
    print("\n=== RESULTADO ===")
    print(f"Tema detectado: {resultado['tema']}")
    print(f"Coincidencia: {resultado['coincidencia']}%")
    print(f"Palabras clave detectadas: {resultado['palabras_detectadas']}")
    print(f"Total de palabras analizadas: {resultado['total_palabras']}")