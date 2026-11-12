"""A sua função do exercício da aula «Comparar médias independentes e pareadas».

Troque o raise pelo seu código e rode:  python3 conferir.py
"""
import math
from statistics import mean, stdev

from distribuicao_t import t_critico


def comparar_pareadas(linhas, coluna_a, coluna_b, nivel=0.95):
    """Faixa t da diferença média entre dois lados de cada par, e o tamanho do efeito.

    linhas: lista de dicionários, como sai do csv.DictReader. Cada linha é um par.
    coluna_a, coluna_b: os nomes das duas colunas. A diferença é a menos b.
      Os valores chegam como texto. Célula vazia, só com espaços ou None não tem número.
    nivel: 0.95 para a faixa de 95%.

    Um par com um dos lados sem número sai inteiro da conta, dos dois lados.

    Retorna um dicionário com:
      n          quantos pares completos entraram
      diferenca  a média das diferenças a menos b
      baixo      o começo da faixa t
      alto       o fim da faixa t
      gl         os graus de liberdade (n menos 1)
      dz         a diferença média dividida pelo desvio das diferenças
      dav        a diferença média dividida pela média dos desvios de a e de b, nos pares completos

    Com menos de 2 pares completos, levanta ValueError.
    Não muda a lista que recebeu.
    """
    raise NotImplementedError("escreva a função")
