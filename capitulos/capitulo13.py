import streamlit as st

def mostrar13():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/Rosa.jpeg")
        st.write("Hubo un instante en que me sentí visto…aunque tal vez no fue real. Pero ese segundo bastó…para enseñarme lo que anhelaba ser.")

    with col2:
        #st.image("imagenes/sec51.jpeg")
        st.image("imagenes/SaraSola.jpeg")
        #st.write("Lo que había dentro.")

    with col3:
        st.audio("audio/sabesT.mp3")
        #st.image("imagenes/yotriste.jpeg")
        #st.write("Lo que había dentro.")


    