# 18. Normal e exponencial

Os arquivos da aula «Normal e exponencial» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `dados/caixas.csv` | A altura, em centímetros, das 200 caixas da amostra do fornecedor novo. Usado nas seções 3, 4 e 8 da aula |
| `dados/intervalos_pedidos.csv` | Os minutos entre dois pedidos seguidos do site em 10 noites de setembro, das 20h às 23h, com a noite e a hora do pedido. Usado nas seções 5 a 8 |
| `dados/intervalos_chat.csv` | Os minutos entre dois chamados seguidos do chat nos 21 dias úteis de setembro, com o dia, a faixa (`manha` ou `tarde`) e a hora do chamado. Usado no exercício |
| `dados/camisetas.csv` | O comprimento, em centímetros, de 150 camisetas M de um fornecedor novo. Usado no exercício |
| `respostas-modelo.md` | A folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome |

Nos dois arquivos de intervalos, o intervalo é contado desde o chamado ou pedido anterior do mesmo dia (e, no chat, da mesma faixa). Por isso o primeiro de cada noite ou faixa não aparece.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos na ordem, a partir da seção 4. Os blocos da seção 4 leem as caixas e criam a função `faixas`. O primeiro da seção 5 lê os pedidos, e o segundo cria a `expon_cdf`. Os blocos seguintes, o exercício e os pedidos 2 e 4 da prática usam essas duas funções.

Tudo usa só o que vem com o Python: os módulos `csv`, `math` e `statistics`. O `NormalDist` do `statistics` existe do Python 3.8 em diante, e o kit do curso pede o 3.9 ou mais novo. O SciPy não é necessário nessa aula. As saídas foram as mesmas no Python 3.9, no 3.14 e no 3.15.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
