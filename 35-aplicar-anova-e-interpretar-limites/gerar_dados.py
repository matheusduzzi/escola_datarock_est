"""Gera os dois arquivos dessa aula. Abra só depois de fazer a aula e o exercício.

carrinho.csv: as quatro semanas do teste da faixa de frete do Rafa. Cada cliente que chega ao
  carrinho é sorteado uma vez para uma das três versões e fica nela. Uns 960 pedidos em 28 dias.
  Perto de 1 em cada 7 pedidos é de um cliente que já comprou no teste. Alguns desses clientes
  perderam o sorteio (trocaram de aparelho) e foram sorteados de novo: podem ter caído em duas versões.
  Valor do pedido: lognormal. Sem faixa, mediana R$ 140 e espalhamento 0,40. Faixa de R$ 199,
  mediana R$ 160 e espalhamento 0,55. Faixa de R$ 149, mediana R$ 152 e espalhamento 0,50.
  Sábado e domingo, os pedidos são 12% maiores, nas três versões. No dia 19, um cliente novo da
  faixa de R$ 149 fez um pedido de R$ 2.380,00 (uma empresa comprando para revender).
transportadoras.csv: o teste da Dani no interior. 23 dias, 50 entregas por dia, cada entrega
  sorteada para uma das quatro transportadoras. Horas da coleta à entrega: normal, cortada em 12 h.
  Atual: média 52, desvio 9. A: média 49, desvio 8. B: média 44, desvio 14. C: média 51, desvio 10.
  No dia 9 houve bloqueio na estrada e todas as entregas levaram 16 horas a mais.
  Chance de a entrega se perder (status extraviada, sem horas): atual 0,5%, A 0,5%, B 3%, C 0,5%.
"""
import csv
import math
import random
import sys
from pathlib import Path

SEMENTE = 3535
DIAS = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
VERSOES = {"sem_faixa": (140, 0.40), "faixa_199": (160, 0.55), "faixa_149": (152, 0.50)}
TRANSP = {"atual": (52, 9, 0.005), "A": (49, 8, 0.005), "B": (44, 14, 0.03), "C": (51, 10, 0.005)}


def gerar(semente):
    rng = random.Random(semente)
    carrinho, versao_do, clientes = [], {}, []
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
            if dia == 19 and v == "faixa_149" and not any(l["valor"] == "2380.00" for l in carrinho) \
                    and cliente == clientes[-1]:
                valor = 2380.0
            carrinho.append({"pedido": pid, "cliente": cliente, "semana": (dia - 1) // 7 + 1, "dia": dia,
                             "dia_semana": dia_semana, "versao": v, "valor": f"{valor:.2f}"})

    transportadoras = []
    eid = 0
    for dia in range(1, 24):
        for _ in range(50):
            eid += 1
            t = rng.choice(list(TRANSP))
            media, desvio, perda = TRANSP[t]
            h = max(12.0, rng.gauss(media, desvio)) + (16 if dia == 9 else 0)
            perdida = rng.random() < perda
            transportadoras.append({"entrega": eid, "dia": dia, "transportadora": t,
                                    "status": "extraviada" if perdida else "entregue",
                                    "horas": "" if perdida else f"{h:.1f}"})
    return {"carrinho.csv": carrinho, "transportadoras.csv": transportadoras}


def gravar(pasta, tabelas):
    for nome, linhas in tabelas.items():
        with open(Path(pasta) / nome, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas[0]))
            w.writeheader()
            w.writerows(linhas)


if __name__ == "__main__":
    pasta = sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parent
    tabelas = gerar(SEMENTE)
    gravar(pasta, tabelas)
    print(" ".join(f"{nome[:-4]}={len(linhas)}" for nome, linhas in tabelas.items()))
