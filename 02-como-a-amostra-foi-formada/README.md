# 02. Como a amostra foi formada

Os arquivos da aula «Como a amostra foi formada» do curso Estatística para decisão.

| Arquivo | Para quê |
|---|---|
| `formar_amostra.py` | O jogo do tablet das seções 4 e 5: um cadastro em que se sabe a resposta de todos os clientes e cinco formas de coletar, cada uma repetida 1.000 vezes |
| `coletas.md` | As três coletas do exercício: a pesquisa por e-mail, as entregas de março e as avaliações da mochila |
| `mapa-de-vieses.md` | A folha do exercício: as quatro perguntas, a direção, o alcance e o próximo passo de cada coleta |

Rode de dentro dessa pasta:

```bash
python3 formar_amostra.py
```

Ele usa só o NumPy, que vem junto com o pandas instalado pelo README do kit, e roda em cerca de um segundo. Não precisa de internet. O sorteio é sempre o mesmo, então a sua saída sai igual à da aula. O começo do programa conta as regras do jogo: quantos clientes viriam no domingo e a chance de cada um passar no caixa e responder. Mude esses números e rode de novo para ver o que acontece com cada forma de coletar.

A coleta 2 do exercício usa `../dados/loja/entregas.csv`. Você escreve o seu próprio código no pandas; as dicas do exercício mostram por onde começar.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
