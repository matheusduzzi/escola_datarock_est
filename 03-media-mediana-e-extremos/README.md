# 03. Média, mediana e extremos

Os arquivos da aula «Média, mediana e extremos» do curso Estatística para decisão.

| Arquivo | Para quê |
|---|---|
| `centro.py` | As contas das seções 4 a 7: média e mediana do site, o site sem o pedido 117, o resumo por canal e as amostras sorteadas de 60 pedidos |
| `minha_escolha.py` | O ponto de partida do exercício: a função `resumo_centro` para você escrever e a chamada com os pedidos do site |

Os dois programas leem os tíquetes da base compartilhada do kit, em `../dados/loja/tiquetes.csv`. Rode de dentro dessa pasta:

```bash
python3 centro.py
python3 minha_escolha.py
```

Eles usam o pandas e o NumPy, que o README do kit já instala. Não precisam de internet. O sorteio do `centro.py` parte sempre do mesmo ponto, então a sua saída sai igual à da aula. O começo de cada programa conta o que ele faz.

Antes de você escrever a função, o `minha_escolha.py` para com `NotImplementedError: escreva a função resumo_centro`. É o esperado: a mensagem diz o que falta.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
