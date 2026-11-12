# 38. Comparar conclusões sob métodos distintos

Os arquivos da aula «Comparar conclusões sob métodos distintos» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `carrinho_divisorias.csv` | O teste do Bruno no depósito: 24 separadores, cada um com um turno no carrinho comum e um no carrinho com divisórias, em ordem sorteada. Colunas `separador`, `ordem` (`comum_primeiro` ou `divisorias_primeiro`), `comum_min` e `divisorias_min` (minutos médios por pedido no turno) |
| `chat_triagem.csv` | O teste da Carla no atendimento, do exercício: 320 chats, com `chat`, `cliente`, `triagem` (`antiga` ou `nova`) e `minutos` até a primeira resposta de uma pessoa |
| `receitas.py` | As receitas das aulas anteriores, prontas para importar: `pareado`, `welch`, `postos`, `chance_de_ganhar`, `mann_whitney`, `dif_medias` e `permutacao` |
| `distribuicao_t.py` | A tabela t no Python, só com a biblioteca padrão. O `receitas.py` usa ele |
| `respostas-modelo.md` | A folha do exercício, com as cinco tarefas. Salve uma cópia com o seu nome |
| `gerar_dados.py` | Gera os dois CSVs de novo. Ele conta como cada número nasce: abra só depois de fazer a aula e o exercício |

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. O primeiro bloco da seção 4 importa as receitas. O segundo cria `troca_de_sinais`, `soma_postos_positivos` e `teste_do_sinal`. O bloco da seção 5 lê o carrinho e cria `difs`, o da seção 6 cria `ordem`, e o da seção 8 cria `bootstrap_media`. O resto da aula usa esses nomes. O bloco da seção 10 leva uns 20 segundos.

Para o exercício, abra o Python na mesma pasta e importe o que precisar do `receitas.py`:

```python
from receitas import welch, permutacao, dif_medias, mann_whitney
```

Para gerar os CSVs de novo:

```bash
python3 gerar_dados.py
```

A saída é `carrinho_divisorias=24 chat_triagem=320`. Os arquivos saem iguais toda vez.

Os sorteios da aula também saem iguais toda vez que você roda, porque cada bloco cria o seu `random.Random(38)`. Se a sua saída tiver outros números, rode o bloco inteiro de novo.

No Windows, troque `python3` por `py`. Não precisa do SciPy. Se você já usa o SciPy, a aula diz qual função dele faz cada conta.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
