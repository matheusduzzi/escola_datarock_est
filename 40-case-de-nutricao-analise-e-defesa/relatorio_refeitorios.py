"""Refaz todos os números do relatório dos refeitórios da Bia, na ordem em que o relatório usa.

Rode dentro da pasta dessa aula:  python3 relatorio_refeitorios.py
Precisa do pandas e do distribuicao_t.py, que fica nesta mesma pasta.
"""
from itertools import combinations
from math import sqrt

import pandas as pd

from distribuicao_t import t_critico

SORTEADOS = ["A", "C", "D"]
LIMITE_G = 10


def mudanca_por_refeitorio(tabela):
    m = tabela.groupby(["refeitorio", "periodo"])["salada_g"].mean().unstack()
    return m["depois"] - m["antes"]


def diferenca(m, lado):
    return m[list(lado)].mean() - m.drop(list(lado)).mean()


def intervalo(a, c, nivel=0.95):
    va, vc = a.var() / len(a), c.var() / len(c)
    erro = sqrt(va + vc)
    gl = (va + vc) ** 2 / (va ** 2 / (len(a) - 1) + vc ** 2 / (len(c) - 1))
    d = a.mean() - c.mean()
    k = t_critico(nivel, gl)
    return d, d - k * erro, d + k * erro


def resumo(m):
    d, baixo, alto = intervalo(m[SORTEADOS], m.drop(SORTEADOS))
    maiores = sum(diferenca(m, lado) >= diferenca(m, SORTEADOS) for lado in combinations(m.index, 3))
    return (f"{d:.1f} g (intervalo de 95% de {baixo:.1f} a {alto:.1f} g; "
            f"{maiores} das 20 divisões com diferença igual ou maior)")


def main():
    b = pd.read_csv("dados/bandejas.csv").merge(pd.read_csv("dados/refeitorios.csv"), on="refeitorio")
    print("1. O que mudou em cada refeitório (média por bandeja, g)")
    media = b.groupby(["grupo", "refeitorio", "periodo"])["salada_g"].mean().unstack()
    media["mudanca"] = media["depois"] - media["antes"]
    print(media.round(1).to_string())
    print()
    mudanca = mudanca_por_refeitorio(b)
    print("2. Diferença entre as mudanças, salada primeiro menos ordem de sempre")
    print("   " + resumo(mudanca))
    print(f"   Limite da Bia para pagar a obra: {LIMITE_G} g")
    print()
    print("3. Sensibilidade")
    lugares = b.groupby("cracha")["refeitorio"].nunique()
    cinco = lugares[lugares > 1].index
    pessoa = b.groupby(["refeitorio", "cracha", "periodo"])["salada_g"].mean().unstack().dropna()
    versoes = {
        "sem os cinco crachás": mudanca_por_refeitorio(b[~b["cracha"].isin(cinco)]),
        "os cinco contados no A": mudanca_por_refeitorio(
            b.assign(refeitorio=b["refeitorio"].where(~b["cracha"].isin(cinco), "A"))),
        "média por pessoa": (pessoa["depois"] - pessoa["antes"]).groupby("refeitorio").mean(),
    }
    for nome, m in versoes.items():
        print(f"   {nome}: {resumo(m)}")
    print()
    print(f"Arquivos: {len(b)} bandejas, {b['cracha'].nunique()} crachás, {b['refeitorio'].nunique()} refeitórios")


if __name__ == "__main__":
    main()
