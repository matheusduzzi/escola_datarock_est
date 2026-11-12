# 33. Comparar médias independentes e pareadas

Os arquivos da aula «Comparar médias independentes e pareadas» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `setembro.csv` | O piloto de setembro da Dani: 210 entregas da capital, sorteadas uma a uma, 105 para cada transportadora. Colunas `id_entrega`, `transportadora` (`atual` ou `nova`) e `horas` |
| `separacao.csv` | O turno do Bruno no depósito: 16 separadores, cada um com 10 pedidos na lista de papel e 10 no aplicativo. Colunas `id_pedido`, `separador`, `ordem` (`papel_primeiro` ou `celular_primeiro`), `lista` (`papel` ou `celular`) e `minutos` |
| `distribuicao_t.py` | A tabela t no Python, só com a biblioteca padrão: `t_critico(nivel, gl)` dá o número da tabela para uma faixa de `nivel`, e os graus de liberdade podem ter vírgula |
| `frete.csv` | O teste do Rafa, do exercício: 240 pedidos do site, com `id_pedido`, `grupo` (`com_faixa` ou `sem_faixa`) e `valor` em reais |
| `embalagem.csv` | O teste da mesa nova, do exercício: 14 embaladores, com `id_embalador`, `ordem`, `antiga_min` e `nova_min` (média de minutos por caixa em cada turno). A célula vazia é de quem faltou |
| `minha_solucao.py` | Onde você escreve a função `comparar_pareadas` do exercício |
| `conferir.py` | Testa a sua função com casos pequenos montados à mão |
| `respostas-modelo.md` | A folha do exercício, com as cinco tarefas. Salve uma cópia com o seu nome |
| `gerar_dados.py` | Gera os quatro CSVs de novo. Ele conta como cada número nasce: abra só depois de fazer a aula e o exercício |

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta:

```bash
python3
```

Depois cole os blocos da aula na ordem, a partir da seção 3. O bloco da seção 3 cria `welch` e `mostrar`, o da seção 4 cria `student` e `cobertura`, o da seção 6 cria `pareado` e o da seção 9 cria `d_independente`. O resto da aula e o exercício usam essas funções. O bloco da cobertura, na seção 4, leva uns 10 segundos.

Para testar a sua função do exercício:

```bash
python3 conferir.py
```

Enquanto a função não estiver pronta, ele mostra `FALHA` em cada teste e termina com `8 teste(s) falharam`. Quando estiver, termina com `tudo certo`.

Para gerar os CSVs de novo:

```bash
python3 gerar_dados.py
```

A saída é `setembro=210 separacao=320 frete=240 embalagem=14`. Os arquivos saem iguais toda vez.

Os sorteios da aula também saem iguais toda vez que você roda. Se a sua saída da cobertura tiver outros números, rode o bloco inteiro de novo, desde a linha do `random.Random`.

No Windows, troque `python3` por `py`. Não precisa do SciPy: o `distribuicao_t.py` faz a conta da tabela t. Se você já usa o SciPy, a aula mostra a chamada equivalente de cada receita.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
