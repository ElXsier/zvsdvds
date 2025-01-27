import streamlit as st
import random
import time
import os
from playsound import playsound

# Configuración de la página
st.set_page_config(page_title="Generador de Palabras Aleatorias", layout="centered")
st.title("Generador de Palabras Aleatorias con Sonidos")

# Cargar el diccionario de palabras
@st.cache
def load_dictionary():
    with open("rae_dictionary.txt", "r", encoding="utf-8") as file:
        return set(file.read().splitlines())

rae_words = load_dictionary()

# Generar combinaciones aleatorias de letras
def generate_random_letters():
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(3, 8)))

# Reproducir un sonido aleatorio
def play_random_sound():
    sounds = ["sound1.mp3", "sound2.mp3", "sound3.mp3"]
    sound = random.choice(sounds)
    playsound(sound)

# Mostrar combinaciones y verificar palabras
placeholder = st.empty()
found_words = st.container()
st.text("Cargando combinaciones aleatorias...")

with found_words:
    st.subheader("Palabras encontradas:")
    found_list = st.empty()

found_words_set = set()

while True:
    random_word = generate_random_letters()
    placeholder.markdown(f"### {random_word}")

    if random_word in rae_words and random_word not in found_words_set:
        found_words_set.add(random_word)
        with found_list:
            st.write(f"✅ {random_word}")
        play_random_sound()

    time.sleep(1)
