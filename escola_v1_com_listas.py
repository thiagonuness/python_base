#!/usr/bin/env python3
""" Exibe relatorio de criancas por atividade

Imprimir a lista de criancas agrupadas por sala
que frequentam cada uma das atividades
"""

__version__ = "0.1.0"

#Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca  = ["Gustavo", "Sofia", "Joana", "Antonio"]


""" 
#Primeiro alternativa de solucao
# Listar alunos em casa atividade por sala

aula_ingles_sala1 = []
aula_ingles_sala2 = []

aula_musica_sala1 = []
aula_musica_sala2 = []

aula_danca_sala1 = []
aula_danca_sala2 = []

for aluno in aula_ingles:

    if aluno in sala1:
        aula_ingles_sala1.append(aluno) #adiciona o item aluno a lista
    elif aluno in sala2:
        aula_ingles_sala2.append(aluno)
"""     

#segunda alternativa de solucao

#tupla atividades

atividades = [("Ingles", aula_ingles),
              ("Musica",aula_musica) ,
              ("Danca", aula_danca),
]

#faz a iteracao no conjunto de listas dentro de atividade
for nome_atividade,  atividade in atividades: 
    
    atividade_sala1 = []
    atividade_sala2 = []
#checa o contedo da lista
    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print("-" * 30)        
    print(f"A {nome_atividade} sala 1: {atividade_sala1}")
    print("A", nome_atividade,"sala 2:" , atividade_sala2)
    print("-" * 30)


























