"""Gera as duas tabelas da aula «Investigar associações».

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

SEED = 909


def valor(rng, centro, espalhamento):
    return round(centro * math.exp(rng.gauss(0, espalhamento)), 2)


def pedidos(rng):
    linhas = []
    for canal, n, km_min, km_max, centro in [("app", 72, 1, 12, 85), ("site", 58, 3, 35, 165),
                                             ("empresas", 19, 25, 70, 520)]:
        for _ in range(n):
            linhas.append({"canal": canal, "distancia_km": round(rng.uniform(km_min, km_max), 1),
                           "valor": valor(rng, centro, 0.35)})
    rng.shuffle(linhas)
    linhas.append({"canal": "empresas", "distancia_km": 94.0, "valor": 7480.00})
    saida = []
    for i, l in enumerate(linhas, start=1001):
        saida.append({"id_pedido": i, "canal": l["canal"], "distancia_km": f"{l['distancia_km']:.1f}",
                      "valor": f"{l['valor']:.2f}"})
    return saida


def entregas(rng):
    linhas = []
    for _ in range(61):
        cx, km = rng.randint(1, 5), round(rng.uniform(2, 40), 1)
        linhas.append({"modalidade": "normal", "volumes": cx, "distancia_km": km,
                       "horas": 30 + 1.5 * cx + 0.3 * km + rng.gauss(0, 4)})
    for _ in range(28):
        cx, km = rng.randint(4, 12), round(rng.uniform(2, 40), 1)
        linhas.append({"modalidade": "expressa", "volumes": cx, "distancia_km": km,
                       "horas": 6 + 0.8 * cx + 0.15 * km + rng.gauss(0, 2)})
    rng.shuffle(linhas)
    linhas.insert(57, {"modalidade": "normal", "volumes": 2, "distancia_km": 11.4, "horas": 196.0})
    saida = []
    for i, l in enumerate(linhas, start=1):
        saida.append({"id_entrega": i, "modalidade": l["modalidade"], "volumes": l["volumes"],
                      "distancia_km": f"{l['distancia_km']:.1f}", "horas": f"{max(1.0, l['horas']):.1f}"})
    return saida


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
    a, b = pedidos(rng), entregas(rng)
    escrever(pasta / "pedidos_setembro.csv", a)
    escrever(pasta / "entregas_maio.csv", b)
    print(f"pedidos_setembro={len(a)} entregas_maio={len(b)}")


if __name__ == "__main__":
    main()
