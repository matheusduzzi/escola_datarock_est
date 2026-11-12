"""Gera separacao_novembro.csv: minutos de separação de 400 pedidos no estoque, 200 por turno.

Roda igual toda vez: usa só rng.random(), cuja sequência o Python garante entre versões.
Manhã: 6 minutos fixos mais três esperas exponenciais de média 2.
Noite: 4 minutos fixos mais duas esperas exponenciais de média 4.
Os dois turnos têm média perto de 12 minutos; a noite espalha mais.
"""
import csv
import math
import random

rng = random.Random(22)


def espera(media):
    return -media * math.log(1 - rng.random())


linhas = []
for i in range(1, 401):
    if i % 2:
        turno, minutos = "manha", 6 + espera(2) + espera(2) + espera(2)
    else:
        turno, minutos = "noite", 4 + espera(4) + espera(4)
    linhas.append({"id_pedido": i, "turno": turno, "minutos": round(minutos, 1)})

with open("separacao_novembro.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["id_pedido", "turno", "minutos"])
    w.writeheader()
    w.writerows(linhas)

print(f"pedidos={len(linhas)} menor={min(l['minutos'] for l in linhas)} maior={max(l['minutos'] for l in linhas)}")
