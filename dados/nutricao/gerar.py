"""Gera o estudo inventado de orientação alimentar das aulas 39 e 40 de Estatística para decisão.

Só biblioteca padrão (Python 3.9 ou mais novo). Semente fixa: rodar duas vezes dá os mesmos
arquivos, byte a byte.

    python3 gerar.py                 # escreve nesta pasta
    python3 gerar.py --saida /tmp/x  # escreve em outra pasta

Nada aqui vem de pessoa, posto ou estudo real. O resultado não serve para aconselhar ninguém
sobre alimentação: o estudo existe para treinar a análise e os limites do desenho.

Como os números nascem (o mecanismo, para você comparar com o que a análise mostra):
1. Oito postos de atendimento. Quatro aderiram ao programa de orientação; os outros quatro
   seguiram o atendimento de sempre. Quem escolheu foi o posto, não um sorteio.
2. Cada posto tem um jeito próprio (efeito do posto, normal com desvio 0,4 porção). Os postos
   que aderiram já partiam de um consumo um pouco maior (+0,3 porção): escolheram aderir.
3. Cada participante começa com consumo normal de média 2,8 porções por dia de frutas e
   hortaliças, desvio 1,0, mais o efeito do posto. Valores abaixo de zero viram zero.
4. Na semana 12, todo mundo muda +0,2 porção (época do ano) e quem está nos postos do programa
   muda mais +0,6. A variação individual tem desvio 0,8.
5. Parte das pessoas não volta para a medida da semana 12. No programa, quem começou abaixo de
   2,5 porções desiste com chance 25%; os demais, 8%. Nos postos sem programa, 10% para todos.
6. Uma medida foi digitada sem a vírgula: 45,0 no lugar de 4,5.
"""
import argparse
import csv
import pathlib
import random

SEED = 20261108
POSTOS = [("P1", "programa"), ("P2", "programa"), ("P3", "programa"), ("P4", "programa"),
          ("P5", "comparacao"), ("P6", "comparacao"), ("P7", "comparacao"), ("P8", "comparacao")]
POR_POSTO = 30
BASE_MEDIA, BASE_DP = 2.8, 1.0
DP_POSTO = 0.4
SELECAO_PROGRAMA = 0.3
MUDANCA_GERAL = 0.2
EFEITO_PROGRAMA = 0.6
DP_MUDANCA = 0.8
DIGITACAO = (4.5, 45.0)
FAIXAS = ["18-29", "30-44", "45-59", "60+"]


def gerar(saida):
    rng = random.Random(SEED)
    saida.mkdir(parents=True, exist_ok=True)
    efeito_posto = {p: rng.gauss(0, DP_POSTO) for p, _ in POSTOS}
    participantes, medidas = [], []
    n = 0
    for posto, grupo in POSTOS:
        no_programa = grupo == "programa"
        for _ in range(POR_POSTO):
            n += 1
            pid = "N%03d" % n
            faixa = rng.choice(FAIXAS)
            inicio = rng.gauss(BASE_MEDIA, BASE_DP) + efeito_posto[posto] + (SELECAO_PROGRAMA if no_programa else 0)
            inicio = max(0.0, round(inicio, 1))
            fim = inicio + MUDANCA_GERAL + (EFEITO_PROGRAMA if no_programa else 0) + rng.gauss(0, DP_MUDANCA)
            fim = max(0.0, round(fim, 1))
            chance_sair = (0.25 if inicio < 2.5 else 0.08) if no_programa else 0.10
            saiu = rng.random() < chance_sair
            participantes.append([pid, posto, faixa])
            medidas.append([pid, 0, inicio])
            if not saiu:
                medidas.append([pid, 12, fim])
    # erro de digitação: a primeira medida de semana 12 igual a 4,5 vira 45,0
    for linha in medidas:
        if linha[1] == 12 and linha[2] == DIGITACAO[0]:
            linha[2] = DIGITACAO[1]
            break
    escrever(saida / "postos.csv", ["posto", "grupo"], [list(p) for p in POSTOS])
    escrever(saida / "participantes.csv", ["id_participante", "posto", "faixa_etaria"], participantes)
    escrever(saida / "medidas.csv", ["id_participante", "semana", "porcoes_dia"], medidas)
    return {"postos": len(POSTOS), "participantes": len(participantes), "medidas": len(medidas),
            "sem_semana_12": len(participantes) - sum(1 for m in medidas if m[1] == 12)}


def escrever(caminho, cabecalho, linhas):
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(cabecalho)
        w.writerows(linhas)


def main():
    parser = argparse.ArgumentParser(description="Gera o estudo inventado de orientação alimentar.")
    parser.add_argument("--saida", default=str(pathlib.Path(__file__).resolve().parent))
    resumo = gerar(pathlib.Path(parser.parse_args().saida))
    print(" ".join("%s=%s" % (k, v) for k, v in resumo.items()))


if __name__ == "__main__":
    main()
