import streamlit as st

def mostrar():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/amanecer.jpeg")

    with col2:
        st.image("imagenes/huesuda.jpeg")

    with col3:
        from pathlib import Path

        BASE = Path(__file__).resolve().parent.parent

        st.audio(BASE / "audio" / "0despedidaM.mp3")
        st.write("Toda historia comienza mucho antes del primer recuerdo.Mucho antes de las palabras...Mucho antes de la memoria...Hubo un amanecer que empezó a escribir la mía.Ven...Escucha.La música hará el resto.")
        
    