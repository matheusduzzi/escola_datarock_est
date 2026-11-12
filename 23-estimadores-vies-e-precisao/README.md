# 23. Estimadores, viés e precisão

Os arquivos da aula «Estimadores, viés e precisão» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `estimadores.py` | As funções `media`, `mediana`, `mistura`, `sortear`, `comparar` e `resumo` das seções 4 e 5 da aula, para usar no exercício |
| `respostas-modelo.md` | A folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome |

Os tíquetes da aula e as entregas do exercício ficam na base compartilhada do kit, em `../dados/loja/tiquetes.csv` e `../dados/loja/entregas.csv`.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. O primeiro bloco lê os tíquetes e cria `site`, `mu` e `sigma`, que os outros usam. Os blocos da seção 4 criam as regras e as funções `sortear`, `comparar` e `resumo`. As seções 5, 6 e 7 e o pedido 2 da prática guiada usam essas funções. Os sorteios usam só a biblioteca padrão do Python. O bloco da seção 5 é o mais demorado, perto de 15 segundos.

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`. Rodar só uma parte continua o sorteio de onde ele parou.

No exercício, comece com:

```python
from estimadores import comparar, media, mediana, mistura, resumo
```

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
