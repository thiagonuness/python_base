#!/usr/bin/env python
"""
Imprime a tabuada do 1 ao 10. 

---Tabuada do 1---

    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
... cont
#####################
---Tabuada do 2---

    1 x 2 = 2
    2 x 2 = 4
    3 x 2 = 6
... cont
#####################
"""

__version__ = "0.1.1"
__author__ = "Thiago"

template_base = """

---Tabuada do {n1} ---

    {bloco}

##################
"""


#numeros = [1,2,3,4,5,6,7,8,9,10]
# Iterable (objetos percorriveis)
numeros = list(range(1,11))

for n1 in numeros:
    bloco = ""
    for n2 in numeros:
        resultado = n1 * n2
        bloco = bloco + f"\n{n1} x {n2} = {resultado}"

    print(template_base.format(bloco=bloco, n1=n1))
       
