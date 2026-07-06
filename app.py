import streamlit as st

from capitulos.capitulo01 import mostrar
from capitulos.capitulo02 import mostrar2
from capitulos.capitulo03 import mostrar3

from capitulos.capitulo04 import mostrar4
from capitulos.capitulo05 import mostrar5
from capitulos.capitulo06 import mostrar6
from capitulos.capitulo07 import mostrar7
from capitulos.capitulo08 import mostrar8
from capitulos.capitulo09 import mostrar9
from capitulos.capitulo10 import mostrar10
from capitulos.capitulo11 import mostrar11
from capitulos.capitulo12 import mostrar12
from capitulos.capitulo13 import mostrar13
from capitulos.capitulo14 import mostrar14
from capitulos.capitulo15 import mostrar15
from capitulos.capitulo16 import mostrar16
from capitulos.capitulo17 import mostrar17
from capitulos.capitulo18 import mostrar18
from capitulos.capitulo19 import mostrar19

from capitulos.capitulo20 import mostrar20




st.set_page_config(page_title="Mi música de vida", layout="centered")


st.write(" 🎶  Dale play en cada etapa a Un recorrido por momentos que me dejaron huella...")

# 🧠 Inicializar estado
if "pagina" not in st.session_state:
    st.session_state.pagina = 0

    # 🔝 BOTONES ARRIBA
colA, colB = st.columns(2)

with colA:
    if st.button("⏮️ Anterior") and st.session_state.pagina > 0:
        st.session_state.pagina -= 1
        st.rerun()

with colB:
    if st.button("⏭️ Siguiente") and st.session_state.pagina < 19:
        st.session_state.pagina += 1
        st.rerun()


# 🌅 ESCENA 1 - DESPEDIDA
if st.session_state.pagina == 0:
    mostrar()
# 🌅 ESCENA 2 - CACHITO
elif st.session_state.pagina == 1:
    mostrar2()

    
# 🌅 ESCENA 3 -  La muñeca fea
elif st.session_state.pagina == 2:

    mostrar3()

  

# 🌅 ESCENA 4 - muñequita linda
elif st.session_state.pagina == 3:
   
    mostrar4()
   
    
# 🌅 ESCENA 5 - La espera
elif st.session_state.pagina == 4:
    mostrar5()
    
    

        

    
    # 🌅 ESCENA 6 - La desilusion osito de felpa
elif st.session_state.pagina == 5:
    
    mostrar6()
    
    
    
    
      
# 🌅 ESCENA 7 - Me has mirado a los ojos
elif st.session_state.pagina == 6:
    mostrar7()
        

    
       

# 🌅 ESCENA 8 - Aquellos ojos verdes
elif st.session_state.pagina == 7:
    
    mostrar8()
    
        
       
    
       

# 🌅 ESCENA 9 - Las verdes hojas del verano
elif st.session_state.pagina == 8:
    
    mostrar9()
    
        
       



# 🌅 ESCENA 10 - Esos fueron los dias
elif st.session_state.pagina == 9:
    
        mostrar10()

    

# 🌅 ESCENA 11 - triste
elif st.session_state.pagina == 10:

     mostrar11()

# 🌅 ESCENA 12 - Felicidad
elif st.session_state.pagina == 11:
  mostrar12()
        
        

    
   
# 🌅 ESCENA 13 - Sabes una cosa
elif st.session_state.pagina == 12:
    mostrar13()
    
# 🌅 ESCENA 14 - un angel busco yo
elif st.session_state.pagina == 13:
    mostrar14()
    
    
    
# 🌅 ESCENA 15 - Mi niña cree en mi
elif st.session_state.pagina == 14:
    mostrar15()
    
# 🌅 ESCENA 16 - Mi error mi fantasia
elif st.session_state.pagina == 15:
    mostrar16()
    
       
        # 🌅 ESCENA 17 -El sueño imposible
elif st.session_state.pagina == 16:
    mostrar17()
    
   # 🌅 ESCENA 18 -en algun lugarel

elif  st.session_state.pagina == 17:

     mostrar18()

# 🌅 ESCENA 19 - mi viejo

elif st.session_state.pagina == 18:
           
           mostrar19()
  # 🌅 ESCENA 20 - camino a Dios
    
   
elif st.session_state.pagina == 19:
    mostrar20()
    