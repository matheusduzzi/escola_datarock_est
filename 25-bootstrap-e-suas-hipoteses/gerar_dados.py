"""Gera os três arquivos de dados da aula «Bootstrap e suas hipóteses».

Só biblioteca padrão. Sai igual toda vez:

    python3 gerar_dados.py

coletas_outubro.csv: as mesmas 40 coletas da aula «Intervalo de confiança e cobertura».
    Tempos de uma curva normal com média 50 h e desvio padrão 12 h, arredondados a 0,1 h.

coletas_novembro.csv: 12 dias sorteados de novembro, 10 coletas em cada dia.
    Cada dia tem um jeito próprio (chuva, trânsito, caminhão), que puxa todas as coletas do dia
    para cima ou para baixo: um desvio do dia, de uma curva normal com média 0 h e desvio 8 h.
    Cada coleta soma 50 h, o desvio do dia e um desvio próprio, de uma curva normal com média 0 h e desvio 8 h.

pedidos_turnos.csv: o exercício. 8 turnos de manhã ou de tarde sorteados em novembro, 9 pedidos em cada um.
    Cada turno tem um desvio próprio (equipe, mix de pedidos), de uma curva normal com média 0 min e desvio 3 min.
    Cada pedido soma 18,5 min, o desvio do turno e um desvio próprio, de uma curva normal com média 0 min e
    desvio 3 min, arredondado a 0,1 min.

Os sorteios usam só rng.random(), que repete a mesma sequência em qualquer versão do Python.
"""
import csv
import random
from pathlib import Path
from statistics import NormalDist

PASTA = Path(__file__).resolve().parent


def gravar(nome, cabecalho, linhas):
    with open(PASTA / nome, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(cabecalho)
        w.writerows(linhas)


# outubro: igual ao gerador da aula anterior
rng = random.Random(25)
curva = NormalDist(50, 12)
outubro = [round(curva.inv_cdf(rng.random()), 1) for _ in range(40)]
gravar("coletas_outubro.csv", ["id_coleta", "horas"], [[i + 1, h] for i, h in enumerate(outubro)])

# novembro: 12 dias, 10 coletas por dia
DIAS = ["03/11", "04/11", "06/11", "07/11", "10/11", "12/11", "13/11", "17/11", "19/11", "21/11", "24/11", "26/11"]
rng = random.Random(2511)
desvio = NormalDist(0, 8)
novembro = []
for dia in DIAS:
    do_dia = desvio.inv_cdf(rng.random())
    for _ in range(10):
        novembro.append([dia, len(novembro) + 1, round(50 + do_dia + desvio.inv_cdf(rng.random()), 1)])
gravar("coletas_novembro.csv", ["dia", "id_coleta", "horas"], novembro)

# exercício: 8 turnos, 9 pedidos por turno
TURNOS = [("03/11", "manhã"), ("05/11", "tarde"), ("06/11", "manhã"), ("11/11", "tarde"),
          ("13/11", "tarde"), ("18/11", "manhã"), ("20/11", "manhã"), ("25/11", "tarde")]
rng = random.Random(2512)
d3 = NormalDist(0, 3)
pedidos = []
for n_turno, (data, periodo) in enumerate(TURNOS, 1):
    do_turno = d3.inv_cdf(rng.random())
    for _ in range(9):
        pedidos.append([f"T{n_turno}", data, periodo, len(pedidos) + 1,
                        round(18.5 + do_turno + d3.inv_cdf(rng.random()), 1)])
gravar("pedidos_turnos.csv", ["turno", "data", "periodo", "id_pedido", "minutos"], pedidos)

print(f"outubro={len(outubro)} novembro={len(novembro)} dias={len(DIAS)} pedidos={len(pedidos)} turnos={len(TURNOS)}")
