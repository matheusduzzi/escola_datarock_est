"""A sua função do exercício da aula «Intervalo para média de entregas».

Troque o raise pelo seu código e rode:  python3 conferir.py
"""
import statistics


def intervalo_da_coluna(valores, t):
    """Intervalo de confiança de 95% da média, pela tabela t.

    valores: a coluna como veio do CSV, com textos, células vazias ("" ou só espaços) e None.
    t: o número da tabela t para n - 1 graus de liberdade, coluna 0,975.

    Retorna um dicionário com:
      n         quantos valores têm número
      vazias    quantos estão vazios
      media     a média dos que têm número
      inferior  o começo da faixa
      superior  o fim da faixa

    Com menos de 2 valores com número, levanta ValueError.
    Não muda a lista que recebeu.
    """
    raise NotImplementedError("escreva a função")
