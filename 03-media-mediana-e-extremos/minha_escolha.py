"""Exercício da aula «Média, mediana e extremos»: a função que escolhe a medida de centro.

Rode de dentro da pasta dessa aula:  python3 minha_escolha.py

Escreva a função resumo_centro do jeito que o exercício pede. Embaixo, o programa chama a função
com os pedidos do site. Acrescente as chamadas das tarefas 2 e 3 depois dela.
"""
from pathlib import Path

import pandas as pd

DADOS = Path("../dados/loja/tiquetes.csv")


def resumo_centro(valores, pergunta):
    """Retorna n, media, mediana, desvio_padrao, distancia, medida_escolhida e valor_escolhido.

    pergunta: "tipico" ou "total". Outro texto, ou nenhum valor, para com ValueError.
    """
    raise NotImplementedError("escreva a função resumo_centro")


def mostrar(nome, resultado):
    print(nome, {k: round(x, 2) if isinstance(x, float) else x for k, x in resultado.items()})


if __name__ == "__main__":
    tiquetes = pd.read_csv(DADOS)
    site = tiquetes[tiquetes["canal"] == "site"]["valor"]
    mostrar("site, tipico:", resumo_centro(site, "tipico"))
