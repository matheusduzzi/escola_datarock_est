# 41. Nota de decisão sobre prazo de entrega

Os arquivos da aula «Nota de decisão sobre prazo de entrega» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `setembro.csv` | O piloto de setembro da aula «Comparar médias independentes e pareadas»: 210 entregas da capital, 105 para cada transportadora. Colunas `id_entrega`, `transportadora` (`atual` ou `nova`) e `horas` |
| `distribuicao_t.py` | A tabela t no Python, a mesma da aula 33. A aula e o `nota_capital.py` usam a função `t_critico` |
| `nota_capital.py` | Os números da nota da capital, da seção 9 da aula. É o comando que a nota cita |
| `interior_outubro.csv` | O exercício: 200 entregas do interior em outubro. Colunas `id_entrega`, `dia` (o dia de outubro em que o pedido saiu) e `horas`. Célula de `horas` vazia quer dizer que a baixa não foi anotada |
| `minha_solucao.py` | Onde você escreve `quadro_de_prazos` e `prazo_para_mostrar`, da tarefa 2. Depois, é o comando da sua nota |
| `conferir.py` | Testa as suas funções com setembro, com as entregas de março e com casos pequenos. Não usa o interior |
| `gerar_dados.py` | O programa que gera `interior_outubro.csv` de novo, igual toda vez. O começo dele conta como os tempos e as baixas que faltam foram sorteados: abra só depois de fazer o exercício |
| `nota-modelo.md` | A folha do exercício, com o molde da nota. Salve uma cópia com o seu nome |

As 48 entregas de março, do pedido 3 da prática guiada, ficam na base compartilhada do kit: `../dados/loja/entregas.csv`.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. O primeiro bloco importa `csv`, `math`, as funções de `statistics` e o `t_critico`, e cria `horas`. Os outros criam `welch`, `decidir`, `wilson` e `pct`. A prática guiada usa essas funções.

Para ver os números da nota da capital de uma vez:

```bash
python3 nota_capital.py
```

Nenhuma conta da aula usa sorteio: as saídas são sempre as mesmas.

Para testar as suas funções da tarefa 2:

```bash
python3 conferir.py
```

Enquanto as funções não estiverem prontas, aparecem linhas com `FALHA` e o motivo. Quando tudo passar, a última linha é `tudo certo`. Aí rode `python3 minha_solucao.py` para ver os quadros do interior.

Para gerar o arquivo do interior de novo:

```bash
python3 gerar_dados.py
```

A saída é `interior=200 antes_do_dia_15=90 a_partir_do_dia_15=110 sem_baixa=5`.

Tudo aqui usa só a biblioteca padrão do Python 3.9 ou mais novo. No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
