"""Gera os dois arquivos dessa aula. Abra só depois de fazer a aula e o exercício.

carrinho_divisorias.csv: o teste do Bruno no depósito. 24 separadores, cada um fez um turno com o
  carrinho comum e um com o carrinho com divisórias. A ordem foi sorteada: 12 começaram por cada
  carrinho. Minutos médios por pedido em cada turno. Cada separador tem o seu ritmo (média 10,
  desvio 2). O quanto as divisórias poupam muda de pessoa para pessoa e tem cauda para a direita:
  exp(normal(log 0,35; 0,9)) menos 0,05 minuto, com média perto de 0,47. Cada turno tem um ruído
  normal de desvio 0,3. O segundo turno sai 0,25 minuto mais rápido, pelo treino. O S17 começou
  pelas divisórias, se perdeu no primeiro dia e perdeu 1,6 minuto por pedido.
chat_triagem.csv: o teste da Carla no atendimento. 320 chats. Cada cliente novo é sorteado para a
  triagem antiga ou a nova e fica nela; 12% dos chats são de um cliente que já tinha aberto um.
  Minutos até a primeira resposta de uma pessoa. Antiga: exp(normal(log 6; 0,6)). Nova:
  exp(normal(log 4,6; 0,7)), e em 2% dos chats da nova a triagem trava e a espera fica entre 55 e
  95 minutos.
"""
import csv
import math
import random
import sys
from pathlib import Path

SEMENTE_CARRINHO = 21764
SEMENTE_CHAT = 42


def carrinho(semente):
    rng = random.Random(semente)
    ids = [f"S{i:02d}" for i in range(1, 25)]
    ordens = ["comum_primeiro"] * 12 + ["divisorias_primeiro"] * 12
    rng.shuffle(ordens)
    linhas = []
    for s, ordem in zip(ids, ordens):
        ritmo = rng.gauss(10, 2)
        ganho = math.exp(rng.gauss(math.log(0.35), 0.9)) - 0.05
        if s == "S17":
            ganho = -1.6
            ordem = "divisorias_primeiro"
        comum = ritmo + rng.gauss(0, 0.3)
        divisorias = ritmo - ganho + rng.gauss(0, 0.3)
        if ordem == "comum_primeiro":
            divisorias -= 0.25
        else:
            comum -= 0.25
        linhas.append({"separador": s, "ordem": ordem, "comum_min": f"{comum:.2f}",
                       "divisorias_min": f"{divisorias:.2f}"})
    return linhas


def chat(semente):
    rng = random.Random(semente)
    linhas, versao, clientes = [], {}, []
    for i in range(1, 321):
        if clientes and rng.random() < 0.12:
            cliente = rng.choice(clientes)
        else:
            cliente = f"K{len(clientes) + 1:03d}"
            clientes.append(cliente)
            versao[cliente] = rng.choice(["antiga", "nova"])
        v = versao[cliente]
        if v == "antiga":
            minutos = math.exp(rng.gauss(math.log(6.0), 0.6))
        else:
            minutos = math.exp(rng.gauss(math.log(4.6), 0.7))
            if rng.random() < 0.02:
                minutos = rng.uniform(55, 95)
        linhas.append({"chat": f"T{i:04d}", "cliente": cliente, "triagem": v, "minutos": f"{minutos:.1f}"})
    return linhas


def salvar(nome, linhas):
    with open(nome, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)


if __name__ == "__main__":
    pasta = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
    c, t = carrinho(SEMENTE_CARRINHO), chat(SEMENTE_CHAT)
    salvar(pasta / "carrinho_divisorias.csv", c)
    salvar(pasta / "chat_triagem.csv", t)
    print(f"carrinho_divisorias={len(c)} chat_triagem={len(t)}")
