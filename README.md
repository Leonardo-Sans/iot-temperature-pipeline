IoT Temperature Monitoring Pipeline

📌 Sobre o projeto



Neste projeto eu desenvolvi um pipeline de dados para monitoramento de temperatura utilizando dados simulados de sensores IoT.



O objetivo foi demonstrar o processo completo de ingestão, armazenamento, processamento e visualização de dados utilizando ferramentas modernas de engenharia de dados.



Tecnologias utilizadas:



Python

PostgreSQL

Docker

Streamlit

Pandas

SQLAlchemy

⚙️ Arquitetura do projeto



O fluxo do projeto segue as seguintes etapas:



Coleta de dados de sensores IoT a partir de um dataset CSV

Processamento e ingestão dos dados com Python

Armazenamento em banco de dados PostgreSQL executando em container Docker

Criação de views SQL para análise dos dados

Visualização das informações em um dashboard web com Streamlit

🐳 Execução do banco de dados



Para executar o banco de dados PostgreSQL foi utilizado Docker.



docker run --name postgres-iot \\

\-e POSTGRES\_PASSWORD=123456 \\

\-e POSTGRES\_USER=iotuser \\

\-e POSTGRES\_DB=iotdb \\

\-p 5432:5432 \\

\-d postgres

🚀 Execução do pipeline



Para carregar os dados no banco:



python pipeline.py



O script realiza:



leitura do dataset

tratamento dos dados

inserção no PostgreSQL

📊 Dashboard



O dashboard foi desenvolvido com Streamlit para visualização interativa das informações.



Para executar:



streamlit run dashboard.py



O sistema gera gráficos como:



temperatura média por sala

temperatura média interna vs externa

quantidade de leituras por ambiente

📷 Exemplos do sistema

Pipeline executando


![Pipeline Execution](images/pipeline_execution.png)


Banco de dados PostgreSQL


![Sql views](images/sql_views.png)


Dashboard Streamlit


![Dashboard](images/1.png)
![Dashboard](images/2.png)
![Dashboard](images/3.png)

🎯 Conclusão



Este projeto demonstra um pipeline completo de dados IoT, integrando coleta, armazenamento, análise e visualização utilizando ferramentas amplamente utilizadas no mercado de engenharia de dados.

