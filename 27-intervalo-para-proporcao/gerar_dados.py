"""Gera o arquivo de dados do exercício da aula «Intervalo para proporção».

Só biblioteca padrão. Sai igual toda vez:

    python3 gerar_dados.py

entregas_maio.csv: 90 entregas sorteadas entre as entregas de maio da Loja Exemplo.
    60 são da capital e 30 do interior, em ordem sorteada.
    As horas da capital vêm de uma curva normal com média 41 h e desvio padrão 7 h.
    As do interior, de uma curva normal com média 58 h e desvio padrão 7 h.
    Em maio a transportadora passou a mandar a baixa em horas cheias: tudo arredondado à hora.
    Depois, 2 entregas da capital e 4 do interior, sorteadas dentro de cada região,
    ficam com a célula de horas vazia: a baixa não foi anotada.

As 48 entregas de março que a aula usa ficam em ../dados/loja/entregas.csv e saem do gerador
daquela pasta.

Os sorteios usam só rng.random(), rng.shuffle() e rng.sample() de random.Random, com o mesmo número inicial.
"""
import csv
import random
from pathlib import Path
from statistics import NormalDist

PASTA = Path(__file__).resolve().parent

rng = random.Random(2721)
regioes = ["capital"] * 60 + ["interior"] * 30
rng.shuffle(regioes)
curvas = {"capital": NormalDist(41, 7), "interior": NormalDist(58, 7)}
linhas = [[i, r, round(curvas[r].inv_cdf(rng.random()))] for i, r in enumerate(regioes, 1)]
capital = [i for i, r in enumerate(regioes) if r == "capital"]
interior = [i for i, r in enumerate(regioes) if r == "interior"]
for i in rng.sample(capital, 2) + rng.sample(interior, 4):
    linhas[i][2] = ""

with open(PASTA / "entregas_maio.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["id_entrega", "regiao", "horas"])
    w.writerows(linhas)

vazias = sum(1 for l in linhas if l[2] == "")
print(f"maio={len(linhas)} capital={len(capital)} interior={len(interior)} sem_baixa={vazias}")
