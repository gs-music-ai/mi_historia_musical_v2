import streamlit as st

def mostrar10():

    col1, col2, col3 = st.columns((1,1,1))

    with col1:
        #st.image("imagenes/fueron los dias.jpeg")
        st.write("En ese tiempo  encontré mi lugar sin tener que explicarme… rodeado de risas suaves y complicidades sencillas.Ahí por un momento, la vida fue amable conmigo.")

    with col2:
        st.image("imagenes/sec51.jpeg")

    with col3:
        st.audio("audio/fueronlosdiasT.mp3")
        st.image("imagenes/niñas secundaria.jpeg")
        #st.write("En ese tiempo  encontré mi lugar sin tener que explicarme… rodeado de risas suaves y complicidades sencillas.Ahí por un momento, la vida fue amable conmigo.")


    