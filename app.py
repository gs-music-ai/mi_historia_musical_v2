import streamlit as st

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
    col1, col2, col3 = st.columns([1,1,1])


    with col1:
    
        st.image("imagenes/amanecer.jpeg")


    with col2:
        st.image("imagenes/huesuda.jpeg")
    with col3:
        st.audio("audio/0despedidaM.MP3")
        st.write("🎶Espero te guste esta despedida que inicie su prepararción cuando la huesuda se acerco a recordarme suavemente al oido que todo principio tiene un final")

        st.write("Después de esta introduccion comienza el recorrido musical de mi vida.")

# 🌅 ESCENA 2 - CACHITO
elif st.session_state.pagina == 1:
    col1, col2, col3 = st.columns([1,1,1])
    

        

    with col1:

        st.image("imagenes/mamaenpoli.jpeg")  
        st.write("CACHITO.Mamá Graciela luchando por su beca en el politecnico y estudiando dos carreras")


    with col2:
        st.image("imagenes/debebe.jpeg")
        st.write(" Para mi todo empezo en 1954")
        
    with col3:
    
       st.audio("audio/cachitoT.mp3")
       st.write("Hubo un tiempo en que el mundo cabía en unas manos que me cuidaban… y en una canción,cachito,que me nombraba con ternura. Ahí fui amado sin preguntas… ahí fui, simplemente, yo.")
       st.write("Después de esta canción… la niñez.")


    
# 🌅 ESCENA 3 -  La muñeca fea
elif st.session_state.pagina == 2:
    col1, col2, col3 = st.columns([1,1,1])
    

        

    with col1:

        st.image("imagenes/muñeca_fea.jpeg")  
        st.write("La muñeca fea. Viví mucho tiempo sintiéndome fuera de lugar… como si mi esencia no tuviera nombre ni espacio.Pero incluso en silencio…algo en mí seguía siendo hermoso")



    with col2:
        st.image("imagenes/Habitacion_triste.jpeg")
        st.write(" Hubo una época en que me sentía exactamente así, escondido tras los rincones como la muñeca fea, mirando al mundo a travez de una ventana de un modesto departamento.")

    with col3:
    
       st.audio("audio/Muñequita_feaT.mp3")
       st.write(" Para que mi madre pudiera seguir estudiando no podía presentarme como su hijo y yo no podía decirle mamá se quedó la instrucción tan impregnada que así la llamé por primera vez cuando me entregaron sus cenizas")
       st.write("Después de esta canción… Entre la esperanza y la desilusion.")


# 🌅 ESCENA 4 - muñequita linda
elif st.session_state.pagina == 3:
    col1, col2, col3 = st.columns([1,1,1])
    

        

    with col1:

        st.image("imagenes/Estrella.jpeg")  
        st.write("Muñequita linda. Desde muy pequeño, mi corazón ya sabía esperar…le hice espacio a un sueño cada noche,como si el amor pudiera llegar en forma de milagro.La esperé… con una fe que nadie veía.")

    with col2:
        st.image("imagenes/GraYGis.jpeg")
        st.write(" Yo desconocía la diferencia de géneros y el concepto de madre en mi entorno era muy difuso , a los cuatro años por primera vez salí del departamento donde permanecí escondido y vi a una mujer con su bebe y dándole toda su ternura pregunté y me dijeron que era una madre con su bebé que acababa de llegar del cielo  y decidí que yo quería ser madre ,.")

    with col3:
    
       st.audio("audio/Muñequita_lindaT.mp3")
       st.write("  recordé un cuento creo que otomí en el cual una mujer solitaria había pedido compañía a una estrella y la estrella descendió como una bella niña. Una noche Pedí lo mismo a la estrella más brillante y desde esa noche hice un lugar en mi pequeña cama para recibirla y cuidarla toda la vida .Esta canción la cantaba en silencio… para alguien que nunca llegó, pero que siempre sentí cerca.")
       st.write("Después de esta canción… la espera")

# 🌅 ESCENA 5 - La espera
elif st.session_state.pagina == 4:
    col1, col2, col3 = st.columns([1,1,1])
    

        

    with col1:
        st.image("imagenes/piano.jpeg")
        
        st.write("Vals capricho. En medio de todo…hubo destellos que me dieron refugio .Un piano, una voz, una presencia…y el mundo volvía a estar en su lugar.")

    with col2:
        st.image("imagenes/abuelajoven.jpeg")
        st.write(" en mi espera había momentos felices , los breves que pasaba con mi madre, las historias de mi tía Mary ")

    with col3:
    
       st.audio("audio/CaprichoT.mp3")
       st.write("  y la música que tocaba mi abuela en el piano , este vals Capricho de Ricardo Castro era uno de los que frecuentemente le pedía tocar y que intenté aprender completo sin éxito...")
       st.write("Después de esta canción… la desilusion")

    # 🌅 ESCENA 6 - La desilusion osito de felpa
elif st.session_state.pagina == 5:
    col1, col2, col3 = st.columns([1,1,1])
    

        

    with col1:

        st.image("imagenes/partida_Giselle.jpeg")  

        st.write(" Osito de felpa. Existen  despedidas que el alma anticipa y ya duelen")



    with col2:
        st.image("imagenes/partida_Giselle2.jpeg")  
        st.write(" Sin saberlo, esta canción osito de felpa me hacía llorar… como si algo en mí ya supiera que no iba a llegar.,.")

    with col3:
    
       st.audio("audio/ositoT.mp3")
       st.image("imagenes/Arcoiris.jpeg")  
       st.write("Después de esta canción… la resignacion")

# 🌅 ESCENA 7 - Me has mirado a los ojos
elif st.session_state.pagina == 6:
    col1, col2, col3 = st.columns([1,1,1])
    

        

    with col1:

        
        st.write("")
        st.image("imagenes/comunion1.jpeg")
        st.write(" Me has mirado a los ojos. Hubo muchas veces en que pedí irme por no entender mi lugar en este mundo.Y aun así… aquí seguí.Deseaba hacer mi primera comunión porque me habían dicho que me acercaría a  Dios. Cuando mi espera resultó inútil le dije a Dios que estaba en el lugar equivocado que aceptara una devolución y me regresara con él pero tampoco fue concedida esta petición . ,.")

    with col2:
        st.image("imagenes/nardem.jpeg")  
        
        st.write("  en cambio en sueños una hermosa niña apareció y me dijo que no le habían permitido llegar a mi lado , y me mostró un hermoso jardín en el que se encontraba.")

    with col3:
    
       st.audio("audio/mehasmiradoT.mp3")
       st.image("imagenes/doblearcoagua.jpeg")
       st.write(" desperté y le dije a mi madre que a donde la habían llevado que fuéramos por ella y me dijo fue un sueño, no existe esa niña, 40 años después me confesó que mi padre la había hecho abortar.Después de esta canción… Nueva ilusión")



# 🌅 ESCENA 8 - Aquellos ojos verdes
elif st.session_state.pagina == 7:
    col1, col2, col3 = st.columns([1,1,1])
    

        

    with col1:

        
        st.write("")
        st.image("imagenes/maricarmenyyo.jpeg")
        st.write(" Aquellos ojos verdes. Un día a mis 12 años , todo cambió con una mirada… y el mundo dejó de ser confuso por un instante. Aunque yo no entendía quién era…sí sabía lo que sentía.”,.")

    with col2:
        st.image("imagenes/otromundo.jpeg")  
        
        st.write("  “En un instante nuestras miradas se cruzaron sus verdes ojos se clavaron en los míos , el tiempo se detuvo , me sentí en otro mundo maravilloso ella era huérfana y la trataban mal , quise rescatarla y,.”.")

    with col3:
    
       st.audio("audio/ojosverdesT.mp3")
       st.write("   aunque me decían que estaba loco, obtuve la ayuda para casarnos e irnos a vivir lejos, ella seguiría estudiando y yo trabajaría y también estudiaría , todo estaba listo pero ella tuvo miedo , le dije disfruta tu vida como es, yo te hubiera cuidado para siempre pero el miedo paraliza y tú lo permitiste , jamás la volvi a ver pero la lloré por ańos. Después de esta canción… El dolor y la esperanza")


# 🌅 ESCENA 9 - Las verdes hojas del verano
elif st.session_state.pagina == 8:
    col1, col2, col3 = st.columns([1,1,1])
    

        

    with col1:

        
        st.write("")
        st.image("imagenes/Habitacion_triste.jpeg")
        st.write(" Las verdes hojas del verano. Prometí un futuro que no pudo ser…y aprendí que no todos los sueños caminan al mismo ritmo.Pero el amor… ese sí fue real. Aunque tal vez no el que yo creí porque aunque quería casarme no era por un interés sexual que aún no despertaba, solo quería cuidarla, verla feliz y que nadie la lastimara.”.”,.")

    with col2:
        st.image("imagenes/verdeshojas.jpeg")  
        
        st.write("  ““Quise cambiar mi destino por amor… pero no todos los sueños están listos para suceder, el dolor de la pérdida era muy intenso y tomé una decisión solo tendría amigas , estudiaría psicología en la UNAM y al terminar buscaría una beca a España, encontraría una chica linda como Mary Carmen y ahora si me casaría, porque según mi imaginario todas las espańolas eran muy parecidas.”.")

    with col3:
    
       st.audio("audio/verdeshojasT.mp3")
       st.write("   Las verdes hojas del verano simpre me hacian pensar en ella, desconozco la razon pero al escuchar esta cancion el llanto era inevitable Después de esta canción… Año de paz")




# 🌅 ESCENA 10 - Esos fueron los dias
elif st.session_state.pagina == 9:
    col1, col2, col3 = st.columns([1,1,1])
    

        

    with col1:

        
        st.write("")
        #st.image("fueron los dias.jpeg")
        st.write(" Esos fueron los dias. En ese tiempo  encontré mi lugar sin tener que explicarme… rodeado de risas suaves y complicidades sencillas.Ahí fui ligero y por un momento, la vida fue amable conmigo.. .a los 13 años, me cambie de escuela para no volver a ver a Mary Carmen ,mantuve solo a mi amigo de siempre que era como mi hermano se llamaba Joel y tuve 6 nuevas excelentes amigas,")

    with col2:
        st.image("imagenes/sec51.jpeg")  
        
        st.write(" Fue un año maravilloso en que compartí todo con ellas, tareas visitas a museos , etc y penetre en el mundo femenino , en sus ilusiones, en sus sueños y ahí mi manera soñadora y sentimental de ser no era mal vista.")

    with col3:
    
       
       st.audio("audio/fueronlosdiasT.mp3")
       st.write("   así fue hasta el segundo año de preparatoria, a todas las chicas que mostraban interés en mi les platicaba mis plan de vida y que no podía tener novia hasta realizarlo. Después de esta canción… Doble cara")
       st.image("imagenes/niñas secundaria.jpeg")
       



# 🌅 ESCENA 11 - triste
elif st.session_state.pagina == 10:

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/canarios3.jpeg", width='stretch')
        st.write("El muchacho de los ojos tristes. La imagen que todos veían")

    with col2:  
         st.write("Lo que había dentro")
         st.image("imagenes/yotriste.jpeg", width='stretch')
       
       
    
    with col3:
        st.audio("audio/ojostrisT.mp3")
        st.write("""
Aprendí a sonreír como se esperaba de mí…

a encajar en una forma  
que no terminaba de ser mía.

Pero alguien lo vio.

Vio más allá de la sonrisa,  
más allá de la ropa,  
más allá del papel.

Y entonces supe…  
que no estaba completamente oculto.Despues Nuevas ilusiónes
""")

# 🌅 ESCENA 12 - Felicidad
elif st.session_state.pagina == 11:

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/papasconmiherm anoyo.jpeg", width='stretch')
        st.write("Felicidad. A los 15 años ocurrió algo inesperado tuve un hermano , que desperto en mi anhelos que creía marchitos, ayude en lo que pude en los preparativos para recibirlo y por fin llegó ese bebé que había pedido 11 años atrás  ")
    with col2:  
        st.write("""
pero casi simultáneamente llegó alguien que cambiaría mi planes su nombre Sara , también huérfana que en un principio la vi como hija y quise apoyarla.
⸻""")
        st.image("imagenes/SaraSola.jpeg", width='stretch')
         
        

    
    with col3:
        st.audio("audio/felicidadT.mp3")
        st.write("“Parecia que la felicidad habia llegado pero confundí el amor con pertenecer…y me entregué sin medida a un sueño que no era mío.Por un momento fui feliz…aunque me estuviera perdiendo. Despues el conflicto”")

# 🌅 ESCENA 13 - Sabes una cosa
elif st.session_state.pagina == 12:

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/Rosa.jpeg", width='stretch')
        st.write("Sabes una cosa. Hubo un instante en que me sentí visto…aunque tal vez no fue real.Pero ese segundo bastó…para enseñarme lo que anhelaba ser.”")
    with col2:  
        st.write("""Sara no pidió permiso me acarició y me besó a su antojo, ignorando mi plática de que tenías planes y no quería enamorarme, eventualmente me decía, si te molesta no lo hago pero la verdad no me molestaba al contrario despertó en mí la sexualidad dormida pero de una manera diferente a lo que se esperaría.""")
        #st.image("imagenes/SaraSola.jpeg", width='stretch')
         
        

    
    with col3:
        st.audio("audio/sabesT.mp3")
        st.write("Ańos después lo entendí cuando una endocrinóloga me explicó que tenía una alteracion hormonal en que predominaban en mí hormonas femeninas que explicaban  todo lo que me había ocurrido desde mi deseo de tener un hijo a los 4 años hasta lo que me hacían sentir las caricias y los besos de Sara, la Dra lo llamó caprichos de la naturaleza“.”Despues el sueño imposible")

# 🌅 ESCENA 14 - un angel busco yo
elif st.session_state.pagina == 13:

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/tereenburro.jpeg", width='stretch')
        st.write("Un angel busco yo. El conflicto surgió porque mi padre trató mal a Sara y posteriormente ya casados a mi hijo a quien le impedía jugar con mi hermanito yo estaba acostumbrado a sus modos y lo ignoraba pero Sara me ordenó alejarme y la obedecí , sólo pasaba ya tiempo con ella y no pude disfrutar ni de mi madre ni de mi hermano porque no tuve el valor de defender ese derecho aunque tuviera razón referente a mi padre, pero  aún de novios a pesar de mi sumisión Sara siempre peleaba por algo y yo acababa disculpándomel pero una noche en que mi madre estaba en peligro de muerte en el hospital ella me acompañó a visitarla junto con mi mejor amigo , al salir del hospital ella se subió al asiento de atrás del carro de mi madre, me dejaron de chofer y todo el camino estuvo vacilando, riéndose y coqueteando con mi amigo,”")
    with col2:  
        st.write("""me sentí herido  por ambos y la situación en que me encontraba, pasé a dejar a mi amigo y después le reclamé a Sara su actitud y me dijo con sarcasmo pues si no te gusta vete, dicho que me había repetido muchas veces pero esa vez si me fui, no cedí , y esa noche me quede sin amigo y sin novia, pedí a Dios que me enviara un ángel a ayudarme , después mi madre salió del hospital y solo recibí ayuda de la modista de mi mamá María de los Ángeles , posteriormente a mí me operaron y en mi vida apareció un ángel de 12 años que se crió por azares del destino en una pequeña población  en el estado de Puebla,""")
        #st.image("imagenes/SaraSola.jpeg", width='stretch')
         
        

    
    with col3:
        st.audio("audio/unangelT.mp3")
        st.write(" alli aprendió a amar a cualquier ser vivo y al campo en general , su nombre Teresa , quien a pesar de que la vida la ha golpeado duramente en muchas ocasiones, siempre tiene amor para compartir con cualquier persona, animal o planta que la necesite y yo en particular tuve el privilegio en esos momentos difíciles de contar con ella incondicionalmente. La quise adoptar y no fue posible, lamentablemente  tuvo una vida complicada al lado de un mal marido,Ella y yo  a pesar del sufrimiento decidimos no amargarnos sino transmutar el dolor en amor para compartir, hasta la fecha cuento con ella “.”Despues la ilusion de formar mi propia familia")

# 🌅 ESCENA 15 - Mi niña cree en mi
elif st.session_state.pagina == 14:

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/tereia.jpeg", width='stretch')
        st.write("Mi niña cree en mi. Tere llego a la casa porque escucho que mi madre estaba enferma y necesitaba ayuda para cuidar a mi hermanito y se ofreció a hacerlo, pero cuando vio que yo estaba recién operado y necesitaba ayuda también de inmediato me la brindo, yo en broma le decía venias a cuidar al niño chiquito no al grande y se reía y me decía puedo cuidar a ambos ,pasamos muy agradables momentos por su sentido del humor y en poco tiempo se gano todo mi cariño y la empezó a sentir como la hija que tanto había soñado:,”")
    with col2:  
        st.write("""Sus padres la habían regalado con su abuela y recién la habían vuelto a traer con ellos hasta los 12 años, cuando conocí su historia y platique con su maestro de 6 año, decidí adoptarla y pedi ayuda a un amigo que estaba bien relacionado, cuando todo estuvo  listo e iba a ir por ella con una patrulla, ella dijo que se podría enfermar su papa del susto yo recordé lo de Mary Carmen y le dije lo mismo que a ella, sigue como estas y sin darle oportunidad a mas también me aleje de ella.
,""")
        #st.image("imagenes/SaraSola.jpeg", width='stretch')
         
        

    
    with col3:
        st.audio("audio/miniñaT.mp3..mp3")
        st.write(" Nuevamente senti una profunda soledad y una noche que iba a un  evento; le pedi a Maria de Los Ángeles la modista de mi mama que me acompañara, accedió y empezamos a salir porque ella tampoco tenia pareja, era mayor que yo y me decía mi bebe y todos los días me llevaba un panquecito  de chochitos, al poco tiempo le propuse matrimónio, para formar mi propia familia. “.”Despues mi error mi fantasia")

# 🌅 ESCENA 16 - Mi error mi fantasia
elif st.session_state.pagina == 15:

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/familia.jpeg", width='stretch')
        st.write("Mi error mi fantasia. Di más de lo que tenía…y me quedé vacío.Pero incluso en la caída…había una parte de mí que aún creía.estaba a punto de casarme con María de los Ángeles pero después de un ańo de ausencia Sara apareció  de nuevo, con sus caricias , la forma en que me tocaba y me miraba volvió a despertar sensaciones irresistibles y de nuevo a entregarme incondicionalmente, mi voluntad se volvió la suya. ””")
    with col2:  
        st.write("""rompí mi compromiso y después  de un par de años nos casamos y por fin tuve el hijo y la familia  anhelada.Hubo momentos maravillosos pero yo nunca pude tomar la iniciativa en el sexo por mi problema hormonal solo respondía a los estímulos de Sara y yo tenía que esperar a que ella tomara la iniciativa siempre , .
,""")
        #st.image("imagenes/SaraSola.jpeg", width='stretch')
         
        

    
    with col3:
        st.audio("audio/mierrorT.mp3")
        st.write(" Hubo  tambien  traiciones e infidelidades, en la última que soporté hablé con el tipo y le dije que le iba a dar el divorcio a Sara para que fueran felices , él cobardemente  dijo que nunca podría dejar a sus familia. No me divorcié pero por primera vez en la vida me llene de resentimiento y empecé a actuar como ella no por deseo sino por venganza , como yo no podía tener relaciones convencionales les pedía a ellas que tomaran la iniciativa ya que siempre las habían tomado a ellas y funciono “.”Despues el sueño imposible.")

       
        # 🌅 ESCENA 17 -El sueño imposible
elif st.session_state.pagina == 16:

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/ElyCami.jpeg", width='stretch')
        st.write("El sueño imposible. Seguí creyendo…aunque el mundo dijera que no era posible.Porque hay sueños que no se cumplen…pero tampoco se abandonan.”Dentro de los altibajos en mi matrimonio , aun soñaba con una pareja de hijos niño y niña, la relaciones con Sara eran muy escasas porque ella decía que mas valía calidad que cantidad, un dia en mi desesperación por única vez en todos los años de matrimonio tome la iniciativa y por alguna extraña razón pude funcionar y …””")
    with col2:  
        st.write("""Por segunda vez fui padre pero otra vez la vida me negó el poder compartirla con Ileana quien solo estuvo tres días en que sus pequeños ojos se abrían cuando me acercaba a la incubadora para decirme solo vengo de paso no puedo quedarme y regreso a las estrellas.
,""")
        st.image("imagenes/ElyCami2.jpeg", width='stretch')


    
    with col3:
        st.audio("audio/sueñoT.mp3")
        st.write(" el dolor de la perdida fue desgarrador y otra vez le pedi a Dios que por favor me llevara  con el , era mas de lo que podia soportar , mi tío Manuel me hizo reaccionar al decirme ‘tu hijo te espera’ finalmente llegaron dos hermosas princesas que renovaron ilusiones  les  di todo mi amor y entrega , le pido a Dios que les de todo lo que necesiten para ser felices  y las proteja siempre.Despues la debacle del matrimonio ")
        st.image("imagenes/ElyCami3.jpeg", width='stretch')

   # 🌅 ESCENA 18 -en algun lugarel

elif  st.session_state.pagina == 17:

    col1, col2, col3 = st.columns([1,1,1])

    with col1:
        st.image("imagenes/compañia3.jpeg", width='stretch')
        st.write("Somwhere. Siempre creí que en algún lugar existía una vida donde todo encajaba y aunque nunca la encontré del todo…nunca dejé de buscarla.”””")
    with col2:  
        st.write("""Varias veces sentí que no debía soportar más humillaciones de Sara, a lo largo de mi matrimonio me fui como tres veces porque aunque a veces tenía bellísimos detalles otras me lastimaba profundamente con sus palabras o acciones , las tres regresé por mi hijo o por mis nietas después, incluso por Sara que alguna vez pudo decir lo siento , regresa, te extraño, .
,""")
        st.image("imagenes/compañia2.jpeg", width='stretch')


    
    with col3:
        st.audio("audio/somwhereT.mp3")
        st.write(" La última me dijo que me había estrenado , me había usado y ahora los PELLEJOS se los regalaba a Teresa todo era cierto y tal vez otras veces me había hecho o dicho cosas peores, pero esa vez dije hasta aquí y me fui y dije voy a viajar todo lo que pueda porque siempre me encantó hacerlo y en tres años he viajado mas que en toda mi vida aunque muchos trayectos lo he hecho solo nunca me ha faltado  con quien compartir, algunos muy reservados claro. ")
        st.image("imagenes/compañia1.jpeg", width='stretch')


# 🌅 ESCENA 19 - mi viejo

elif st.session_state.pagina == 18:
    col1, col2, col3 = st.columns([1,1,1])

    with col1:
      
        st.image("imagenes/papa.jpeg", width='stretch')
        st.write("Mi viejo. Me hubiera gustado compartir muchas cosas con mi padre, tristezas, alegrias , momentos.Entre lo que fue… y lo que pudo ser…queda un espacio lleno de preguntas.Y aun así…también quedan pequeños gestos que nunca olvidé.” ")

    with col2:
        
        st.write("Como el dia que competi por unica vez por una cinta en Artes Marciales, el llego con mi hermano a verme, Sara prefirio ir a ver jugar football a sus compañeros o el dia que me regalo mi primer reloj o el disco del golpe,cuando me llegó el momento de ser padre y tuve a mi hijo Gerardo Isaías  me dije , voy a ser el padre que me hubiera gustado tener y puse mi mejor empeño en serlo, claro que no lo logré pero por lucha no quedó. ")

    with col3:
        st.audio("audio/viejoT.mp3")
        st.write("No se donde me toque el capitulo final por lo pronto estoy en el bello caribe mexicano con los valencias y les doy las gracias por sus atenciones ")
        st.image("imagenes/valencias.jpeg", width='stretch')


        #st.image("imagenes/SaraSola.jpeg", width='stretch')
         # 🌅 ESCENA 20 - camino a Dios
    
   
elif st.session_state.pagina == 19:
    col1, col2  = st.columns([1,1])
    with col1:
       
        st.image("imagenes/camino a Dios.jpeg", width='stretch')

    with col2:
        st.audio("audio/DiosT.mp3")
        st.write("Por último agradezco profundamente a los que me amaron y apoyaron en mi tránsito por este plano , pero también a los que me dañaron intencionalmente o no porque todo es un aprendizaje.En mi interior hay un torrente de amor que trate de repartir entre todos los que tuve cerca y lo hice sin limitaciones.La vida me quitó pero también me dio y Como dijo Amado Nervo digo vida nada me debes vida estamos en paz. Dios los bendiga en su camino sean felices por favor , la vida es bella disfrútenla Adiós a todos  ")
       
    
