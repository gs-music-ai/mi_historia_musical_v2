import streamlit as st

def mostrar9():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/Habitacion_triste.jpeg")

    with col2:
        st.image("imagenes/verdeshojas.jpeg")

    with col3:
        st.audio("audio/verdeshojasT.mp3")
        #st.image("imagenes/verdeshojas.jpeg")
        st.write("Prometí un futuro que no pudo ser…y aprendí que no todos los sueños caminan al mismo ritmo.Pero el amor… ese sí fue real. Aunque tal vez no el que yo creí ")


    