# 🤖 Alura Agent: Assistente de Inteligência Artificial para Análise de Dados

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
![Oracle Cloud](https://img.shields.io/badge/Oracle_Cloud-OCI-F80000)

Este repositório contém a entrega final para o desafio **Challenge Alura Agente**. O projeto é uma aplicação interativa com interface web que utiliza Inteligência Artificial (Google Gemini) e a biblioteca LangChain para permitir que os usuários façam perguntas em linguagem natural sobre uma base de dados estruturada.

O projeto tem como base a análise de um conjunto de dados sobre tempo de tela e saúde mental (`bdi_and_screen_items.csv`), demonstrando a capacidade da IA de atuar como um analista de dados automatizado.

---

## 🔄 Fluxo de Desenvolvimento e Commits

O desenvolvimento deste projeto seguiu uma abordagem estruturada focada em prototipagem e deploy:

1. **Fase de Prototipagem (Google Colab):** Toda a ideação inicial, testes de integração com a API do Google Gemini, validação do LangChain e leitura do DataFrame foram realizados iterativamente em um notebook do Google Colab.
2. **Consolidação (Interface Web):** Após a validação de que o agente respondia corretamente aos comandos, o código final foi exportado e consolidado no script principal (`app.py`), em conjunto com a construção da interface gráfica usando Streamlit.
   _Nota: Devido a essa transição de um ambiente de notebook para os arquivos estáticos, o histórico de commits deste repositório reflete as etapas de versionamento do código já consolidado, o setup das dependências e os ajustes de deploy._

---

## ☁️ Arquitetura da Solução e Deploy em Nuvem

> **Aviso de Desativação:** O deploy desta aplicação foi realizado com sucesso em um servidor de produção (Ubuntu 22.04) provisionado na **Oracle Cloud Infrastructure (OCI)**. A aplicação esteve ativa e acessível publicamente através da URL **`http://150.230.82.222:8501`**. Após a validação técnica, testes de firewall e captura das demonstrações para este portfólio, a instância foi intencionalmente desligada e destruída para evitar o consumo ocioso de recursos na nuvem.

A arquitetura da solução englobou:

- Provisionamento de uma VM (Compute Instance) no nível _Always Free_ da OCI.
- Transferência segura de dados locais para o servidor em nuvem utilizando SCP.
- Configuração de regras de rede (Ingress Rules) na VCN da Oracle e liberação de portas no firewall interno do Ubuntu (`iptables`) para acesso público ao tráfego TCP na porta 8501.

---

## 💬 Exemplos de Uso (Perguntas e Respostas)

O agente atua como um assistente de análise de dados sobre o dataset carregado. Abaixo estão exemplos de interações reais que o agente consegue realizar:

**Exemplo 1: Exploração da Base de Dados**

- **Usuário:** _"Quantas linhas e colunas existem na nossa base de dados atual?"_
- **Agente:** _"O conjunto de dados possui 314 linhas e 15 colunas."_

**Exemplo 2: Análise Estatística Descritiva**

- **Usuário:** _"Qual é a média de horas de tempo de tela entre os participantes da pesquisa?"_
- **Agente:** _"A média de tempo de tela diário registrado pelos participantes é de aproximadamente 5,2 horas."_

**Exemplo 3: Cruzamento de Dados e Tendências**

- **Usuário:** _"Existe alguma correlação evidente entre o alto tempo de uso de telas e pontuações mais altas no índice BDI nos dados fornecidos?"_
- **Agente:** _"Sim, ao analisar a correlação entre as métricas de tempo de tela e as pontuações BDI no arquivo fornecido, observa-se uma correlação positiva moderada. Isso sugere que usuários com maior tempo de exposição a telas tendem a apresentar pontuações ligeiramente maiores no questionário BDI."_

---

## 📸 Demonstração do Projeto

Abaixo estão os registros do funcionamento e da infraestrutura do projeto operando em nuvem durante a sua janela de ativação:

### 1. Interface Web (Deploy no Ar)

A interface da aplicação rodando com sucesso no IP público do servidor na nuvem, pronta para receber a chave da API e interagir com o usuário.
![Site no Ar](source/site-ar.png)

### 2. Infraestrutura na Oracle Cloud (OCI)

Painel de controle da Oracle Cloud comprovando a criação e operação da máquina virtual (Instance) associada ao IP público.
![Painel Oracle Cloud](source/cloud-oracle.png)

### 3. Acesso e Configuração via Terminal (SSH)

Registro da conexão remota segura via SSH, instalação do ambiente Python (`pip`) e inicialização bem-sucedida do servidor Streamlit.
![Acesso Terminal](source/terminal.png)

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

- **Python:** Linguagem base de todo o ecossistema.
- **Google Colab:** Ambiente de desenvolvimento para prototipagem do agente.
- **Streamlit:** Framework utilizado para a construção e deploy da interface gráfica (UI).
- **LangChain & LangChain Experimental:** Orquestradores utilizados para integrar a base de dados com a IA (utilizando a funcionalidade `create_pandas_dataframe_agent`).
- **Google Gemini (`gemini-1.5-flash`):** LLM (Large Language Model) fornecido via Google AI Studio atuando como o motor lógico da aplicação.
- **Pandas & Tabulate:** Bibliotecas utilizadas para a leitura estruturada do arquivo CSV e conversão dos dados de saída para formatos legíveis pela interface.
- **Oracle Cloud Infrastructure (OCI):** Provedor de computação em nuvem onde a arquitetura foi hospedada.

---

## 📁 Estrutura do Repositório

```text
├── source/                      # Diretório de imagens para a documentação
│   ├── cloud-oracle.png
│   ├── site-ar.png
│   └── terminal.png
├── app.py                       # Código-fonte principal da aplicação Streamlit
├── bdi_and_screen_items.csv     # Base de dados utilizada pelo Agente
├── requirements.txt             # Lista de dependências e bibliotecas Python
└── README.md                    # Documentação do projeto

---

## 🚀 Como Executar Localmente

Se desejar clonar e rodar este projeto na sua própria máquina, siga os passos abaixo:

1. Clone o repositório:

git clone https://github.com/Pablobrek-bit/alura-agent-server
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
python -m streamlit run app.py
```

4. Acesse no navegador:

O Streamlit abrirá automaticamente, mas você também pode acessar manualmente via http://localhost:8501 . Nota: É necessário possuir uma chave ativa do Google AI Studio para interagir com o agente.

Projeto desenvolvido por Pablo Henrique da Silva Andrade como parte dos desafios e aprendizados propostos na Imersão ONE (Oracle Next Education).
