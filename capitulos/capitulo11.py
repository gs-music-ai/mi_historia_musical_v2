import streamlit as st

def mostrar11():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/canarios3.jpeg")
        st.write("La imagen que todos veían.")

    with col2:
        #st.image("imagenes/sec51.jpeg")
        st.image("imagenes/yotriste.jpeg")
        st.write("Lo que había dentro.")

    with col3:
        st.audio("audio/ojostrisT.mp3")
        #st.image("imagenes/yotriste.jpeg")
        #st.write("Lo que había dentro.")


    