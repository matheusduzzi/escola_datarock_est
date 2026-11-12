# 19. Distribuições t e qui-quadrado

Os arquivos da aula «Distribuições t e qui-quadrado» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `estatisticas.py` | As três contas da aula (`media_padronizada`, `soma_de_quadrados` e `qui_quadrado_tabela`) e os limites das tabelas da t e da qui-quadrado do NIST, em quatro dicionários com os graus de liberdade como chave |
| `respostas-modelo.md` | A folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome |

Essa aula não tem arquivo de dados. As caixas da Dani, a tabela da Rita, as camisetas do Léo e a pesquisa do Caio vão direto no código, como a aula mostra.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos na ordem, a partir da seção 4. O primeiro cria o `lote` e a função `media_padronizada`, e os outros usam o que veio antes. Os dois sorteios, nas seções 5 e 6, levam alguns segundos cada.

No exercício, comece com:

```python
from estatisticas import *
print(T_DUAS_PONTAS[9], QUI2_5_ACIMA[2])
```

```
2.262 5.991
```

São os limites que a aula usa para a Dani e para a Rita. Os quatro dicionários são:

| Nome | O ponto da régua |
|---|---|
| `T_DUAS_PONTAS` | t que deixa 2,5% acima, e 2,5% abaixo do negativo |
| `QUI2_5_ACIMA` | qui-quadrado que deixa 5% acima |
| `QUI2_2_5_ACIMA` | qui-quadrado que deixa 2,5% acima |
| `QUI2_2_5_ABAIXO` | qui-quadrado que deixa 2,5% abaixo |

As chaves vão de 1 a 12 graus, mais 15, 24, 29, 30 e 100. A t tem também a chave `"sem fim"`, que é a normal. Para outros graus, veja as tabelas completas do NIST, nos links da seção 16 da aula.

As contas usam só o `math`, o `random` e o `statistics` do Python. O kit do curso pede o Python 3.9 ou mais novo. O SciPy não é necessário nessa aula.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
