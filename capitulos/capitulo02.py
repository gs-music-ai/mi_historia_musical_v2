import streamlit as st

def mostrar2():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/mamaenpoli.jpeg")

    with col2:
        st.image("imagenes/debebe.jpeg")

    with col3:
        st.audio("audio/cachitoT.mp3")
        st.write("“No fue el juguete lo que marcó mi infancia, sino el sueño que despertó en mí.”")
        
    