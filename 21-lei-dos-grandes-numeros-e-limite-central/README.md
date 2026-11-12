# 21. Lei dos grandes números e limite central

Os arquivos da aula «Lei dos grandes números e limite central» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `medias.py` | As funções `fora_da_faixa`, `sortear` e `medias_de_amostras` das seções 4 e 7 da aula, para usar no exercício |
| `chamados_outubro.csv` | A espera de 300 chamados do chat em outubro: `id_chamado` e `minutos`, de abrir a conversa até a primeira resposta |
| `gerar_chamados.py` | O programa que gera `chamados_outubro.csv` de novo, igual toda vez |
| `respostas-modelo.md` | A folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome |

Os tíquetes da aula ficam na base compartilhada do kit, em `../dados/loja/tiquetes.csv`.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. O primeiro bloco lê os tíquetes e cria `site`, `mu` e `sigma`, que os outros usam. Os blocos das seções 4 e 7 criam as funções que as seções seguintes usam. Os sorteios usam só a biblioteca padrão do Python. O da seção 8 sorteia 10 milhões de pedidos e leva alguns segundos.

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`. Rodar só uma parte continua o sorteio de onde ele parou.

No exercício, comece com:

```python
from medias import fora_da_faixa, medias_de_amostras
```

Para gerar o CSV de novo:

```bash
python3 gerar_chamados.py
```

A saída é `chamados=300 menor=0.0 maior=41.5`.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
