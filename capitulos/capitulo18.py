import streamlit as st

def mostrar18():

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/compañia3.jpeg", width='stretch')
        st.write("Siempre creí que en algún lugar existía una vida donde todo encajaba y aunque nunca la encontré del todo…nunca dejé de buscarla.”””")
    with col2:  
        #st.write("""Varias veces sentí que no debía soportar más humillaciones de Sara, a lo largo de mi matrimonio me fui como tres veces porque aunque a veces tenía bellísimos detalles otras me lastimaba profundamente con sus palabras o acciones , las tres regresé por mi hijo o por mis nietas después, incluso por Sara que alguna vez pudo decir lo siento , regresa, te extraño, .,""")
        st.image("imagenes/compañia2.jpeg", width='stretch')


    
    with col3:
        st.audio("audio/somwhereT.mp3")
        #st.write(" La última me dijo que me había estrenado , me había usado y ahora los PELLEJOS se los regalaba a Teresa todo era cierto y tal vez otras veces me había hecho o dicho cosas peores, pero esa vez dije hasta aquí y me fui y dije voy a viajar todo lo que pueda porque siempre me encantó hacerlo y en tres años he viajado mas que en toda mi vida aunque muchos trayectos lo he hecho solo nunca me ha faltado  con quien compartir, algunos muy reservados claro. ")
        st.image("imagenes/compañia1.jpeg", width='stretch')
