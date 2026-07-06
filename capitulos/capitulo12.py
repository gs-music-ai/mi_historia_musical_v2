import streamlit as st

def mostrar12():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/papasconmiherm anoyo.jpeg")
        st.write("Despues de 11 años de espera por fin llego mi hermanito.")

    with col2:
        st.write("Tambien llego el amor.")

        st.image("imagenes/SaraSola.jpeg")
        #st.image("imagenes/yotriste.jpeg")

    with col3:
        st.audio("audio/felicidadT.mp3")
        #st.image("imagenes/yotriste.jpeg")
        st.write("Parecia que la felicidad habia llegado pero confundí el amor con pertenecer…y me entregué sin medida a un sueño que no era mío.")


    