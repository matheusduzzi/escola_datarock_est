"""Gera as duas tabelas da aula «Covariância e correlação».

Só biblioteca padrão (Python 3.9 ou mais novo). O sorteio é sempre o mesmo: rodar duas vezes dá
os mesmos arquivos, byte a byte.

    python3 gerar.py                 # escreve em dados/, ao lado deste programa
    python3 gerar.py --saida /tmp/x  # escreve em outra pasta
"""
import argparse
import csv
import math
import pathlib
import random

SEED = 808


def produtos(rng):
    linhas = []
    for i in range(1, 61):
        preco = round(15 + 585 * rng.random() ** 2, 2)
        visitas = round(4000 * math.exp(-preco / 110) * math.exp(rng.gauss(0, 0.25)))
        vendas = max(0, round(0.04 * visitas + rng.gauss(0, 8)))
        peso = round(rng.uniform(0.2, 12), 1)
        linhas.append({"id_produto": i, "preco": f"{preco:.2f}", "visitas": visitas,
                       "vendas": vendas, "peso_kg": f"{peso:.1f}"})
    return linhas


def nota_de(horas, rng):
    nota = 5 if horas <= 20 else 4 if horas <= 30 else 3 if horas <= 40 else 2 if horas <= 50 else 1
    if rng.random() < 0.15:
        nota += rng.choice([-1, 1])
    return min(5, max(1, nota))


def entregas(rng):
    linhas = []
    for i in range(1, 81):
        km = round(rng.uniform(2, 60), 1)
        hora = rng.randint(7, 19)
        horas = round(max(1.0, 8 + 0.6 * km + 0.4 * (hora - 13) ** 2 + rng.gauss(0, 3)), 1)
        volumes = rng.randint(1, 6)
        linhas.append({"id_entrega": i, "distancia_km": f"{km:.1f}", "hora_saida": hora,
                       "volumes": volumes, "horas": f"{horas:.1f}", "nota": nota_de(horas, rng)})
    return linhas


def escrever(caminho, linhas):
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(linhas)


def main():
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--saida", default=str(pathlib.Path(__file__).resolve().parent / "dados"))
    args = p.parse_args()
    pasta = pathlib.Path(args.saida)
    pasta.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SEED)
    a, b = produtos(rng), entregas(rng)
    escrever(pasta / "produtos.csv", a)
    escrever(pasta / "entregas_abril.csv", b)
    print(f"produtos={len(a)} entregas_abril={len(b)}")


if __name__ == "__main__":
    main()
