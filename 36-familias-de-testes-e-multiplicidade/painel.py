"""Funções do painel de métricas da aula «Famílias de testes e multiplicidade».

sortear_painel monta clientes de dois grupos e compara cada métrica entre eles.
Cada cliente tem um jeito de comprar (mais ou menos animado) que puxa várias métricas
juntas, como acontece num painel de verdade. Só a biblioteca padrão do Python.
"""
import math
from statistics import NormalDist

Z = NormalDist()

# nome, tipo, base, desvio (só média), carga do jeito de comprar
METRICAS_CARRINHO = [
    ("itens_por_pedido", "media", 2.4, 1.3, 0.5),
    ("minutos_no_site", "media", 14.0, 6.0, 0.5),
    ("paginas_vistas", "media", 11.0, 5.0, 0.5),
    ("desconto_cupom", "media", 9.0, 7.0, 0.2),
    ("dias_ate_entrega", "media", 4.0, 1.5, 0.0),
    ("nota_da_compra", "media", 4.3, 0.8, 0.3),
    ("usou_cupom", "proporcao", 0.30, None, 0.3),
    ("comprou_de_novo_30d", "proporcao", 0.18, None, 0.5),
    ("pagou_pix", "proporcao", 0.40, None, 0.0),
    ("parcelou", "proporcao", 0.35, None, 0.3),
    ("comprou_pelo_celular", "proporcao", 0.62, None, 0.0),
    ("assinou_novidades", "proporcao", 0.12, None, 0.3),
    ("avaliou_produto", "proporcao", 0.22, None, 0.4),
    ("pediu_troca", "proporcao", 0.06, None, 0.0),
    ("abriu_reclamacao", "proporcao", 0.05, None, 0.0),
    ("entrega_no_prazo", "proporcao", 0.91, None, 0.0),
    ("cancelou", "proporcao", 0.03, None, 0.0),
    ("frete_expresso", "proporcao", 0.15, None, 0.3),
    ("lista_de_desejos", "proporcao", 0.25, None, 0.5),
    ("retirou_na_loja", "proporcao", 0.08, None, 0.0),
]


def _cliente(metricas, rng, efeitos, juntas):
    u = rng.gauss(0, 1)
    valores = {}
    for nome, tipo, base, desvio, carga in metricas:
        c = carga if juntas else 0.0
        x = c * u + math.sqrt(1 - c * c) * rng.gauss(0, 1)
        if tipo == "media":
            valores[nome] = base + desvio * x + efeitos.get(nome, 0.0)
        else:
            valores[nome] = 1 if x > _corte(base + efeitos.get(nome, 0.0)) else 0
    return valores


_CORTES = {}


def _corte(p):
    """Ponto da curva normal que deixa a proporção p acima dele (guardado para não refazer a conta)."""
    p = min(max(p, 0.001), 0.999)
    if p not in _CORTES:
        _CORTES[p] = Z.inv_cdf(1 - p)
    return _CORTES[p]


def _media_variancia(xs):
    n = len(xs)
    m = sum(xs) / n
    return m, sum((x - m) ** 2 for x in xs) / (n - 1)


def comparar(a, b):
    """Diferença (b menos a), erro padrão e p-valor de dois lados pela curva normal.

    Serve para médias e para proporções (valores 0 e 1): a variância de uma lista de 0 e 1 é quase p(1 - p).
    """
    ma, va = _media_variancia(a)
    mb, vb = _media_variancia(b)
    dif = mb - ma
    ep = math.sqrt(va / len(a) + vb / len(b))
    z = dif / ep if ep > 0 else 0.0
    return dif, ep, 2 * (1 - Z.cdf(abs(z)))


def sortear_painel(metricas, n_a, n_b, rng, efeitos=None, juntas=True):
    """Uma linha por métrica: nome, tipo, média de cada grupo, diferença, erro padrão e p-valor."""
    efeitos = efeitos or {}
    ga = [_cliente(metricas, rng, {}, juntas) for _ in range(n_a)]
    gb = [_cliente(metricas, rng, efeitos, juntas) for _ in range(n_b)]
    linhas = []
    for nome, tipo, *_ in metricas:
        a = [c[nome] for c in ga]
        b = [c[nome] for c in gb]
        dif, ep, p = comparar(a, b)
        linhas.append({"metrica": nome, "tipo": tipo, "grupo_a": sum(a) / len(a), "grupo_b": sum(b) / len(b),
                       "diferenca": dif, "erro_padrao": ep, "p_valor": p})
    return linhas
