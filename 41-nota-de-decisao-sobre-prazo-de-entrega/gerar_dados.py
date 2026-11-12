"""Gera interior_outubro.csv, as entregas do interior em outubro, igual toda vez.

    python3 gerar_dados.py

Abra este arquivo só depois de fazer o exercício. O começo conta como cada número nasceu.

Como os tempos foram sorteados (só biblioteca padrão, random.Random(11)):
- Dias 1 a 14: 90 entregas, um carregamento por dia no depósito. Horas sorteadas de uma curva
  normal com média 84 e desvio 13, arredondadas para uma casa, nunca abaixo de 20.
- Dias 15 a 31: 110 entregas, dois carregamentos por dia. Curva normal com média 61 e desvio 8,5.
- O dia de cada entrega é sorteado por igual dentro do período, e as linhas saem em ordem de dia.
- Em cada período, algumas entregas ficam sem a hora de baixa (célula vazia): 2 antes do dia 15
  e 3 depois. Elas são escolhidas ao acaso, sem ligação com o tempo que levaram.
Hipóteses que o sorteio garante e que uma loja de verdade não sabe: as entregas não dependem umas
das outras, o tempo só muda no dia 15 e as baixas que faltam caíram ao acaso.
"""
import csv
import random
from pathlib import Path

SEMENTE = 11
PERIODOS = [
    # (quantidade, primeiro dia, último dia, média, desvio, sem baixa)
    (90, 1, 14, 84, 13, 2),
    (110, 15, 31, 61, 8.5, 3),
]


def gerar():
    rng = random.Random(SEMENTE)
    linhas = []
    for n, d0, d1, media, desvio, sem_baixa in PERIODOS:
        dias = sorted(rng.randint(d0, d1) for _ in range(n))
        horas = [round(max(20.0, rng.gauss(media, desvio)), 1) for _ in range(n)]
        for i in rng.sample(range(n), sem_baixa):
            horas[i] = ""
        linhas += list(zip(dias, horas))
    return [[i + 1, dia, h] for i, (dia, h) in enumerate(linhas)]


def main():
    linhas = gerar()
    with open(Path(__file__).resolve().parent / "interior_outubro.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["id_entrega", "dia", "horas"])
        w.writerows(linhas)
    depois = [l for l in linhas if l[1] >= 15]
    print(f"interior={len(linhas)} antes_do_dia_15={len(linhas) - len(depois)} "
          f"a_partir_do_dia_15={len(depois)} sem_baixa={sum(1 for l in linhas if l[2] == '')}")


if __name__ == "__main__":
    main()
