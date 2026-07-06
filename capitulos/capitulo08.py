import streamlit as st

def mostrar8():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/maricarmenyyo.jpeg")

    with col2:
        st.image("imagenes/otromundo.jpeg")

    with col3:
        st.audio("audio/ojosverdesT.mp3")
        #st.image("imagenes/doblearcoagua.jpeg")
        st.write("Un día a mis 12 años , todo cambió con una mirada… y el mundo dejó de ser confuso por un instante.")


    