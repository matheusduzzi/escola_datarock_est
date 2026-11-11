"""As contas da aula «Como a amostra foi formada»: o jogo do tablet da loja física.

Rode de dentro da pasta da aula:

    python3 formar_amostra.py

O que ele faz, na ordem da aula:
1. Monta um cadastro de 2.000 clientes da loja física em que eu sei a resposta de todos:
   quem viria se a loja abrisse no domingo. Esses números são escolhas do jogo, para ver
   o que cada forma de coletar faz com a conta. A loja de verdade não sabe esses números.
     - 600 clientes trabalham no sábado e nunca passam na loja no sábado à tarde;
       480 deles viriam no domingo.
     - 1.400 clientes podem passar no sábado; 420 deles viriam no domingo.
2. Coleta a resposta de quatro jeitos, cada um repetido 1.000 vezes:
     - sorteio no cadastro e ligação, com 100 e com 400 clientes, todo mundo responde;
     - tablet no caixa aos sábados à tarde: cada cliente que pode vir no sábado passa no
       caixa num sábado com chance de 6%. A caixa convida quem passa. Quem viria no domingo
       aceita responder com chance de 60%; quem não viria, com chance de 25%;
     - o mesmo tablet, mas com todo convidado respondendo (só o problema de quem passa);
     - o tablet por 4 e por 40 sábados. O tablet não sabe quem já respondeu, então a mesma
       pessoa pode responder em sábados diferentes.
3. Para cada jeito, mostra a média das 1.000 estimativas e a faixa onde caem 9 em cada 10.
   O sorteio é sempre o mesmo, então a sua saída sai igual à da aula.
"""
import numpy as np

SORTEIO = 2
REPETICOES = 1000

TRABALHAM_SABADO, SIM_TRABALHAM = 600, 480
PODEM_SABADO, SIM_PODEM = 1400, 420
CHANCE_PASSAR = 0.06
RESPONDE_SIM, RESPONDE_NAO = 0.60, 0.25


def br(numero, casas=1):
    texto = f"{numero:,.{casas}f}"
    return texto.replace(",", "X").replace(".", ",").replace("X", ".")


def pct(numero):
    return br(100 * numero) + "%"


def cadastro():
    """Uma linha por cliente: True se viria no domingo. Os primeiros 600 trabalham no sábado."""
    trabalham = np.array([True] * SIM_TRABALHAM + [False] * (TRABALHAM_SABADO - SIM_TRABALHAM))
    podem = np.array([True] * SIM_PODEM + [False] * (PODEM_SABADO - SIM_PODEM))
    return np.concatenate([trabalham, podem])


def ligacao(rng, viria, n):
    estimativas = [viria[rng.choice(len(viria), size=n, replace=False)].mean() for _ in range(REPETICOES)]
    return np.array(estimativas), n, n


def tablet(rng, viria, sabados, todos_respondem=False):
    podem = viria[TRABALHAM_SABADO:]
    chance = np.where(podem, RESPONDE_SIM, RESPONDE_NAO)
    if todos_respondem:
        chance = np.ones_like(chance)
    estimativas, respostas, pessoas = [], [], []
    for _ in range(REPETICOES):
        passou = rng.random((sabados, len(podem))) < CHANCE_PASSAR
        respondeu = passou & (rng.random((sabados, len(podem))) < chance)
        por_pessoa = respondeu.sum(axis=0)
        total = por_pessoa.sum()
        estimativas.append((por_pessoa * podem).sum() / total)
        respostas.append(total)
        pessoas.append((por_pessoa > 0).sum())
    return np.array(estimativas), np.mean(respostas), np.mean(pessoas)


def linha(nome, resultado):
    estimativas, respostas, pessoas = resultado
    baixo, alto = np.quantile(estimativas, [0.05, 0.95])
    print(f"  {nome:<34}{br(respostas, 0):>7}{br(pessoas, 0):>8}"
          f"   {pct(estimativas.mean()):>6}   {pct(baixo)} a {pct(alto)}")


def main():
    rng = np.random.default_rng(SORTEIO)
    viria = cadastro()

    print(f"Jogo: o cadastro da loja física com {br(len(viria), 0)} clientes")
    print(f"  trabalham no sábado: {br(TRABALHAM_SABADO, 0)}, dos quais {SIM_TRABALHAM} viriam no domingo "
          f"({pct(SIM_TRABALHAM / TRABALHAM_SABADO)})")
    print(f"  podem vir no sábado: {br(PODEM_SABADO, 0)}, dos quais {SIM_PODEM} viriam no domingo "
          f"({pct(SIM_PODEM / PODEM_SABADO)})")
    print(f"  todos: {viria.sum()} de {br(len(viria), 0)} viriam no domingo ({pct(viria.mean())})")
    print()
    print(f"Cada forma de coletar, repetida {br(REPETICOES, 0)} vezes")
    print(f"  {'':<34}{'resp.':>7}{'pessoas':>8}   {'média':>6}   9 em cada 10 entre")
    linha("ligação para 100 sorteados", ligacao(rng, viria, 100))
    linha("ligação para 400 sorteados", ligacao(rng, viria, 400))
    linha("sábado, todo convidado responde", tablet(rng, viria, 4, todos_respondem=True))
    linha("tablet, 4 sábados", tablet(rng, viria, 4))
    linha("tablet, 40 sábados", tablet(rng, viria, 40))


if __name__ == "__main__":
    main()
