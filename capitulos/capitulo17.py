import streamlit as st

def mostrar17():

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/ElyCami.jpeg", width='stretch')
        st.write("Seguí creyendo…aunque el mundo dijera que no era posible. Porque hay sueños que no se cumplen…pero tampoco se abandonan.…””")
    with col2:  
        #st.write("""Por segunda vez fui padre pero otra vez la vida me negó el poder compartirla con Ileana quien solo estuvo tres días en que sus pequeños ojos se abrían cuando me acercaba a la incubadora para decirme solo vengo de paso no puedo quedarme y regreso a las estrellas.,""")
        st.image("imagenes/ElyCami2.jpeg", width='stretch')


    
    with col3:
        st.audio("audio/suenoT.mp3")
        #st.write(" el dolor de la perdida fue desgarrador y otra vez le pedi a Dios que por favor me llevara  con el , era mas de lo que podia soportar , mi tío Manuel me hizo reaccionar al decirme ‘tu hijo te espera’ finalmente llegaron dos hermosas princesas que renovaron ilusiones  les  di todo mi amor y entrega , le pido a Dios que les de todo lo que necesiten para ser felices  y las proteja siempre.Despues la debacle del matrimonio ")
        st.image("imagenes/ElyCami3.jpeg", width='stretch')
