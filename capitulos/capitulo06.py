import streamlit as st

def mostrar6():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/partida_Giselle.jpeg")

    with col2:
        st.image("imagenes/partida_giselle2.jpeg")

    with col3:
        st.audio("audio/ositoT.mp3")
        st.write("Existen  despedidas que el alma anticipa y ya duelen")
        st.write(" Sin saberlo, esta canción osito de felpa me hacía llorar… como si algo en mí ya supiera el triste final.,.")

    