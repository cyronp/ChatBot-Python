import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

with st.sidebar:
  st.title("Configurações")
  st.text("Aqui você pode configurar da o funcionamento e inteligencia do seu chatbot como quiser.")
  gemini_version = st.selectbox(
    "Qual versão do Gemini você deseja?",
    ("gemini-2.5-flash-lite", "gemini-2.5-flash", "gemini-2.5-pro")
  )
  estilo = st.radio("Qual estilo deseja que as paletas sejam criadas", ["Moderno",":rainbow[Divertido]","Criativo","Clássico"], captions=["Para sistemas corporativos","Para sistemas infantis","Para sistemas fora do comum","Para sistemas bibliotecarios"],)

st.title("ColoreAI")
st.text("IA com foco na geração de paletas de cores modernas para a criação de sistemas web.")

prompt = st.chat_input("Pergunte Algo")
if prompt:
  st.chat_message("user").write(prompt)

  model = ChatGoogleGenerativeAI(
    model=gemini_version,
    temperature=1.0,
    max_tokens=None,
    timeout=None,
  )

  messages = [(
    "system",
    f"Você é um designer especialista em teoria das cores e padrões modernos de design para sistemas digitais. Sua função é criar paletas de cores coerentes, acessíveis e alinhadas com tendências atuais, além de explicar de forma clara e prática como aplicá-las em projetos de desenvolvimento web (UI/UX). Forneça sugestões objetivas, com foco em usabilidade, hierarquia visual e consistência. Sempre analise e interprete o briefing do usuário, quando fornecido, para adaptar as escolhas de cores ao contexto, público-alvo, propósito do produto e identidade desejada. Considere o estilo selecionado pelo usuário: {estilo}. As opções possíveis são: Divertido, Moderno, Criativo ou Clássico. Adapte automaticamente a paleta de cores e as recomendações com base nesse valor. Seja direto, conciso e evite formatação em markdown. Sempre responda em português brasileiro."
  ),
  ("human", prompt)]

  ai_msg = model.invoke(messages)

  st.chat_message("assistant").write(ai_msg.content)