import streamlit as st
import contrato
from datetime import datetime, time


def main():
    st.title("Sistema de CRM e Vendas")
    email = st.text_input("Email")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))
    valor = st.number_input("Valor da compra", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["Camiseta", "Calça", "Sapato", "Bolsa", "Relógio"])
"""
    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
"""



if __name__ == "__main__":
    main()