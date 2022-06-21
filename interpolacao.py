#!/usr/bin/env python3

email_tmpl="""
Ola, %(nome)s

Voce tem interessa em comprar %(produto)s?
 
Esse produto ira resolver os seus problemas
com %(texto)s

Clique agora em %(link)s
 
Apenas %(quantidade)d disponiveis! 
 
Preco promocional %(preco).2f
"""

clientes = ["Ana Paula", "Thiago", "Vera"]

for i in clientes:
    print(
    email_tmpl 
    % {"nome":i,
     "produto": "Racao que alimenta",
      "texto": "alimentacao saudavel para o seu cachorro", 
      "link": "www.melhorracao.com.br", 
      "quantidade": 10,
      "preco": 169.900})

