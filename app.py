import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# Configuraciones iniciales
translator = Translator()
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
        # Realiza la traducción y el análisis
        blob = TextBlob(texto)
        polaridad = round(blob.sentiment.polarity, 2)
        subjetividad = round(blob.sentiment.subjectivity, 2)
        
        st.write('Polaridad: ', polaridad)
        st.write('Subjetividad: ', subjetividad)
        
        # Determina el tipo de sentimiento y muestra la imagen correspondiente
        if polaridad >= 0.5:
            st.image('https://i.imgur.com/4B6QOIZ.png', caption='Sentimiento Positivo 😊', use_column_width=True)
        elif polaridad <= -0.5:
            st.image('https://i.imgur.com/2m4tzP1.png', caption='Sentimiento Negativo 😔', use_column_width=True)
        else:
            st.image('https://i.imgur.com/ZZyje85.png', caption='Sentimiento Neutral 😐', use_column_width=True)

# Corrección de texto en inglés
with st.expander('Corrección en inglés'):
    texto_ingles = st.text_area('Escribe en inglés para corrección: ', key='4')
    if texto_ingles:
        blob2 = TextBlob(texto_ingles)
        st.write(blob2.correct())
