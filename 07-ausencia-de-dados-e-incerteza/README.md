# 07. Dados que faltam e incerteza

Os arquivos da aula «Dados que faltam e incerteza» do curso Estatística para decisão.

| Arquivo | Para quê |
|---|---|
| `vazios.py` | As contas da seção 5: quantas entregas de março têm baixa, a faixa acima de 48 horas e a média em cada cenário para as três sem baixa |
| `simular.py` | A simulação da seção 6: meses em que a baixa falta ao acaso e meses em que falta nas entregas demoradas |
| `modelo-hipoteses.md` | A folha da nota: população, vazios, hipóteses, o que não muda, limites e próximo passo |

Os dois programas leem as bases compartilhadas do kit, na pasta `../dados`. Rode tudo de dentro dessa pasta:

```bash
python3 vazios.py
python3 simular.py
python3 simular.py --entregas 480
```

Eles usam o pandas e o NumPy, que o README do kit já instala. Não precisam de internet. O `simular.py` sorteia sempre os mesmos números, então a sua saída sai igual à da aula. O começo de cada programa conta o que ele calcula e, no `simular.py`, como os números nascem.

O exercício usa o estudo de orientação alimentar, em `../dados/nutricao`. Você escreve o seu próprio código no pandas; as dicas do exercício mostram por onde começar. Faça o exercício antes de abrir o `gerar.py` de lá.

No Windows, troque `python3` por `py`.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
