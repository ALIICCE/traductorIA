"""
Interfaz grafica para el analizador de texto usando Streamlit, permite
la entrada de texto y muestra los resultados acerca del tema contabilidad.
"""

import streamlit as st
from algoritmo import clasificar_texto

st.set_page_config(page_title="Text Analixer", layout="centered", page_icon="📝")

def app():
    """
    Funcion principal que carga la interfaz
    """
    st.title("Text Analixer - Contabilidad 📝")

    with st.form(key='Search'):
        text_query = st.text_area(
            label='Ingrese su texto',
            height=200,
            placeholder="Escribe o pega aqui el texto que deseas analizar..."
        )
        submit_button = st.form_submit_button(label='Analizar')

    if submit_button:
        if not text_query.strip():
            st.warning("Por favor, ingresa un texto para analizar.")
        else:
            st.subheader("Analisis Tematico 🧾")

            resultado = clasificar_texto(text_query)
            coincidencia = resultado.get("coincidencia", 0)
            tema = resultado.get("tema", "Desconocido")

            if coincidencia > 0:
                mensaje = f"Tema detectado: **{tema}** ({coincidencia}% de coincidencia)"

                if coincidencia <= 33:
                    st.error(mensaje)
                elif coincidencia <= 66:
                    st.warning(mensaje)
                else:
                    st.success(mensaje)

                detalles = resultado.get("detalles", [])
                if detalles:
                    lista_palabras = [item['original'] for item in detalles]
                    lista_unica = list(set(lista_palabras))

                    st.write("**Palabras clave encontradas:**")
                    st.info(", ".join(lista_unica))
                    st.caption(f"Total palabras clave unicas: {len(lista_unica)}")

            else:
                st.error("No se detecto relacion con el tema Contabilidad.")

if __name__ == '__main__':
    app()
