# 🧠 TraductorIA - Tema: Contabilidad

Este repositorio contiene un proyecto desarrollado en **Python** para analizar textos y determinar si pertenecen al tema **Contabilidad**.  
Además, incluye un archivo SQL que crea una base de datos local en **PostgreSQL** con palabras clave, sinónimos y porcentajes de identidad relacionados con el tema.

---

## 📁 Contenido

- **`db_Contabilidad.sql`**  
  Contiene:
  - Creación de la base de datos `db_contabilidad`
  - Creación de la tabla `palabras_contabilidad`
  - Inserción de palabras clave relacionadas con contabilidad y sus sinónimos

- **`buscale.py`**  
  Interfaz principal creada con **Streamlit**, que permite ingresar texto y analizar su relación con el tema de contabilidad.

- **`algoritmo.py`**  
  Contiene la lógica principal del análisis, limpieza del texto y cálculo del porcentaje de coincidencia usando técnicas de similitud léxica (**RapidFuzz** y **NLTK**).

- **`db_connection.py`**  
  Se encarga de conectar la aplicación con la base de datos PostgreSQL utilizando las variables de entorno definidas en el archivo `.env`.

---

## ⚙️ Configuración del entorno (.env)

Para conectar el proyecto con tu base de datos **PostgreSQL**, debes crear un archivo llamado `.env` en la raíz del proyecto.  
Estructura del archivo `.env`:

```bash
DB_NAME=db_contabilidad
DB_USER=postgres
DB_PASSWORD=tu_contraseña_aquí
DB_HOST=localhost
DB_PORT=5432
