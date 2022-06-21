#!/usr/bin/env python3
""" Exibe relatorio de criancas por atividade

Imprimir a lista de criancas agrupadas por sala
que frequentam cada uma das atividades
"""

__version__ = "0.1.0"

#Dados
alunos ={
        "sala1": ["Erik", "Maia", "Gustavo", "Manuel","Sofia", "Joana"],
        "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolda"],
         }

atividades = {
        "aula_ingles" : ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
        "aula_musica" : ["Erik", "Carlos", "Maria"],
        "aula_danca"  : ["Gustavo", "Sofia", "Joana", "Antonio"]            
        }

aulas = {}

print(f"******************************")        

for key, values in atividades.items():
    tamv = len(values)
    for keya, valuesa  in alunos.items():
        print(f"-----------------")
        print(f"A {key} da {keya}")
        print(f"-----------------")
        for i in range(tamv):
            if (atividades[key][i] in alunos.get(keya)):
                 print(f"{atividades[key][i]}")   
                              
    print(f"******************************")        
















