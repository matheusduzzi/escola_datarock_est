# 42. Banca de interpretação

Os arquivos da aula «Banca de interpretação» do curso Estatística para decisão.

## O que tem nessa pasta

| Arquivo | Para quê |
|---|---|
| `setembro.csv` | O piloto de setembro da capital, o mesmo das aulas 33 e 41: 210 entregas, 105 para cada transportadora. Colunas `id_entrega`, `transportadora` (`atual` ou `nova`) e `horas` |
| `distribuicao_t.py` | A tabela t no Python, a mesma das aulas 33, 40 e 41. Dá a função `t_critico` |
| `banca_capital.py` | As cinco perguntas da banca da capital, das seções 4 a 9 da aula. É o comando que a nota final cita |
| `dados/refeitorios.csv` e `dados/bandejas.csv` | Os refeitórios da Bia, os mesmos das aulas 39 e 40. Uma linha de `refeitorios.csv` é um refeitório e o grupo dele. Uma linha de `bandejas.csv` é uma bandeja: `data`, `refeitorio`, `cracha`, `periodo` (`antes` ou `depois`) e `salada_g` |
| `relatorio_refeitorios.py` | O relatório da aula 40, igual. O exercício importa as funções dele: `mudanca_por_refeitorio`, `diferenca`, `intervalo` e `SORTEADOS` |
| `minha_banca.py` | Onde você escreve as contas da tarefa 2 do exercício. Depois, é o comando da sua nota final |
| `roteiro-banca.md` | A folha do exercício: as cinco perguntas da diretoria, o quadro da banca e o molde da nota final. Salve uma cópia com o seu nome |

## Como rodar

Os blocos de código da aula rodam no Python aberto dentro dessa pasta, só com a biblioteca padrão:

```bash
python3
```

Cole os blocos da aula na ordem, a partir da seção 4. O primeiro bloco cria `horas` e as funções `welch`, `decidir`, `wilson` e `pct`. A seção 7 cria `minimo_no_prazo`. A prática guiada usa todas elas.

Para ver as cinco perguntas da banca de uma vez:

```bash
python3 banca_capital.py
```

Nenhuma conta da aula usa sorteio: as saídas são sempre as mesmas.

O exercício usa o pandas, que o README do kit já instala, como na aula 40:

```bash
python3 minha_banca.py
```

Antes de você escrever qualquer coisa, ele mostra uma linha só: `relatório da Bia: 11.0 g, de 5.9 a 16.2 g`. Se aparecer essa linha, os arquivos estão no lugar.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
