"""As contas da aula «O que queremos estimar», com os tíquetes da Loja Exemplo.

Rode de dentro da pasta da aula:

    python3 estimar.py

O que ele faz, na ordem da aula:
1. Mostra o que é uma linha da tabela (um pedido) e quantos pedidos há em cada canal.
2. Calcula a estimativa da pergunta do Rafa: que parte dos pedidos do site passa de R$ 150.
3. Faz a mesma conta para outras populações: a loja física e a loja toda.
4. Finge que os pedidos do site da tabela são todos os pedidos do site e sorteia cinco
   amostras de 60. O número de cada amostra muda; o número de todos fica igual.
   O sorteio é sempre o mesmo, então a sua saída sai igual à da aula.
"""
import numpy as np
import pandas as pd

ARQUIVO = "../dados/loja/tiquetes.csv"
LIMITE = 150
TAMANHO_AMOSTRA = 60
AMOSTRAS = 5
SORTEIO = 3


def br(numero, casas=1):
    return f"{numero:.{casas}f}".replace(".", ",")


def parte(serie, limite):
    acima = int((serie > limite).sum())
    return f"{acima} de {len(serie)} ({br(100 * acima / len(serie))}%)"


def main():
    tiquetes = pd.read_csv(ARQUIVO)
    site = tiquetes[tiquetes["canal"] == "site"]["valor"]
    loja = tiquetes[tiquetes["canal"] == "loja_fisica"]["valor"]

    print(f"Tíquetes: {len(tiquetes)} pedidos, uma linha por pedido")
    print(f"  colunas: {', '.join(tiquetes.columns)}")
    print(f"  site {len(site)} | loja física {len(loja)}")
    print()
    print(f"A pergunta do Rafa: que parte dos pedidos do site passa de R$ {LIMITE}?")
    print(f"  amostra: os {len(site)} pedidos do site da tabela")
    print(f"  estimativa: {parte(site, LIMITE)}")
    print()
    print(f"Outra população, outro número (acima de R$ {LIMITE})")
    print(f"  loja física   {parte(loja, LIMITE)}")
    print(f"  loja toda     {parte(tiquetes['valor'], LIMITE)}")
    print()
    print(f"Se os {len(site)} fossem todos os pedidos do site: {AMOSTRAS} amostras de {TAMANHO_AMOSTRA}")
    gerador = np.random.default_rng(SORTEIO)
    for i in range(1, AMOSTRAS + 1):
        amostra = site.sample(TAMANHO_AMOSTRA, random_state=gerador)
        print(f"  amostra {i}: {parte(amostra, LIMITE)}")
    print(f"  todos os {len(site)}: {parte(site, LIMITE)}, o mesmo nas {AMOSTRAS} vezes")


if __name__ == "__main__":
    main()
