"""Gera os dois arquivos de dados da aula «Famílias de testes e multiplicidade».

painel_carrinho.csv: as 20 métricas do painel do teste do carrinho (faixa de R$ 199 contra sem faixa).
relatorio_chat.csv: o relatório do fornecedor do chat (mensagem nova contra a antiga), uma métrica geral e
quatro métricas em cada uma das quatro regiões.
Rodar dentro da pasta da aula:  python3 gerar_dados.py
Os sorteios saem iguais toda vez que você roda.
"""
import csv
import random

from painel import METRICAS_CARRINHO, _cliente, comparar, sortear_painel

METRICAS_CHAT = [
    ("chamado_onde_esta_meu_pedido", "proporcao", 0.20, None, 0.0),
    ("nota_do_atendimento", "media", 4.1, 0.9, 0.4),
    ("respondeu_a_pesquisa", "proporcao", 0.30, None, 0.4),
    ("pediu_cancelamento", "proporcao", 0.06, None, 0.0),
    ("minutos_ate_a_resposta", "media", 18.0, 9.0, 0.0),
]
REGIOES = ["Sul", "Sudeste", "Nordeste", "Norte e Centro-Oeste"]


def gerar_painel(caminho="painel_carrinho.csv", semente=386):
    linhas = sortear_painel(METRICAS_CARRINHO, 269, 257, random.Random(semente),
                            efeitos={"itens_por_pedido": 0.35})
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["metrica", "tipo", "sem_faixa", "faixa_199", "diferenca", "erro_padrao", "p_valor"])
        for l in linhas:
            w.writerow([l["metrica"], l["tipo"], round(l["grupo_a"], 4), round(l["grupo_b"], 4),
                        round(l["diferenca"], 4), round(l["erro_padrao"], 4), round(l["p_valor"], 4)])
    return linhas


def gerar_chat(caminho="relatorio_chat.csv", semente=531, n_por_lado=640):
    rng = random.Random(semente)
    efeitos = {"chamado_onde_esta_meu_pedido": -0.05}
    clientes = []
    for versao, ef in [("antiga", {}), ("nova", efeitos)]:
        for _ in range(n_por_lado):
            c = _cliente(METRICAS_CHAT, rng, ef, True)
            c["versao"], c["regiao"] = versao, rng.choice(REGIOES)
            clientes.append(c)
    linhas = []
    for regiao in ["todas"] + REGIOES:
        nomes = METRICAS_CHAT[:1] if regiao == "todas" else METRICAS_CHAT[1:]
        for nome, tipo, *_ in nomes:
            a = [c[nome] for c in clientes if c["versao"] == "antiga" and regiao in ("todas", c["regiao"])]
            b = [c[nome] for c in clientes if c["versao"] == "nova" and regiao in ("todas", c["regiao"])]
            dif, ep, p = comparar(a, b)
            linhas.append({"metrica": nome, "regiao": regiao, "tipo": tipo, "n_antiga": len(a), "n_nova": len(b),
                           "antiga": sum(a) / len(a), "nova": sum(b) / len(b), "diferenca": dif,
                           "erro_padrao": ep, "p_valor": p})
    with open(caminho, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["metrica", "regiao", "tipo", "n_antiga", "n_nova", "antiga", "nova", "diferenca", "erro_padrao",
                    "p_valor"])
        for l in linhas:
            w.writerow([l["metrica"], l["regiao"], l["tipo"], l["n_antiga"], l["n_nova"], round(l["antiga"], 4),
                        round(l["nova"], 4), round(l["diferenca"], 4), round(l["erro_padrao"], 4),
                        round(l["p_valor"], 4)])
    return linhas


if __name__ == "__main__":
    gerar_painel()
    gerar_chat()
    print("painel_carrinho.csv e relatorio_chat.csv gerados")
