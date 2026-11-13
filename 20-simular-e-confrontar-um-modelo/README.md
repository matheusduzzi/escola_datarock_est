# 20. Simular e confrontar um modelo

Os arquivos da aula «Simular e confrontar um modelo» do curso Estatística para decisão.

## Os dados da aula

| Arquivo | Colunas |
|---|---|
| `dados/pedidos_trimestre.csv` | Os 92 dias de 1º de julho a 30 de setembro de 2026: `data`, `dia_semana` (seg, ter, qua, qui, sex, sab, dom) e `pedidos` (quantos pedidos a Loja Exemplo recebeu no dia) |

## Os dados do exercício

| Arquivo | Colunas |
|---|---|
| `dados/devolucoes_trimestre.csv` | Os mesmos 92 dias: `data`, `dia_semana`, `pedidos` e `devolucoes` (quantos pedidos feitos naquele dia voltaram em devolução) |

## A folha de respostas

`respostas-modelo.md` é a folha do exercício, com um espaço por tarefa. Salve uma cópia com o seu nome.

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta. Eles usam o pandas e o NumPy que o README do kit já instala:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 4. O primeiro bloco lê os pedidos e cria a tabela `p`. Os outros usam o que os anteriores criaram: `x`, as funções `medidas` e `confrontar`, `modelo1` e `modelo2`. Os caminhos começam em `dados/`.

O sorteio usa o `np.random.default_rng` do NumPy, que existe desde a versão 1.17. A dica 2 do exercício usa o `sliding_window_view`, que existe desde a 1.20. Para ver a sua versão:

```bash
python3 -c "import numpy; print(numpy.__version__)"
```

Com o mesmo número dentro de `default_rng` e a mesma versão do NumPy, as simulações saem iguais às da aula. Em outra versão, a sequência do sorteio pode mudar, e as faixas e frações mudam um pouco. A leitura não muda.

Os dois arquivos de dados vêm prontos e são sempre os mesmos.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
