import streamlit as st
import random
import time

# Configuración de la página
st.set_page_config(page_title="Generador de Palabras Aleatorias", layout="centered")
st.title("Generador de Palabras Aleatorias")

# Cargar el diccionario de palabras
@st.cache
def load_dictionary():
    with open("rae_dictionary.txt", "r", encoding="utf-8") as file:
        return set(file.read().splitlines())

rae_words = load_dictionary()

# Generar combinaciones aleatorias de letras
def generate_random_letters():
    return "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(3, 8)))

# Mostrar combinaciones y verificar palabras
placeholder = st.empty()
found_words = st.container()
st.text("Generando combinaciones aleatorias de letras...")

with found_words:
    st.subheader("Palabras encontradas:")
    found_list = st.empty()

found_words_set = set()

def main_loop():
    while True:
        for _ in range(5):  # Generar 5 combinaciones por segundo
            random_word = generate_random_letters()
            placeholder.markdown(f"### {random_word}")

            if random_word in rae_words and random_word not in found_words_set:
                found_words_set.add(random_word)
                with found_list:
                    st.write(f"✅ {random_word}")

                time.sleep(5)  # Pausa de 5 segundos al encontrar una palabra
                break

            time.sleep(0.2)  # Esperar 0.2 segundos entre combinaciones (5 veces por segundo)

if __name__ == "__main__":
    main_loop()
