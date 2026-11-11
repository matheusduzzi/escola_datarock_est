# Kit do curso Estatística para decisão

Os arquivos que você usa nas aulas: o diagnóstico, a preparação de matemática, os tíquetes e as entregas da Loja Exemplo e o estudo de orientação alimentar das aulas 39 e 40.

## Como o kit está organizado

| Pasta | O que tem |
|---|---|
| `00-apresentacao/` | O [diagnóstico](00-apresentacao/diagnostico.md), a [preparação de matemática](00-apresentacao/preparacao-matematica.md), os dados e programas das tarefas, a [folha de respostas](00-apresentacao/minhas-respostas.md), a [folha da ordem de estudo](00-apresentacao/minha-ordem.md) e o `primeira_olhada.py` da apresentação. |
| `dados/loja/` | Tíquetes de 400 pedidos e horas de 48 entregas da Loja Exemplo. Ver [dados/loja/LEIA-ME.md](dados/loja/LEIA-ME.md). |
| `dados/nutricao/` | Postos, participantes e medidas do estudo de orientação alimentar. Ver [dados/nutricao/LEIA-ME.md](dados/nutricao/LEIA-ME.md). |
| `NN-titulo/` | Uma pasta por aula, com o número e o título da aula. Elas entram no kit junto com as aulas. |

Os comandos das aulas rodam de dentro da pasta da aula. Quando uma aula usa uma base compartilhada, ela diz o caminho, por exemplo `../dados/loja/entregas.csv`.

## Do que você precisa

- Python 3.9 ou mais novo, com o pandas. É o ambiente de Primeiros passos em dados: SQL e Python para quem está migrando; se você ainda não preparou o seu, a aula 03. Preparar o ambiente, de lá, mostra como.
- Um editor de código e um terminal.

O NumPy vem junto com o pandas. O SciPy, que faz os testes e as distribuições, e a biblioteca de gráficos entram nas aulas que usam cada um, com a versão e o comando de instalação. As aulas mostram o código pronto e explicam linha por linha o que ele calcula: o foco é o raciocínio, não escrever a implementação sozinho.

Na pasta do kit, instale o que o diagnóstico usa:

```bash
python3 -m pip install -r requirements.txt
```

E veja se funcionou:

```bash
cd 00-apresentacao
python3 tarefa4.py
```

A saída tem duas linhas de números. Não olhe ainda: a tarefa 4 do diagnóstico pede para você prever essas linhas antes de rodar. Se aparecer `No module named 'pandas'`, o `pip` instalou em outro Python. Rode `python3 -m pip install pandas` com o mesmo `python3` que você usa para rodar o programa. No Windows, troque `python3` por `py`.

Para gerar de novo as bases compartilhadas:

```bash
cd ../dados/loja
python3 gerar.py
cd ../nutricao
python3 gerar.py
```

As saídas são `tiquetes=400 entregas=48 entregas_sem_baixa=3` e `postos=8 participantes=240 medidas=456 sem_semana_12=24`. Os dois geradores só usam a biblioteca padrão e saem iguais toda vez.

## Se precisar de ajuda

Deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.

## Licença

A licença de uso e redistribuição do kit ainda vai ser definida pela Escola Datarock. Até lá, use os arquivos para estudar o curso. Os dados da Loja Exemplo e do estudo de orientação alimentar são inventados e foram gerados pelos programas do próprio kit.

## Aulas com arquivos neste kit

| Pasta | Aula |
|---|---|
| [00-apresentacao/](00-apresentacao/) | Apresentação |
| [01-o-que-queremos-estimar/](01-o-que-queremos-estimar/) | O que queremos estimar |
| [02-como-a-amostra-foi-formada/](02-como-a-amostra-foi-formada/) | Como a amostra foi formada |
| [11-revisar-uma-conclusao-causal/](11-revisar-uma-conclusao-causal/) | Revisar uma conclusão causal |
| [12-eventos-e-regras-de-probabilidade/](12-eventos-e-regras-de-probabilidade/) | Eventos e regras de probabilidade |
