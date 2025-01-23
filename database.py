import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para salvar os dados validados no PostgreSQL
def salvar_no_postgres(dados: Vendas):
    """
    Função para salvar no postgres

    Args:
        dados (Vendas): Dados da venda
    """
    try:
        # Construct connection string
        conn_string = (
            f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
            "?sslmode=require"
        )
        
        # Print connection details (remove in production)
        st.write(f"Tentando conectar a: {DB_HOST}")
        
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        
        # Inserção dos dados na tabela de vendas
        insert_query = sql.SQL(
            "INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto.value
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Dados salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {str(e)}")
        # Print more detailed error info (remove in production)
        st.error(f"Detalhes da conexão:")
        st.error(f"Host: {DB_HOST}")
        st.error(f"Database: {DB_NAME}")
        st.error(f"User: {DB_USER}")