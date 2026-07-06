import streamlit as st

def mostrar14():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/tereenburro.jpeg")
        st.write("En un instante me quede sin novia y sin mi mejor amigo pero llegaron tres angeles y uno aun permanece a mi lado")

    #with col2:
        #st.image("imagenes/sec51.jpeg")
        #st.image("imagenes/SaraSola.jpeg")
        #st.write("Lo que había dentro.")

    with col3:
        st.audio("audio/unangelT.mp3")
        #st.image("imagenes/yotriste.jpeg")
        #st.write("Lo que había dentro.")


    