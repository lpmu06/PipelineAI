from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, validate_call, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    CAMISETA = "Camiseta"
    CALCA = "Calça"
    SAPATO = "Sapato"
    BOLSA = "Bolsa"
    RELOGIO = "Relógio"



class Vendas(BaseModel):
    """
    Modelo de dados para vendas

    Args:
        email (EmailStr): Email do cliente
        data (datetime): Data da venda
        valor (PositiveFloat): Valor da venda
        quantidade (PositiveInt): Quantidade de produtos vendidos
        produto (ProdutoEnum): Produto vendido
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    @classmethod
    def validate_produto(cls, v):
        if v not in ProdutoEnum:
            raise ValueError(f"Produto inválido: {v}")
        return v    

    class Config:
        validate_assignment = True
