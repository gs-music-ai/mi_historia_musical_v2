import streamlit as st

def mostrar4():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/Estrella.jpeg")

    with col2:
        st.image("imagenes/GraYGis.jpeg")

    with col3:
        st.audio("audio/Munequita_lindaT.mp3")
        st.write("“A mis cuatro años, mi corazón ya sabía esperar… le hice espacio a un sueño y cada noche, como si el amor pudiera llegar en forma de milagro, la esperé… pero mi muñequita linda no llego...”")
        
    