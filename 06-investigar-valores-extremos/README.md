# 06. Investigar valores extremos

Os arquivos da aula «Investigar valores extremos» do curso Estatística para decisão. Rode os comandos de dentro dessa pasta.

| Arquivo | Para que serve |
|---|---|
| `extremos.py` | As contas da aula: o exemplo dos dez pedidos, a cerca do IQR e o z-score nos tíquetes do site, os pedidos de novembro com as notas fiscais e a sensibilidade de cada decisão. |
| `dados/pedidos_novembro.csv` | 150 pedidos do site da primeira quinzena de novembro: `id_pedido`, `itens` e `valor` em reais, como o sistema gravou. |
| `dados/notas_novembro.csv` | As notas fiscais desses pedidos: `id_pedido` e `valor_nota` em reais. Pedido sem nota não aparece aqui. |
| `minha_analise.py` | Onde você escreve o código do exercício. |
| `minhas-respostas.md` | Onde você escreve as respostas do exercício. |

O `extremos.py` também lê `../dados/loja/tiquetes.csv`, e o exercício lê `../dados/nutricao/`. São as bases compartilhadas do kit do curso, uma pasta acima dessa.

## Como rodar

Você precisa do Python com o pandas, como no README do kit do curso.

```bash
python3 extremos.py
```

A saída é a mesma das seções 2 a 6 da aula, e sai igual toda vez.

```bash
python3 minha_analise.py
```

Antes de você escrever qualquer coisa, ele só mostra `456 medidas de 240 pessoas`. As tarefas ficam embaixo, nos comentários.

Se aparecer `FileNotFoundError`, você está rodando de outra pasta. Entre na pasta dessa aula e rode de novo.

Os CSVs vêm prontos e não mudam. Não edite à mão: para testar uma correção, troque o valor numa cópia da tabela dentro do código.

## Se precisar de ajuda

Deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
