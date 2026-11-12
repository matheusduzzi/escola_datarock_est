# 16. Bernoulli, binomial e hipergeométrica

Os arquivos da aula «Bernoulli, binomial e hipergeométrica» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `sorteios.py` | Os três sorteios da aula: 4 dos 10 pedidos de 1 de outubro com reposição, os mesmos 4 sem reposição e 20 dos 200 pedidos do mês. Mostra a frequência de cada resultado ao lado da binomial e da hipergeométrica |
| `respostas-modelo.md` | A folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome |

A aula e o exercício não usam arquivo de dados. Os 10 pedidos de 1 de outubro têm 3 devolvidos, e os 200 pedidos do mês, 30. São os das aulas «Eventos e regras de probabilidade» e «Condicional e independência». As quatro situações do exercício estão no texto.

## Como rodar

Os três sorteios:

```bash
python3 sorteios.py
```

Leva uns 2 segundos. A saída tem três tabelas, uma por sorteio, e sai igual toda vez. Ela foi a mesma no Python 3.9, no 3.14 e no 3.15.

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos na ordem, a partir da seção 4. O primeiro cria a função `binomial`, o segundo a `hiper`, e os outros usam as duas. O bloco da seção 7 cria o `p` que o pedido 4 usa.

O `comb` vem do módulo `math` do Python 3.8 em diante. O kit do curso pede o Python 3.9 ou mais novo, então ele já está lá. O SciPy não é necessário nessa aula.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
