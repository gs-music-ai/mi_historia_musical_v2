import streamlit as st

def mostrar7():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/comunion1.jpeg")
        st.write("Hubo muchas veces en que pedí irme por no entender mi lugar en este mundo.Y aun así… aquí seguí.")

    with col2:
        st.image("imagenes/nardem.jpeg")

    with col3:
        st.audio("audio/mehasmiradoT.mp3")
        st.image("imagenes/doblearcoagua.jpeg")


    