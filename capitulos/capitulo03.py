import streamlit as st

def mostrar3():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/muneca_fea.jpeg")

    with col2:
        st.image("imagenes/Habitacion_triste.jpeg")

    with col3:
        st.audio("audio/Munequita_feaT.mp3")
        st.write("“Entre sombras y silencios, también florecen los sueños. Algunas canciones abrazan al niño que alguna vez fuimos.”")
        
    