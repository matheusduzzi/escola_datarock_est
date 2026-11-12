"""A sua função do exercício da aula «Intervalo para proporção».

Troque o raise pelo seu código e rode:  python3 conferir.py
"""
import math


def proporcao_da_coluna(valores, limite, z=1.96):
    """Parte das entregas que chegou até o limite, com a faixa de Wilson de 95%.

    valores: a coluna como veio do CSV, com textos, células vazias ("" ou só espaços) e None.
    limite: o prazo em horas. "Até 48 horas" inclui a entrega de 48 horas cravadas.
    z: 1,96 para 95%.

    Retorna um dicionário com:
      ate       o numerador: quantos valores com número ficaram até o limite
      n         o denominador: quantos valores têm número
      vazias    quantos estão vazios (não entram em ate nem em n)
      p         ate / n
      inferior  o começo da faixa de Wilson
      superior  o fim da faixa de Wilson

    Com nenhum valor com número, levanta ValueError.
    Não muda a lista que recebeu.
    """
    raise NotImplementedError("escreva a função")
