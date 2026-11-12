"""As contas da sua banca dos refeitórios. É o comando que a sua nota final cita.

    python3 minha_banca.py

Ele já refaz o número do relatório da Bia, com as funções do relatorio_refeitorios.py,
que é o mesmo arquivo da aula 40. Escreva as suas contas embaixo de cada TAREFA.
"""
from itertools import combinations

import pandas as pd

from relatorio_refeitorios import SORTEADOS, diferenca, intervalo, mudanca_por_refeitorio

b = pd.read_csv("dados/bandejas.csv").merge(pd.read_csv("dados/refeitorios.csv"), on="refeitorio")
mudanca = mudanca_por_refeitorio(b)
d, baixo, alto = intervalo(mudanca[SORTEADOS], mudanca.drop(SORTEADOS))
print(f"relatório da Bia: {d:.1f} g, de {baixo:.1f} a {alto:.1f} g")


def decidir(inferior, superior, limite):
    if inferior >= limite:
        return "sim"
    if superior < limite:
        return "não"
    return "inconclusivo"


# TAREFA 2a. O limite de 12 g e os dois limites em que a decisão vira.

# TAREFA 2b. A conta sem o refeitório A. E depois sem cada um dos seis, um por vez.
# Dica: com 5 refeitórios, combinations(m.index, 2) dá as divisões possíveis de 2 sorteados.
