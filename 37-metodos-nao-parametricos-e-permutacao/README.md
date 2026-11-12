# 37. Métodos não paramétricos e permutação

Os arquivos da aula «Métodos não paramétricos e permutação» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `carrinho.csv` | O teste do carrinho, o mesmo da aula «Aplicar ANOVA e interpretar limites»: um pedido por linha, com cliente, semana, dia, versão e valor em reais |
| `distribuicao_t.py` | A tabela t no Python, com `t_acumulada` e `t_critico`. A função `welch` da seção 5 usa as duas |
| `notas_chat.csv` | Caso 1 do exercício: a nota de 1 a 5 de cada cliente, com a mensagem antiga ou a nova |
| `entregas_regiao.csv` | Caso 2 do exercício: as horas de cada entrega de um mês, na capital e no interior |
| `leitor_separacao.csv` | Caso 3 do exercício: os minutos por pedido de 12 separadores, com a lista no papel e com o leitor |
| `gerar_dados.py` | Gera de novo os quatro arquivos `.csv` |
| `respostas-modelo.md` | A folha do exercício, com o critério em cinco linhas para os três casos. Salve uma cópia com o seu nome |

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. A seção 4 cria `postos`, `chance_de_ganhar`, `dif_medias` e `permutacao`. A seção 5 lê o `carrinho.csv` e cria `welch` e `mann_whitney`. A seção 8 cria `permutacao_pareada` e `soma_postos_positivos`. O pedido 2 da prática guiada cria `dif_medianas`. O exercício usa essas funções.

O bloco das três contas da seção 5 leva uns 5 segundos. O da seção 7 leva uns 10.

Para gerar os arquivos de novo:

```bash
python3 gerar_dados.py
```

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`. Rodar só uma parte continua o sorteio de onde ele parou.

Só usa a biblioteca padrão do Python: `csv`, `itertools`, `math`, `random`, `collections` e `statistics`. No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
