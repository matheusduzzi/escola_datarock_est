"""Gera os quatro arquivos dessa aula. Abra só depois de fazer a aula e o exercício.

setembro.csv: o piloto de setembro da Dani. 210 entregas da capital, sorteadas uma a uma,
  105 para cada transportadora. Horas da atual: normal com média 43,8 e desvio 5,0.
  Horas da nova: normal com média 40,6 e desvio 5,4. A nova é 3,2 horas mais rápida.
separacao.csv: o teste de um turno do Bruno. 16 separadores, 10 pedidos com a lista no papel e
  10 com o aplicativo. Cada separador tem o seu ritmo: normal com média 0 e desvio 2,5 minutos.
  O pedido leva 12 minutos mais o ritmo, mais um sorteio normal com desvio 3,0 por pedido.
  O aplicativo tira 1,0 minuto. Quem faz a segunda rodada já conhece o turno e ganha 0,4 minuto.
  Metade dos separadores começa pelo papel, metade pelo aplicativo, por sorteio.
frete.csv: a faixa de frete do Rafa. 240 pedidos do site numa semana; no carrinho, 1 em cada 4 foi
  sorteado para ver a faixa "frete grátis acima de R$ 199". Valor do pedido: lognormal; sem a faixa,
  mediana perto de R$ 140; com a faixa, mediana perto de R$ 158 e espalhamento maior.
embalagem.csv: a mesa nova da embalagem. 14 embaladores, cada um com a média de minutos por caixa
  num turno com a mesa antiga e num com a nova, em ordem sorteada. Cada um tem o seu ritmo
  (média 6 e desvio 1,2 minuto); a mesa nova tira 0,35 minuto; sorteio do turno com desvio 0,25.
  O embalador E09 faltou no turno da mesa nova.
"""
import csv
import math
import random
import sys

SEMENTE = 3318


def gerar(semente):
    rng = random.Random(semente)
    setembro = []
    grupos = ["atual"] * 105 + ["nova"] * 105
    rng.shuffle(grupos)
    for i, g in enumerate(grupos, start=1):
        h = rng.gauss(43.8, 5.0) if g == "atual" else rng.gauss(40.6, 5.4)
        setembro.append({"id_entrega": i, "transportadora": g, "horas": f"{h:.1f}"})

    separacao = []
    ordem = ["papel_primeiro"] * 8 + ["celular_primeiro"] * 8
    rng.shuffle(ordem)
    pid = 0
    for s in range(1, 17):
        ritmo = rng.gauss(0, 2.5)
        listas = ["papel", "celular"] if ordem[s - 1] == "papel_primeiro" else ["celular", "papel"]
        for rodada, lista in enumerate(listas):
            for _ in range(10):
                pid += 1
                m = 12 + ritmo + rng.gauss(0, 3.0) - (1.0 if lista == "celular" else 0) - 0.4 * rodada
                separacao.append({"id_pedido": pid, "separador": f"S{s:02d}", "ordem": ordem[s - 1],
                                  "lista": lista, "minutos": f"{max(m, 2.0):.1f}"})

    frete = []
    grupos = ["com_faixa"] * 60 + ["sem_faixa"] * 180
    rng.shuffle(grupos)
    for i, g in enumerate(grupos, start=1):
        v = math.exp(rng.gauss(math.log(158), 0.55)) if g == "com_faixa" else math.exp(rng.gauss(math.log(140), 0.40))
        frete.append({"id_pedido": i, "grupo": g, "valor": f"{v:.2f}"})

    embalagem = []
    ordem = ["antiga_primeiro"] * 7 + ["nova_primeiro"] * 7
    rng.shuffle(ordem)
    for e in range(1, 15):
        ritmo = 6.0 + rng.gauss(0, 1.2)
        antiga = ritmo + rng.gauss(0, 0.25)
        nova = ritmo - 0.35 + rng.gauss(0, 0.25)
        embalagem.append({"id_embalador": f"E{e:02d}", "ordem": ordem[e - 1],
                          "antiga_min": f"{antiga:.2f}", "nova_min": "" if e == 9 else f"{nova:.2f}"})
    return setembro, separacao, frete, embalagem


def salvar(nome, linhas):
    with open(nome, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)


if __name__ == "__main__":
    st, sp, fr, em = gerar(int(sys.argv[1]) if len(sys.argv) > 1 else SEMENTE)
    for nome, linhas in [("setembro.csv", st), ("separacao.csv", sp), ("frete.csv", fr), ("embalagem.csv", em)]:
        salvar(nome, linhas)
    print(f"setembro={len(st)} separacao={len(sp)} frete={len(fr)} embalagem={len(em)}")
