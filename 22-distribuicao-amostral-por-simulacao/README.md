# 22. Distribuição amostral por simulação

Os arquivos da aula «Distribuição amostral por simulação» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `amostras.py` | As funções `sortear` e `repetir` da seção 4 da aula, para usar no exercício |
| `separacao_novembro.csv` | O tempo de separação de 400 pedidos no estoque em novembro: `id_pedido`, `turno` (`manha` ou `noite`) e `minutos` |
| `gerar_separacao.py` | O programa que gera `separacao_novembro.csv` de novo, igual toda vez |
| `respostas-modelo.md` | A folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome |

Os tíquetes da aula ficam na base compartilhada do kit, em `../dados/loja/tiquetes.csv`.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. O primeiro bloco lê os tíquetes e cria `site`, `loja`, `sigma` e `sigma_l`, que os outros usam. Os blocos da seção 4 criam as funções `sortear` e `repetir` e o dicionário `desvios_site`, que a seção 6 usa. Os sorteios usam só a biblioteca padrão do Python. O bloco da `repetir` na seção 4 e o da seção 5 levam perto de um minuto cada.

Os sorteios saem iguais toda vez que você roda. Se a sua saída tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`. Rodar só uma parte continua o sorteio de onde ele parou.

No exercício, comece com:

```python
from amostras import repetir, sortear
```

Para gerar o CSV de novo:

```bash
python3 gerar_separacao.py
```

A saída é `pedidos=400 menor=4.7 maior=31.2`.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
