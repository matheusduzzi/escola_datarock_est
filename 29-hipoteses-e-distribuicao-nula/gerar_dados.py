"""Gera os dois arquivos dessa aula, iguais toda vez.

entregas_junho.csv: o piloto de junho da Dani. 60 entregas da capital. Um sorteio escolheu
30 para a transportadora nova; as outras 30 ficaram com a atual. Os tempos da atual saem de uma
normal com média 42 horas e desvio 5; os da nova, de uma normal com média 40 e desvio 5.
Arredondados em 0,1 hora. Numa loja de verdade, ninguém sabe essas médias: é o que o teste tenta
dizer.

coletas_dezembro.csv: o piloto do Bruno, do exercício. 80 coletas de devolução. Um sorteio
escolheu 40 para o roteiro novo; as outras 40 ficaram no atual. Horas do pedido de coleta até a
retirada, em hora cheia: normal com média 65 e desvio 10 no atual, média 62 e desvio 10 no novo.

Rodar dentro da pasta da aula:  python3 gerar_dados.py
"""
import csv
import random

rng = random.Random(2905)
ids = list(range(1, 61))
nova = set(rng.sample(ids, 30))
with open("entregas_junho.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id_entrega", "transportadora", "horas"])
    for i in ids:
        h = rng.gauss(40, 5) if i in nova else rng.gauss(42, 5)
        w.writerow([i, "nova" if i in nova else "atual", f"{h:.1f}"])

rng = random.Random(7215)
ids = list(range(1, 81))
novo = set(rng.sample(ids, 40))
with open("coletas_dezembro.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id_coleta", "roteiro", "horas"])
    for i in ids:
        h = round(rng.gauss(62, 10) if i in novo else rng.gauss(65, 10))
        w.writerow([i, "novo" if i in novo else "atual", h])

print(f"junho={len(nova) * 2} nova={len(nova)} dezembro={len(novo) * 2} novo={len(novo)}")
