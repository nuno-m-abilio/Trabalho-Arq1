def fatorial(x):
    if x == 0:
        fat = 1
    else:
       fat = x * fatorial(x-1)
    return fat

# Criar estrutura [(pais, ouro prata, broze, total), (pais, ouro prata, broze, total)]
# Começa vazia []
# Lendo a lista temos que ir colocando as informações relevantes aqui.
# Primeiramente, temos que conferir se o páis já está nessa nova tabela. Caso esteja,
# acrescentamos o valor da medalha. Caso, não, criamos um novo país com a medalha (ou
# criamos um pais "vazio" e depois acrescentamos a medalha)
# Fazer isso várias vezes até acabar as medalhas.
# Agora, onde encaixar recursão?
