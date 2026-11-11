# Diagnóstico: por onde começar em Estatística para decisão

A Dani cuida da logística da Loja Exemplo. Em abril ela me mandou um resumo de março com três frases: "o atraso subiu 2%", "a entrega média levou 40 horas" e "no interior, quase metade das entregas passa de 48 horas". As três tinham número de verdade por trás, e as três estavam erradas de um jeito diferente. Antes de responder, eu refiz as contas dela. As cinco tarefas abaixo são essas contas.

Elas usam o que o curso pede de entrada: porcentagem, média e proporção feitas à mão, e um CSV lido, filtrado e agrupado no pandas. O diagnóstico não é prova e não tem nota. Ele mostra por onde você começa. Anote na [folha de respostas](minhas-respostas.md) a conta que fez, o comando que rodou e a saída que apareceu. Só depois compare com as respostas comentadas.

As tarefas 1, 2 e 5 são de lápis e papel ou calculadora. As tarefas 3 e 4 rodam de dentro da pasta `00-apresentacao/`:

```bash
cd 00-apresentacao
python3 tarefa4.py
```

No Windows, troque `python3` por `py`. Se uma conta travar, a [preparação de matemática](preparacao-matematica.md) tem um exemplo curto de cada uma.

## Tarefa 1. Porcentagem e ponto percentual

Em fevereiro, 20 das 250 entregas atrasaram. Em março, 30 das 300.

1. Qual a taxa de atraso de fevereiro e a de março, em porcentagem?
2. Quanto a taxa subiu, em pontos percentuais?
3. Quanto ela subiu em relação a fevereiro, em porcentagem?
4. A Dani escreveu "o atraso subiu 2%". O que está errado nessa frase e como você escreveria?

## Tarefa 2. Média de grupos de tamanhos diferentes

Em março, as 40 entregas do centro levaram em média 30 horas. As 10 entregas do interior levaram em média 50 horas.

1. Qual a média de horas das 50 entregas juntas?
2. A Dani escreveu 40 horas. De onde saiu esse número e por que ele não é a média das entregas?
3. Em que situação a média das duas médias daria o número certo?

## Tarefa 3. Entregas por região no pandas

`dados/entregas_marco.csv` tem 16 entregas de março. Uma linha é uma entrega. A coluna `horas` é o tempo do pedido até a baixa; quando a baixa não foi anotada, a célula fica vazia.

Em `tarefa3.py`, monte uma tabela com uma linha por região e estas colunas:

| Coluna | O que é |
|---|---|
| `regiao` | centro ou interior |
| `entregas` | quantas entregas a região teve, contando as sem baixa |
| `sem_baixa` | quantas estão com `horas` vazia |
| `media_horas` | média das horas que existem, com uma casa decimal |
| `ate_48h_pct` | entre as entregas com horas anotadas, a porcentagem que levou até 48 horas, com uma casa decimal |

Guarde a tabela final na variável `resultado` e mostre com `print(resultado)`. Anote na folha:

1. Qual o denominador de `ate_48h_pct` no interior?
2. O que aconteceria com `media_horas` e com `ate_48h_pct` se você trocasse o vazio por zero?
3. A frase da Dani sobre o interior está certa com esses dados? O que você diria no lugar?

## Tarefa 4. Ler um programa e prever a saída

Abra `tarefa4.py` e leia tudo antes de rodar. Anote na folha as duas linhas que ele vai mostrar. Depois rode e compare.

Responda também:

1. Por que só um tíquete fica acima da média?
2. Quando o tíquete de R$ 2.400,00 sai, a média cai muito e a mediana quase não muda. Por quê?
3. Se a pergunta fosse "quanto um cliente comum gasta", qual dos dois números você mandaria?

## Tarefa 5. Proporção e denominador

Das 200 entregas de março, 50 atrasaram. Houve 40 reclamações, uma por entrega, e 30 delas foram de entregas atrasadas.

1. Que porcentagem das entregas teve reclamação?
2. Que porcentagem das reclamações veio de entrega atrasada?
3. Que porcentagem das entregas atrasadas teve reclamação?
4. Que porcentagem das entregas no prazo teve reclamação?
5. A Dani concluiu: "75% das entregas atrasadas geram reclamação". Qual das suas contas responde a essa frase e qual o número certo?

## Depois das tarefas

Compare a folha com as respostas comentadas e veja a tabela da apresentação do curso. Ela diz que aula de Primeiros passos em dados ou que trecho da preparação estudar para cada tarefa em que você travou.

Se precisar de ajuda, deixe um comentário na aula. Conte o objetivo, o comando que você rodou, a saída que apareceu e o que já tentou, sem dados pessoais.
