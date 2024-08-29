

import streamlit as st
from textblob import TextBlob

st.title('Análisis de Sentimiento con TextBlob')

# Explicación sobre Polaridad y Subjetividad
st.sidebar.subheader("Polaridad y Subjetividad")
st.sidebar.write("""
Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
(hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
""")

# Análisis de Polaridad y Subjetividad
with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    texto = st.text_area('Escribe por favor: ')
    if texto:
        # Analiza el texto directamente en español
        blob = TextBlob(texto)
        polaridad = round(blob.sentiment.polarity, 2)
        subjetividad = round(blob.sentiment.subjectivity, 2)
        
        st.write('Polaridad: ', polaridad)
        st.write('Subjetividad: ', subjetividad)
        
        # Determina el tipo de sentimiento y muestra la imagen correspondiente
        if polaridad >= 0.5:
            st.image('AbuFeliz.jpg', caption='Sentimiento feliz de ver a los nietos 😊', use_column_width=True)
        elif polaridad <= -0.5:
            st.image('abueemo.jpg', caption='Sentimiento triste 😔', use_column_width=True)
        else:
            st.image('abuebue.jpeg', caption='Sentimiento viendo tele 😐', use_column_width=True)


