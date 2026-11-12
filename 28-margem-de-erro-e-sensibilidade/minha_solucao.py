"""As suas funções do exercício da aula «Margem de erro e sensibilidade».

Troque cada raise pelo seu código e rode:  python3 conferir.py
"""
import math
from statistics import NormalDist


def margem(desvio, n, confianca=0.95):
    """Margem de erro da média: z × desvio ÷ √n.

    desvio: o desvio padrão das horas (ou √(p(1 − p)) para uma proporção).
    n: quantas entregas têm número.
    confianca: o nível, entre 0 e 1 (0.95 para 95%).
    O z sai de NormalDist().inv_cdf(0.5 + confianca / 2), como na seção 2 da aula.

    Levanta ValueError com desvio negativo, n menor que 1 ou confiança fora de 0 a 1.
    """
    raise NotImplementedError("escreva a função margem")


def n_para_margem(desvio, alvo, confianca=0.95):
    """Quantas entregas são precisas para a margem ficar em alvo: (z × desvio ÷ alvo)².

    Retorna um inteiro, arredondado para cima, e pelo menos 1.
    Levanta ValueError com desvio negativo, alvo zero ou negativo, ou confiança fora de 0 a 1.
    """
    raise NotImplementedError("escreva a função n_para_margem")
