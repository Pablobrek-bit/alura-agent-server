import os
import streamlit as st
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Alura Agent - Análise de Dados", page_icon="🤖", layout="wide")
st.title("🤖 Alura Agent: Assistente de Inteligência Artificial")
st.markdown("Faça perguntas em linguagem natural sobre o conjunto de dados carregado.")

api_key = st.sidebar.text_input("Chave Google API", type="password")

if not api_key:
    st.info("Insira sua chave de API do Google AI Studio no menu lateral para iniciar.")
    st.stop()

os.environ["GOOGLE_API_KEY"] = api_key

@st.cache_data
def carregar_dados():
    return pd.read_csv("bdi_and_screen_items.csv")

try:
    df = carregar_dados()
    st.sidebar.success("Base de dados carregada com sucesso!")

    with st.expander("Visualizar primeiras linhas da base de dados"):
        st.dataframe(df.head(10))

    llm = ChatGoogleGenerativeAI(
    model="gemini-3.7-flash",
    temperature=0
)

    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=False,
        allow_dangerous_code=True
    )

    pergunta = st.text_input("Digite sua pergunta sobre os dados:", placeholder="Ex: Qual a média da coluna bdi_item_01?")

    if st.button("Enviar Pergunta"):
        if pergunta:
            with st.spinner("Analisando os dados e gerando resposta..."):
                try:
                    resposta = agent.invoke(pergunta)
                    st.success("Resposta:")
                    st.write(resposta["output"])
                except Exception as e:
                    st.error(f"Erro ao processar a requisição: {e}")
        else:
            st.warning("Por favor, digite uma pergunta antes de enviar.")

except FileNotFoundError:
    st.error("Arquivo 'bdi_and_screen_items.csv' não encontrado na raiz da aplicação.")
