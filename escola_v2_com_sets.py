#!/usr/bin/env python3
""" Exibe relatorio de criancas por atividade

Imprimir a lista de criancas agrupadas por sala
que frequentam cada uma das atividades
"""

__version__ = "0.1.1"

#Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca  = ["Gustavo", "Sofia", "Joana", "Antonio"]



#segunda alternativa de solucao

#sets

atividades = [("Ingles", aula_ingles),
              ("Musica",aula_musica) ,
              ("Danca", aula_danca),
]

for nome_atividade,  atividade in atividades: 

    #sala2 intersecao com a atividade
    atividade_sala1 = set(sala1).intersection(set(atividade))
    atividade_sala2 = set(sala2)&set(atividade)
   

    print("-" * 30)        
    print(f"A {nome_atividade} sala 1: {atividade_sala1}")
    print("A", nome_atividade,"sala 2:" , atividade_sala2)
    print("-" * 30)


























