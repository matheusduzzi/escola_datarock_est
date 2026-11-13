# 29. Hipóteses e distribuição nula

Os arquivos da aula «Hipóteses e distribuição nula» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `entregas_junho.csv` | O piloto de junho da Dani: 60 entregas da capital, 30 sorteadas para cada transportadora. Colunas `id_entrega`, `transportadora` (`atual` ou `nova`) e `horas` |
| `coletas_dezembro.csv` | O exercício: 80 coletas de devolução, 40 sorteadas para cada roteiro. Colunas `id_coleta`, `roteiro` (`atual` ou `novo`) e `horas`, em hora cheia |
| `gerar_dados.py` | O programa que gera os dois arquivos de novo, iguais toda vez. O começo dele conta como os tempos foram sorteados. Abra só depois do exercício |
| `respostas-modelo.md` | A folha do exercício, com o plano de oito linhas. Salve uma cópia com o seu nome |

As entregas de março ficam na base compartilhada do kit, em `../dados/loja/entregas.csv`.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 6. O bloco da seção 7 cria as funções `diferenca_medias`, `distribuicao_nula` e `linha_de_corte`, que o resto da aula e o exercício usam. O bloco da seção 8 sorteia 20.000 meses e leva alguns segundos.

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`. Rodar só uma parte continua o sorteio de onde ele parou.

Para gerar os arquivos de novo:

```bash
python3 gerar_dados.py
```

A saída é `junho=60 nova=30 dezembro=80 novo=40`.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
