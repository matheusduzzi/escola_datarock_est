# 05. Descrever distribuição

Os arquivos da aula «Descrever distribuição» do curso Estatística para decisão. Rode os comandos de dentro dessa pasta.

| Arquivo | Para que serve |
|---|---|
| `distribuicao.py` | Os números da aula: quantis dos tíquetes por canal, as sete convenções de quartil, as contagens do histograma, os números do boxplot e a largura do violino. Só precisa do pandas. |
| `graficos.py` | Os gráficos da aula, salvos na pasta `saida/`: os dois histogramas, o boxplot, o violino dos tíquetes e o violino da Ana e do Beto. Precisa do matplotlib. |
| `dados/pedidos_canais_novos.csv` | 169 pedidos do exercício: `id_pedido`, `canal` (`app` ou `whatsapp`) e `valor` em reais. |
| `minha_analise.py` | Onde você escreve o código do exercício. |
| `minhas-respostas.md` | Onde você escreve as respostas do exercício. |

Os tíquetes da aula vêm da base do curso, em `../dados/loja/tiquetes.csv`.

## Do que você precisa

Python com o pandas, como no README do kit do curso. Para os gráficos, instale também o matplotlib, com o mesmo `python3` que roda os programas:

```bash
python3 -m pip install matplotlib
```

Eu rodei esses arquivos com Python 3.9.6, pandas 2.3.3 e matplotlib 3.9.4. Em versões mais novas, os padrões usados aqui continuam os mesmos: 10 faixas no histograma, bigode de 1,5 IQR no boxplot e regra de Scott no violino.

## Como rodar

```bash
python3 distribuicao.py
```

A saída é a mesma da seção 5 da aula, e sai igual toda vez.

```bash
python3 graficos.py
```

Ele cria a pasta `saida/` com cinco imagens PNG e mostra os nomes na tela. Abra as imagens para ver os gráficos.

```bash
python3 minha_analise.py
```

Antes de você escrever qualquer coisa, ele só mostra `169 pedidos: app 160, whatsapp 9`. As tarefas ficam embaixo, nos comentários.

Se aparecer `FileNotFoundError`, você está rodando de outra pasta. Entre na pasta dessa aula e rode de novo. Se aparecer `No module named 'matplotlib'`, falta instalar o matplotlib no Python que você está usando.

O CSV vem pronto e não muda. Não edite à mão: as respostas do exercício dependem desses números.

## Se precisar de ajuda

Deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
