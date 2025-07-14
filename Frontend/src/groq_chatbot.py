import streamlit as st
from langchain_groq import ChatGroq
from groq import Groq
from langchain.schema import HumanMessage, AIMessage
from main import pipeline

if "messages" not in st.session_state:
    st.session_state.messages = []

#Título y cabeceras
st.title("💬🤖 Chatbot Interactivo")
st.header(":blue[Manual de Mantenimiento Técnico para Camiones Mineros]", divider ="blue")
st.subheader(":grey[*Creado por Grupo 6 - Programa en Python 2025-1*]", divider ="gray")

user_input = st.chat_input("Escribe tu pregunta...")

#Recorremos mensajes y establecemos los roles
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

#Definimos que se debe obtener una respuesta si existe un input de usuario
if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = pipeline(user_input)
    #print(response)

    assistant_reply = response["respuesta"]
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    with st.chat_message("assistant"):
        st.markdown(assistant_reply)