"""Gera os tíquetes e as entregas da Loja Exemplo usados em Estatística para decisão.

Só biblioteca padrão (Python 3.9 ou mais novo). Semente fixa: rodar duas vezes dá os mesmos
arquivos, byte a byte.

    python3 gerar.py                 # escreve nesta pasta
    python3 gerar.py --saida /tmp/x  # escreve em outra pasta

Como os números nascem:
- tiquetes.csv: valor de cada pedido sorteado de uma distribuição log-normal por canal
  (site: 240 pedidos, mediana R$ 120,00; loja física: 160 pedidos, mediana R$ 85,00).
  O pedido 117 é trocado por uma compra corporativa de R$ 38.400,00 no site.
- entregas.csv: horas do pedido até a baixa da entrega, sorteadas de uma normal com média 46 h
  e desvio 9 h; 3 entregas ficam sem a hora de baixa (célula vazia).

A sequência de sorteios é a mesma do gerador anterior do curso, então os dois CSVs saem iguais
aos que as aulas antigas usavam.
"""
import argparse
import csv
import math
import pathlib
import random

SEED = 42

CANAIS = [("site", 240, 120.0, 0.35), ("loja_fisica", 160, 85.0, 0.30)]
PEDIDO_EXTREMO = 38400.00
ID_EXTREMO = 117

N_ENTREGAS = 48
HORAS_MEDIA, HORAS_DP = 46.0, 9.0
N_ENTREGA_SEM_BAIXA = 3


def gerar_tiquetes(rng):
    linhas = []
    for canal, n, mediana, espalhamento in CANAIS:
        for _ in range(n):
            valor = round(math.exp(rng.gauss(math.log(mediana), espalhamento)), 2)
            linhas.append([canal, valor])
    rng.shuffle(linhas)
    linhas = [[i + 1] + l for i, l in enumerate(linhas)]
    linhas[ID_EXTREMO - 1] = [ID_EXTREMO, "site", PEDIDO_EXTREMO]
    return linhas


def gerar_entregas(rng):
    linhas = [[i + 1, round(rng.gauss(HORAS_MEDIA, HORAS_DP), 1)] for i in range(N_ENTREGAS)]
    for i in rng.sample(range(N_ENTREGAS), N_ENTREGA_SEM_BAIXA):
        linhas[i][1] = ""
    return linhas


def escrever(caminho, cabecalho, linhas):
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(cabecalho)
        w.writerows(linhas)


def gerar(saida):
    rng = random.Random(SEED)
    saida.mkdir(parents=True, exist_ok=True)
    tiquetes = gerar_tiquetes(rng)
    entregas = gerar_entregas(rng)
    escrever(saida / "tiquetes.csv", ["id_pedido", "canal", "valor"], tiquetes)
    escrever(saida / "entregas.csv", ["id_entrega", "horas"], entregas)
    return {"tiquetes": len(tiquetes), "entregas": len(entregas), "entregas_sem_baixa": N_ENTREGA_SEM_BAIXA}


def main():
    parser = argparse.ArgumentParser(description="Gera tiquetes.csv e entregas.csv da Loja Exemplo.")
    parser.add_argument("--saida", default=str(pathlib.Path(__file__).resolve().parent))
    resumo = gerar(pathlib.Path(parser.parse_args().saida))
    print(" ".join("%s=%s" % (k, v) for k, v in resumo.items()))


if __name__ == "__main__":
    main()
