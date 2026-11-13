"""Gera de novo os dois CSVs da aula: os carrinhos de agosto e as entregas de outubro.

Uso, de dentro da pasta da aula:  python3 gerar.py
Grava em dados/ (ou na pasta de --saida). O sorteio é sempre o mesmo, então os arquivos saem
iguais toda vez. Os pedidos de setembro vêm prontos da aula 09 e não são gerados aqui.
Só usa a biblioteca padrão do Python.
"""
import argparse
import csv
import math
import random
from pathlib import Path


def poisson(rng, media):
    limite, k, p = math.exp(-media), 0, 1.0
    while True:
        p *= rng.random()
        if p <= limite:
            return k
        k += 1


def carrinhos(rng):
    linhas = []
    for i in range(400):
        valor = round(min(900.0, max(25.0, rng.lognormvariate(math.log(130), 0.5))), 2)
        frete = round(rng.uniform(8, 45), 2)
        chance = max(0.03, min(0.95, 1.2 - 5.0 * frete / valor))
        finalizou = 1 if rng.random() < chance else 0
        linhas.append({"id_carrinho": 5001 + i, "valor_carrinho": f"{valor:.2f}",
                       "frete": f"{frete:.2f}", "finalizou": finalizou})
    return linhas


def entregas(rng):
    linhas = []
    for i in range(120):
        horas = round(max(14.0, rng.gauss(42, 13)), 1)
        nas_24h = poisson(rng, 1.4)
        depois = poisson(rng, 0.4 + max(0.0, horas - 48) / 3)
        linhas.append({"id_entrega": 7001 + i, "horas": f"{horas:.1f}",
                       "consultas_24h": nas_24h, "consultas_total": nas_24h + depois})
    return linhas


def gravar(caminho, linhas):
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=list(linhas[0]))
        escritor.writeheader()
        escritor.writerows(linhas)


def main():
    parser = argparse.ArgumentParser(description="Gera os CSVs da aula 10.")
    parser.add_argument("--saida", default="dados", help="pasta de destino (padrão: dados)")
    args = parser.parse_args()
    pasta = Path(args.saida)
    pasta.mkdir(parents=True, exist_ok=True)
    rng = random.Random(1010)
    c = carrinhos(rng)
    e = entregas(rng)
    gravar(pasta / "carrinhos_agosto.csv", c)
    gravar(pasta / "entregas_outubro.csv", e)
    print(f"carrinhos_agosto={len(c)} entregas_outubro={len(e)}")


if __name__ == "__main__":
    main()
