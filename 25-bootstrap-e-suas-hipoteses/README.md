# 25. Bootstrap e suas hipóteses

Os arquivos da aula «Bootstrap e suas hipóteses» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `coletas_outubro.csv` | As 40 coletas de devolução que o Bruno anotou em outubro, as mesmas da aula «Intervalo de confiança e cobertura»: `id_coleta` e `horas` |
| `coletas_novembro.csv` | As 120 coletas de novembro, 10 em cada um de 12 dias sorteados: `dia`, `id_coleta` e `horas` |
| `pedidos_turnos.csv` | O exercício: 72 pedidos cronometrados no depósito, 9 em cada um de 8 turnos: `turno`, `data`, `periodo` (`manhã` ou `tarde`), `id_pedido` e `minutos` |
| `gerar_dados.py` | O programa que gera os três arquivos de novo, iguais toda vez. O começo dele conta como os tempos foram sorteados |
| `respostas-modelo.md` | A folha do exercício, com o plano de seis linhas. Salve uma cópia com o seu nome |

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 3. O primeiro bloco faz as 3.125 reamostras das 5 coletas e importa `csv` e `statistics`. O bloco da seção 4 cria as funções `media`, `reamostrar` e `bootstrap`, que o resto da aula e o exercício usam. O bloco da seção 6 cria `horas`, `por_dia` e `medias_dia`. Os blocos das seções 5 e 6 que contam acertos em 200 meses levam alguns segundos cada.

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`. Rodar só uma parte continua o sorteio de onde ele parou.

Para gerar os arquivos de novo:

```bash
python3 gerar_dados.py
```

A saída é `outubro=40 novembro=120 dias=12 pedidos=72 turnos=8`.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
