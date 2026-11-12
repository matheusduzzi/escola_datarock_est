"""Gera o arquivo de dados do exercício da aula «Intervalo para média de entregas».

Só biblioteca padrão. Sai igual toda vez:

    python3 gerar_dados.py

entregas_abril.csv: 60 entregas sorteadas entre as entregas de abril da Loja Exemplo.
    40 são da capital e 20 do interior, em ordem sorteada.
    As horas da capital vêm de uma curva normal com média 44 h e desvio padrão 7 h.
    As do interior, de uma curva normal com média 54 h e desvio padrão 9 h.
    Tudo arredondado a 0,1 h.
    Depois, 7 entregas do interior e 1 da capital, sorteadas dentro de cada região,
    ficam com a célula de horas vazia: a baixa não foi anotada.

As 48 entregas de março que a aula usa ficam em ../dados/loja/entregas.csv e saem do gerador
daquela pasta.

Os sorteios usam só rng.random() e rng.shuffle()/rng.sample() de random.Random, com o mesmo número inicial.
"""
import csv
import random
from pathlib import Path
from statistics import NormalDist

PASTA = Path(__file__).resolve().parent

rng = random.Random(2623)
regioes = ["capital"] * 40 + ["interior"] * 20
rng.shuffle(regioes)
curvas = {"capital": NormalDist(44, 7), "interior": NormalDist(54, 9)}
linhas = [[i, r, round(curvas[r].inv_cdf(rng.random()), 1)] for i, r in enumerate(regioes, 1)]
capital = [i for i, r in enumerate(regioes) if r == "capital"]
interior = [i for i, r in enumerate(regioes) if r == "interior"]
for i in rng.sample(interior, 7) + rng.sample(capital, 1):
    linhas[i][2] = ""

with open(PASTA / "entregas_abril.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["id_entrega", "regiao", "horas"])
    w.writerows(linhas)

vazias = sum(1 for l in linhas if l[2] == "")
print(f"abril={len(linhas)} capital={len(capital)} interior={len(interior)} sem_baixa={vazias}")
