import streamlit as st

def mostrar16():

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/familia.jpeg", width='stretch')
        st.write(" Di más de lo que tenía…y me quedé vacío.Pero incluso en la caída…había una parte de mí que aún creía.")
    #with col2:  
        #st.write("""rompí mi compromiso y después  de un par de años nos casamos y por fin tuve el hijo y la familia  anhelada.Hubo momentos maravillosos pero yo nunca pude tomar la iniciativa en el sexo por mi problema hormonal solo respondía a los estímulos de Sara y yo tenía que esperar a que ella tomara la iniciativa siempre , .""")
        #st.image("imagenes/SaraSola.jpeg", width='stretch')
         
        

    
    with col3:
        st.audio("audio/mierrorT.mp3")
        #st.write(" Hubo  tambien  traiciones e infidelidades, en la última que soporté hablé con el tipo y le dije que le iba a dar el divorcio a Sara para que fueran felices , él cobardemente  dijo que nunca podría dejar a sus familia. No me divorcié pero por primera vez en la vida me llene de resentimiento y empecé a actuar como ella no por deseo sino por venganza , como yo no podía tener relaciones convencionales les pedía a ellas que tomaran la iniciativa ya que siempre las habían tomado a ellas y funciono “.”Despues el sueño imposible.")
