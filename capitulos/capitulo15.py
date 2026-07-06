import streamlit as st

def mostrar15():

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/tereia.jpeg", width='stretch')
        #st.write("Llego a mi vida un angel que me devolvio las ilusiones de tener una hija pero a la gente buena la maldad la ataca duramente, las calumnia e intrigas no me permitieron adoptarla")
     
    with col2:
        #st.image("imagenes/tereia.jpeg", width='stretch')
        st.write("Llego a mi vida un angel que me devolvio las ilusiones de tener una hija pero a la gente buena la maldad la ataca duramente, las calumnia e intrigas no me permitieron adoptarla")
     

    
    with col3:
        st.audio("audio/mininaT.mp3")
        #st.write(" Nuevamente senti una profunda soledad y una noche que iba a un  evento; le pedi a Maria de Los Ángeles la modista de mi mama que me acompañara, accedió y empezamos a salir porque ella tampoco tenia pareja, era mayor que yo y me decía mi bebe y todos los días me llevaba un panquecito  de chochitos, al poco tiempo le propuse matrimónio, para formar mi propia familia. “.”Despues mi error mi fantasia")

    