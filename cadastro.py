#!/usr/bin/env python3
"""Cadastro de produto

variaveis serao reescritas em forma de dicionario 
produto_nome = "Caneta"
produto_cor1 = "azul"
produto_cor2 = "branco"
produto_preco = 3.23
produto_dimensao_altura = 12.1
produto_dimensao_largura = 12.1
produto_em_estoque = True
produto_codigo = 45678
produto_codecar = None

"""
__version__ =  "0.1.0"
#import pprint
from pprint import pprint

#dicionario 1
"""
produto = {
    "nome" : "Caneta",
    "cor1" : "azul",
    "cor2" : "branco",
    "preco" : 3.23,
    "dimensao_altura" : 12.1,
    "dimensao_largura" : 0.8 ,
    "em_estoque" : True,
    "codigo" : 45678,
    "codecar" : None,
    
}
"""
#dicionario 2
produto = {
    "nome" : "Caneta",
    "cores" : ["azul", "branco"],
    "preco" : 3.23,
    "dimensao" : {
                    "altura" : 12.1 ,
                     "largura" : 0.8,
                     },
    "em_estoque" : True,
    "codigo" : 45678,
    "codecar" : None,
    
}

cliente = {
    "nome": "Thiago"
}

compra = {
    "cliente" : cliente,
    "produto" : produto,
    "quantidade" : 3
}

#pprint.pprint(compra)

#pprint(compra)
"""
total_compra = compra[2] * produto["preco"]

print(
    f"O cliente {compra[0]} comprou {compra[1]}"
    f" e pagou o total de {total_compra}"
)
"""
total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou a quantidade {compra['quantidade']} do"
    f" produto {compra['produto']['nome']}" 
    f" e pagou o valor total de {total_compra}"
)

