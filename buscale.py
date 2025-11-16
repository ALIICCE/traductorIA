import streamlit as st
from algoritmo import clasificar_texto

st.set_page_config(page_title="Text Analixer", layout="centered", page_icon="📝")

def app():
    st.title("Text Analixer - Contabilidad 📝")

    with st.form(key='Search'):
        text_query = st.text_input(label='Ingrese su texto')
        submit_button = st.form_submit_button(label='Analizar')

    if submit_button:
        st.subheader("Análisis Temático 🧾")
        resultado = clasificar_texto(text_query)

        if resultado.get("coincidencia", 0) > 0:
            st.success(
                f"Tema detectado: **{resultado['tema']}** "
                f"({resultado['coincidencia']}% de coincidencia)"
            )
            st.write("Palabras detectadas:", ", ".join(resultado["palabras_detectadas"]))
        else:
            st.warning("No se detectaron palabras relacionadas con Contabilidad.")

if __name__ == '__main__':
    app()
