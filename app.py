import streamlit as st
import time
import random

# Configurar la página
st.set_page_config(page_title="Chistes Buenos", layout="centered")
st.title("¡Chistes Buenos!")

# Lista de chistes buenos
chistes = [
    "¿Por qué los pájaros no usan Facebook? Porque ya tienen Twitter.",
    "¿Qué hace un pez en el agua? ¡Nada!",
    "¿Qué hace una abeja en el gimnasio? Zum-ba.",
    "¿Por qué los programadores odian la naturaleza? Porque tiene demasiados bugs.",
    "¿Cómo se despiden los químicos? Ácido un placer.",
    "¿Qué hace una planta cuando quiere hablar con otra? La llama por celular.",
    "¿Cuál es el café más peligroso del mundo? El ex-preso.",
    "¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas."
    "¿Cómo se llama un boomerang que no vuelve? Palo."
    "¿Por qué los elefantes no usan computadoras? Por miedo al ratón."
    "¿Cómo se llama un perro que vende helados? ¡Un perrito caliente!"
    "¿Qué hace un mago en el supermercado? Magiares."
    "¿Cómo se llama el pez más divertido? El pez payaso."
    "¿Qué hace un pato con un libro? Lo lee-cuack."
    "¿Por qué un tomate no toma café? Porque toma-té"
    "¿Qué le dijo un semáforo a otro? No me mires, estoy cambiando."
    "¿Qué hace un caballo en la computadora? ¡Click, click!"
    "¿Por qué los robots no van al cine? Porque ya vieron los trailers."
    "¿Qué hace una vaca con los ojos cerrados? Leche concentrada"
    "¿Cómo se llama el primo vegano de Bruce Lee? Broco Lee."
    "¿Dónde caga Batman? En el Bat-er."
]

# Contenedor para mostrar el chiste
placeholder = st.empty()
st.write("¡Prepárate para partirte de risa cada 8 segundos!")

# Bucle para mostrar un chiste cada 8 segundos
while True:
    chiste = random.choice(chistes)
    placeholder.markdown(f"### {chiste}")
    time.sleep(8)
