"""Gera os quatro arquivos dessa aula. Abra só depois de fazer a aula e o exercício.

carrinho.csv: o mesmo arquivo da aula «Aplicar ANOVA e interpretar limites». As quatro semanas do
  teste da faixa de frete do Rafa. Cada cliente que chega ao carrinho é sorteado uma vez para uma das
  três versões e fica nela. Valor do pedido: lognormal. Sem faixa, mediana R$ 140 e espalhamento
  0,40. Faixa de R$ 199, mediana R$ 160 e espalhamento 0,55. Faixa de R$ 149, mediana R$ 152 e
  espalhamento 0,50. Sábado e domingo, os pedidos são 12% maiores. No dia 19, um cliente novo da
  faixa de R$ 149 fez um pedido de R$ 2.380,00.
notas_chat.csv: o teste da Carla. Cada cliente sorteado para a mensagem antiga ou a nova, e a nota
  do atendimento de 1 a 5. Antiga: 8%, 12%, 25%, 35% e 20% para as notas 1 a 5. Nova: 5%, 8%, 22%,
  37% e 28%.
entregas_regiao.csv: entregas de um mês, capital e interior. Ninguém sorteou a região: ela é onde o
  cliente mora. Capital: horas normais, média 34 e desvio 7. Interior: lognormal, mediana 30 horas e
  espalhamento 0,6 (média perto de 36, cauda longa). Nenhuma entrega abaixo de 6 horas.
leitor_separacao.csv: o teste do Bruno. 12 separadores, cada um fez um turno com a lista no papel e um
  com o leitor de código de barras, em ordem sorteada. Minutos médios por pedido. Cada separador tem o
  seu ritmo (média 6, desvio 1,5); o leitor poupa em média 0,5 minuto, variando de pessoa para pessoa.
"""
import csv
import math
import random
import sys
from pathlib import Path

SEMENTE_CARRINHO = 3535
SEMENTE_NOTAS = 13
SEMENTE_ENTREGAS = 252
SEMENTE_LEITOR = 2
DIAS = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
VERSOES = {"sem_faixa": (140, 0.40), "faixa_199": (160, 0.55), "faixa_149": (152, 0.50)}


def carrinho(semente):
    rng = random.Random(semente)
    linhas, versao_do, clientes = [], {}, []
    pid = 0
    for dia in range(1, 29):
        dia_semana = DIAS[(dia - 1) % 7]
        fator = 1.12 if dia_semana in ("sab", "dom") else 1.0
        for _ in range(rng.randint(30, 38)):
            pid += 1
            if clientes and rng.random() < 0.15:
                cliente = rng.choice(clientes)
                if rng.random() < 0.12:
                    versao_do[cliente] = rng.choice(list(VERSOES))
            else:
                cliente = f"C{len(clientes) + 1:04d}"
                clientes.append(cliente)
                versao_do[cliente] = rng.choice(list(VERSOES))
            v = versao_do[cliente]
            mediana, espalhamento = VERSOES[v]
            valor = fator * math.exp(rng.gauss(math.log(mediana), espalhamento))
            if dia == 19 and v == "faixa_149" and not any(l["valor"] == "2380.00" for l in linhas) \
                    and cliente == clientes[-1]:
                valor = 2380.0
            linhas.append({"pedido": pid, "cliente": cliente, "semana": (dia - 1) // 7 + 1, "dia": dia,
                           "dia_semana": dia_semana, "versao": v, "valor": f"{valor:.2f}"})
    return linhas


def notas(semente):
    rng = random.Random(semente)
    pesos = {"antiga": [0.08, 0.12, 0.25, 0.35, 0.20], "nova": [0.05, 0.08, 0.22, 0.37, 0.28]}
    linhas = []
    for i in range(1, 301):
        mensagem = rng.choice(["antiga", "nova"])
        linhas.append({"cliente": f"K{i:04d}", "mensagem": mensagem,
                       "nota": rng.choices([1, 2, 3, 4, 5], pesos[mensagem])[0]})
    return linhas


def entregas(semente):
    rng = random.Random(semente)
    linhas = []
    for i in range(1, 205):
        regiao = "interior" if rng.random() < 24 / 204 else "capital"
        h = rng.gauss(34, 7) if regiao == "capital" else math.exp(rng.gauss(math.log(30), 0.6))
        linhas.append({"entrega": i, "regiao": regiao, "horas": round(max(h, 6.0), 1)})
    return linhas


def leitor(semente):
    rng = random.Random(semente)
    linhas = []
    for i in range(1, 13):
        ritmo = rng.gauss(6.0, 1.5)
        ganho = rng.gauss(0.5, 0.35)
        primeiro = rng.choice(["papel", "leitor"])
        papel = ritmo + rng.gauss(0, 0.15)
        com_leitor = ritmo - ganho + rng.gauss(0, 0.15)
        linhas.append({"separador": f"S{i:02d}", "primeiro": primeiro,
                       "papel": round(papel, 2), "leitor": round(com_leitor, 2)})
    return linhas


def gravar(pasta, tabelas):
    for nome, linhas in tabelas.items():
        with open(Path(pasta) / nome, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas[0]))
            w.writeheader()
            w.writerows(linhas)


if __name__ == "__main__":
    pasta = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent
    tabelas = {"carrinho.csv": carrinho(SEMENTE_CARRINHO), "notas_chat.csv": notas(SEMENTE_NOTAS),
               "entregas_regiao.csv": entregas(SEMENTE_ENTREGAS), "leitor_separacao.csv": leitor(SEMENTE_LEITOR)}
    gravar(pasta, tabelas)
    print(" ".join(f"{nome[:-4]}={len(linhas)}" for nome, linhas in tabelas.items()))
