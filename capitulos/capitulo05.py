import streamlit as st

def mostrar5():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        st.image("imagenes/piano.jpeg")

    with col2:
        st.image("imagenes/abuelajoven.jpeg")

    with col3:
        st.audio("audio/CaprichoT.mp3")
        st.write("En medio de todo…hubo destellos que me dieron refugio .Un piano, una voz, una presencia…y el mundo volvía a estar en su lugar.")
        
    