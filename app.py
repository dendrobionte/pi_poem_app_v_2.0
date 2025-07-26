
import streamlit as st
import random

def load_number(file_name):
    with open(file_name, "r") as f:
        return f.read().strip()

def load_text(file):
    text = file.read().decode("utf-8")
    words = text.replace("\n", " ").split()
    return words

def get_blocks(number_string, block_size, start_index):
    blocks = []
    for i in range(start_index, len(number_string) - block_size + 1, block_size):
        block = number_string[i:i + block_size]
        if block.isdigit():
            blocks.append(int(block))
    return blocks

def generate_poem(words, blocks):
    poem_words = []
    for block in blocks:
        index = block % len(words)
        poem_words.append(words[index])
    return poem_words

def create_tankas(poem_words):
    tankas = []
    for i in range(0, len(poem_words), 7):
        verse = poem_words[i:i+7]
        if len(verse) == 7:
            tankas.append(" ".join(verse))
    return tankas

st.set_page_config(page_title="Poema Numérico v2.0", layout="wide")
st.title("✍️ Poema Numérico 2.0")
st.markdown("Generador poético a partir de π, e, φ o √2.")

number_choice = st.sidebar.selectbox(
    "Elige la constante numérica:",
    ("π (pi)", "e", "φ (phi)", "√2"),
    format_func=lambda x: x
)

number_file_map = {
    "π (pi)": "pi.txt",
    "e": "e.txt",
    "φ (phi)": "phi.txt",
    "√2": "sqrt2.txt"
}

block_size = st.sidebar.slider("Tamaño del bloque", min_value=2, max_value=6, value=3)
start_index = st.sidebar.slider("Punto de inicio", min_value=0, max_value=1000, value=0, step=10)

uploaded_file = st.file_uploader("Sube un texto (.txt)", type=["txt"])

if uploaded_file:
    words = load_text(uploaded_file)
    number_string = load_number(number_file_map[number_choice])
    blocks = get_blocks(number_string, block_size, start_index)
    poem_words = generate_poem(words, blocks)
    tankas = create_tankas(poem_words)

    st.markdown(f"### 🌿 Poema generado con {number_choice}")
    for i, tanka in enumerate(tankas, start=1):
        st.markdown(f"**{i}.** *{tanka}*")
