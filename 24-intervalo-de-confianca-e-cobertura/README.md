# 24. Intervalo de confiança e cobertura

Os arquivos da aula «Intervalo de confiança e cobertura» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `coletas_outubro.csv` | As 40 coletas de devolução que o Bruno anotou em outubro: `id_coleta` e `horas`, do pedido de devolução até a chegada da transportadora |
| `gerar_coletas.py` | O programa que gera `coletas_outubro.csv` de novo, igual toda vez |
| `respostas-modelo.md` | A folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome |

O exercício não usa arquivo de dados: o resumo do depósito está no enunciado.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. O primeiro bloco lê as coletas e cria `horas`, `media`, `s` e `ep`, que os outros usam. O bloco da seção 6 cria o `mundo` e as funções que as seções 7 e 8 usam. Os sorteios usam só a biblioteca padrão do Python e levam poucos segundos.

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`. Rodar só uma parte continua o sorteio de onde ele parou.

Para gerar o CSV de novo:

```bash
python3 gerar_coletas.py
```

A saída é `coletas=40 menor=29.1 maior=73.1`.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
