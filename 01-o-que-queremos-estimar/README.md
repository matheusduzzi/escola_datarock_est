# 01. O que queremos estimar

Os arquivos da aula «O que queremos estimar» do curso Estatística para decisão.

| Arquivo | Para quê |
|---|---|
| `estimar.py` | As contas das seções 4 e 5: a parte dos pedidos do site acima de R$ 150, a mesma conta para outras populações e cinco amostras sorteadas de 60 pedidos |
| `minha-pergunta.md` | A folha do exercício: a pergunta escrita, unidade, população, parâmetro, amostra, estimativa e o que fica de fora |

O `estimar.py` lê os tíquetes da base compartilhada do kit, em `../dados/loja/tiquetes.csv`. Rode de dentro dessa pasta:

```bash
python3 estimar.py
```

Ele usa o pandas e o NumPy, que o README do kit já instala. Não precisa de internet. O sorteio é sempre o mesmo, então a sua saída sai igual à da aula. O começo do programa conta o que cada parte calcula.

O exercício usa as entregas e os tíquetes de `../dados/loja`. Você escreve o seu próprio código no pandas; as dicas do exercício mostram por onde começar.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
