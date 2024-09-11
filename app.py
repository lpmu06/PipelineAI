import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError

def main():
    st.title("Sistema de CRM e Vendas")
    email = st.text_input("Email")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))
    valor = st.number_input("Valor da compra", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto = st.selectbox("Produto", options=["Camiseta", "Calça", "Sapato", "Bolsa", "Relógio"])

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(email=email,
                            data=data_hora,
                            valor=valor,
                            quantidade=quantidade,
                            produto=produto)
            st.success("Venda salva com sucesso!")
            st.write(venda)
        except ValidationError as e:
            st.error(f"Erro: {e}")




if __name__ == "__main__":
    main()