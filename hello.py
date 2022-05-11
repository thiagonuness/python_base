ls#!/usr/bin/env python3
"""
Hello World Multi Linguas

Dependendo da lingua configurada no ambiente 
o programa exibe a mensagem correnspondente

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execucao: 

    python3 hello.py 
    ou
    ./hello.py
"""
#O trecho acima sera mostrado quando em modo help
#Esse trecho fica sendo considerado como dumentacao

#Metadados - dunder(metadado)dunder -> dunder = __
__version__ = "0.0.1"
__author__ = "Thiago Nunnes"
__license__ = "Unlicense"

#todo programa python e um script python...um conjunto de comandos
#que sera interpretado pelo python
#script e um conjunto de comandos que poderiam ser execudados
#separadamente e coloca encadeado um atras do outro.
#if __name__ = "__main__" -> para identificar bloco principal

import os #biblioteca para manipular/ler variaveis do ambiente
#name convention para var = snake case -> uso de _ para separacao

current_language = os.getenv("LANG", "en_US")[:5]
#getenv le a variavel do ambiente caso exista, seta um padrao caso nao

msg = "Hello, World!"    
if current_language == "pt_BT":
    msg = "Ola Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "en_ZA":
    msg = "Sanny Bonani!"


    
print(msg) #built-in -> ja vem com a linguagem


#testando commit
