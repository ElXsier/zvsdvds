import streamlit as st
import time
import random

# Configurar la página
st.set_page_config(page_title="Chistes Buenos", layout="centered")
st.title("🤣 ¡Chistes Buenos! 🤣")

# Lista de chistes buenos
chistes = [
    "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
    "¿Por qué las bicicletas no se pueden mantener de pie solas? Porque están dos cansadas.",
    "¿Qué hace una abeja en el gimnasio? Zum-ba.",
    "¿Por qué los programadores odian la naturaleza? Porque tiene demasiados bugs.",
    "¿Cómo se despiden los químicos? Ácido un placer.",
    "¿Qué hace una planta cuando quiere hablar con otra? La llama por celular.",
    "¿Cuál es el café más peligroso del mundo? El ex-preso.",
    "¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas."
]

# Contenedor para mostrar el chiste
placeholder = st.empty()
st.write("¡Prepárate para reír cada 15 segundos!")

# Bucle para mostrar un chiste cada 15 segundos
while True:
    chiste = random.choice(chistes)
    placeholder.markdown(f"### {chiste}")
    time.sleep(15)
