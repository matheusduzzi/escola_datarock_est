"""Simula dois jeitos de perder a baixa de uma entrega e mede o que acontece com a média.

Rode de dentro da pasta da aula:  python3 simular.py
                                  python3 simular.py --entregas 480

Como os números nascem:
- cada mês tem N entregas (48 por padrão), com horas sorteadas de uma normal de média 46 h
  e desvio 9 h, arredondadas a uma casa;
- "ao acaso": 3 entregas por mês (ou 1 em cada 16, se N não for 48) ficam sem baixa,
  sorteadas sem olhar as horas;
- "as demoradas": cada entrega com mais de 55 h fica sem baixa com chance de 40%;
  as outras, com chance de 2%. É o que acontece quando o atraso vira reentrega
  e a baixa da reentrega não é anotada.
O programa repete o mês 2000 vezes e sorteia sempre os mesmos números.
"""
import argparse

import numpy as np

MEDIA, DESVIO = 46.0, 9.0
DEMORA, CHANCE_DEMORA, CHANCE_OUTRAS = 55.0, 0.40, 0.02
PRAZO = 48
SEMENTE = 7


def br(x, casas=1):
    return f"{x:.{casas}f}".replace(".", ",")


def simular(n, repeticoes, rng):
    resultado = {"ao acaso": [], "as demoradas": []}
    for _ in range(repeticoes):
        horas = np.round(rng.normal(MEDIA, DESVIO, n), 1)
        real = horas.mean(), (horas > PRAZO).mean()
        acaso = np.ones(n, bool)
        acaso[rng.choice(n, size=max(1, round(n / 16)), replace=False)] = False
        chance = np.where(horas > DEMORA, CHANCE_DEMORA, CHANCE_OUTRAS)
        demoradas = rng.random(n) >= chance
        for nome, fica in [("ao acaso", acaso), ("as demoradas", demoradas)]:
            vistas = horas[fica]
            resultado[nome].append((real[0], vistas.mean(), real[1], (vistas > PRAZO).mean(), n - fica.sum()))
    return {k: np.array(v) for k, v in resultado.items()}


def main():
    p = argparse.ArgumentParser(description="Simula baixas que faltam ao acaso e nas entregas demoradas.")
    p.add_argument("--entregas", type=int, default=48)
    p.add_argument("--repeticoes", type=int, default=2000)
    args = p.parse_args()
    if args.entregas < 16 or args.repeticoes < 1:
        raise SystemExit("use --entregas 16 ou mais e --repeticoes 1 ou mais")
    r = simular(args.entregas, args.repeticoes, np.random.default_rng(SEMENTE))
    print(f"{args.repeticoes} meses de {args.entregas} entregas cada")
    print()
    print(f"{'quem fica sem baixa':<20}{'sem baixa':>10}{'média real':>12}{'média vista':>13}"
          f"{'diferença':>11}{'vai e volta':>13}")
    for nome, a in r.items():
        dif = a[:, 1] - a[:, 0]
        print(f"{nome:<20}{br(a[:, 4].mean()):>10}{br(a[:, 0].mean()):>10} h{br(a[:, 1].mean()):>11} h"
              f"{br(dif.mean()):>9} h{br(a[:, 1].std()):>11} h")
    print()
    print(f"Acima de {PRAZO} h")
    for nome, a in r.items():
        print(f"  {nome:<18} real {br(100 * a[:, 2].mean())}%   visto {br(100 * a[:, 3].mean())}%")
    print()
    print("vai e volta: desvio da média vista de um mês para outro")


if __name__ == "__main__":
    main()
