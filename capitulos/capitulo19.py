import streamlit as st

def mostrar19():

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
      
        st.image("imagenes/papa.jpeg", width='stretch')
        st.write("Mi viejo. Me hubiera gustado compartir muchas cosas con mi padre, tristezas, alegrias , momentos.Entre lo que fue… y lo que pudo ser…queda un espacio lleno de preguntas.Y aun así…también quedan pequeños gestos que nunca olvidé.” ")

   # with col2:
        
        #st.write("Como el dia que competi por unica vez por una cinta en Artes Marciales, el llego con mi hermano a verme, Sara prefirio ir a ver jugar football a sus compañeros o el dia que me regalo mi primer reloj o el disco del golpe,cuando me llegó el momento de ser padre y tuve a mi hijo Gerardo Isaías  me dije , voy a ser el padre que me hubiera gustado tener y puse mi mejor empeño en serlo, claro que no lo logré pero por lucha no quedó. ")

    with col3:
        st.audio("audio/viejoT.mp3")
        st.write("No se donde me toque el capitulo final por lo pronto estoy en el bello caribe mexicano con los valencias y les doy las gracias por sus atenciones ")
        st.image("imagenes/valencias.jpeg", width='stretch')


        #st.image("imagenes/SaraSola.jpeg", width='stretch')
