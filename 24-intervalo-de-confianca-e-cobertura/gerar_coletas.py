"""Gera coletas_outubro.csv, as 40 coletas de devolução que o Bruno anotou em outubro.

Só biblioteca padrão. Sai igual toda vez:

    python3 gerar_coletas.py

Cada coleta é o tempo, em horas, entre o pedido de devolução e a chegada da transportadora.
Os tempos vêm de uma curva normal com média 50 h e desvio padrão 12 h, arredondados a 0,1 h.
O sorteio usa só rng.random(), que repete a mesma sequência em qualquer versão do Python.
"""
import csv
import random
from pathlib import Path
from statistics import NormalDist

rng = random.Random(25)
curva = NormalDist(50, 12)
horas = [round(curva.inv_cdf(rng.random()), 1) for _ in range(40)]

with open(Path(__file__).with_name("coletas_outubro.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["id_coleta", "horas"])
    w.writerows([i + 1, h] for i, h in enumerate(horas))
print(f"coletas={len(horas)} menor={min(horas)} maior={max(horas)}")
