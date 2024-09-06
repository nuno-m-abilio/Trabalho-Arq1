# Trabalho-Arq1
Trabalho de implementação de um simulador para uma arquitetura simplificada com memória cache,
composta por um conjunto de instruções aritméticas, de desvio e de movimentação de dados entre 
registradores e memória, sendo orientado pelo Professor Nilton da disciplina de Arquitetura e
Organização de Computadores.

Alunos: Nuno Miguel Mendonça Abilio (ra132830) e Eduardo Angelo Rozada Minholi (ra134932)

Alguns detalhes de implementação:

-> Optamos por trabalhar com palavras (de 8 bytes) por linha na memória cache, sendo no máximo 128. Além 
disso, também configuramos a memória pricnipal com essa medida;

-> A forma de chamar o programa no terminal é na confirguração: python .\main.py 
'nomeDoArquivoDeOperações.txt' palavrasPorLinha LinhasPorConjunto numConjuntos tamMP

-> Ao exibir os valores de memória na tela, não restringimos apenas aos que estão sendo ocupados,
printamos todos;

-> No ciclo de instrução, ele não é executado pausadamente com interação no terminal. São todos 
executados e printados sequencialmente até o critério de parada, que necesse caso, é a tentativa de
executar uma instrução inválida (que acontece eventualmente pela sequência que PC aponta). Após isso,
o programa se encerra;

-> Algumas inconsistências podem acontecer por causa de instruções com endereços "inadequados", que 
apontam para instruções na MP em vez de dados, por exemplo, ou apontam para valores de memória fora do 
range de MP estipulados. Tudo o que posso pedir é atenção a esses detalhes para evitar erros, pois não é 
a proposta deste trabalho ter um código na arquitetura para evitá-los;

-> Falando sobre organização do código, é no arquivo arquitetura.py que estão a maioria das classes 
métodos e funções utilizadas no trabalho. Porém, é em main.py que são lidos e verificados os argumentos 
da linha de comando, além de inicializada a classe Arquitetura e chamados seus métodos mais "gerais";

-> Há diversas documentações e cometários em cada classe, método e função do código explicando sua 
motivação e funcinamento base. Além disso, apesar de longos, seus próprios nomes são bastante intuitivos.
Em caso de dúvidas, acredito que a leitura deles pode ser de grande ajuda!

Muito obrigado!