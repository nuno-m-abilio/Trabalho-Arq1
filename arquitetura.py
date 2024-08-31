class Instrucao:
    ''' Classe que representa uma Instrução a ser realizada/armazenada na Arquitetura. Cada
    instrução tem um Opcode que determina sua ação e até 3 valores de referência que utiliza para
    isso.'''

    Opcode:str
    a:int
    b:int
    c:int

    def __init__(self, instStr) -> None:
        ''' O construtor toma como entrada uma String e faz seu processamento, separando o Opcode
        dos valores referenciais. Para isso, considera-se que a string está no formato correto de
        "Opcode a, b, c". Para as operções que tem somente 1, 2 ou nenhum operador, os valores b e
        c ficam marcados com o valor inválido -1.
        
        >>> x = 'add r2, r31, r100'
        >>> y = Instrucao(x)
        >>> y.Opcode
        'add'
        >>> y.a
        2
        >>> y.b
        31
        >>> y.c
        100

        >>> x = 'lw r2, 31(r100)'
        >>> y = Instrucao(x)
        >>> y.Opcode
        'lw'
        >>> y.a
        2
        >>> y.b
        31
        >>> y.c
        100
        
        >>> x = 'not r2, r32'
        >>> y = Instrucao(x)
        >>> y.Opcode
        'not'
        >>> y.a
        2
        >>> y.b
        32
        >>> y.c
        -1

        >>> x = 'jal 0'
        >>> y = Instrucao(x)
        >>> y.Opcode
        'jal'
        >>> y.a
        0
        >>> y.b
        -1
        >>> y.c
        -1
        
        >>> x = 'ret'
        >>> y = Instrucao(x)
        >>> y.Opcode
        'ret'
        >>> y.a
        -1
        >>> y.b
        -1
        >>> y.c
        -1
        '''
        OpcodeAux = ''
        aAux:str = ''
        bAux:str = ''
        cAux:str = ''
        i:int = 0 
        tam:int = len(instStr)
        while i < tam and instStr[i] != ' ':
            OpcodeAux += instStr[i]
            i += 1
        i += 1 
        if i < tam:
            while i < tam and instStr[i] != ',':
                if instStr[i] != 'r':
                    aAux += instStr[i]
                i += 1
            i += 2
            if i < tam:
                while i < tam and instStr[i] != ',' and instStr[i] != '(':
                    if instStr[i] != 'r':
                        bAux += instStr[i]
                    i += 1
                i += 2
                if i < tam:
                    while i < tam  and instStr[i] != ')':
                        if instStr[i] != 'r':
                            cAux += instStr[i]
                        i += 1
                else:
                    cAux = '-1'
            else:
                bAux, cAux = '-1', '-1'
        else:
            aAux, bAux, cAux = '-1', '-1', '-1'
        self.Opcode = OpcodeAux
        self.a = int(aAux)
        self.b = int(bAux)
        self.c = int(cAux)

# class CicloDeInstrucao:
#     ''' Classe que representa um ciclo de instrução simplificado com 3 etapas: leitura, que
#     armazena uma string com a instrução lida; decodificacao, que armazena uma Instrucao com seus
#     campos devidamente definidos; e execucao, que efetivamente faz a ação da Instrucao que armazena.'''

#     leitura:str
#     decodificacao:Instrucao
#     execucao:Instrucao

#     def __init__(self) -> None:
#         ''' Construtor padrão com valores inválidos padrão.'''
#         self.leitura = ''
#         self.decodificacao = Instrucao('')
#         self.execucao = Instrucao('')
    
#     def rodar(self, newStrInst) -> None:
#         ''' Método que "roda" o ciclo de instrução: a instrução decodificada é executada e
#         armazenada em execucao, a lida é decodificada e armazenada em decodificacao e uma nova
#         instrução newStrInst é lida e armazenada em leitura.
        
#         >>> x = CicloDeInstrucao()
#         >>> x.rodar('add 2, 31, 100')
#         >>> x.leitura
#         'add 2, 31, 100'
#         >>> x.decodificacao.Opcode
#         ''
#         >>> x.execucao.Opcode
#         ''

#         >>> x.rodar('not 2, 32')
#         >>> x.leitura
#         'not 2, 32'
#         >>> x.decodificacao.Opcode
#         'add'
#         >>> x.execucao.Opcode
#         ''

#         >>> x.rodar('ret')
#         >>> x.leitura
#         'ret'
#         >>> x.decodificacao.Opcode
#         'not'
#         >>> x.execucao.Opcode
#         'add'
#         '''
#         if self.decodificacao.Opcode != '':
#             self.execucao = self.decodificacao
#             #Inserir função de execução dessa instrução na Arquitetura
#         if self.leitura != '':
#             self.decodificacao = Instrucao(self.leitura)
#         self.leitura = newStrInst

class CicloDeInstrucao:
    ''' Classe que representa um ciclo de instrução simplificado com 2 etapas: leitura, que
    armazena uma string com a instrução lida; e decodificacao + separação de operandos + execução, que armazena uma
    Instrucao com seus campos devidamente definidos e realiza efetivamente sua ação.'''

    leitura:str
    execucao:Instrucao

    def __init__(self) -> None:
        ''' Construtor padrão com valores inválidos padrão.'''
        self.leitura = ''
        self.execucao = Instrucao('')

class Processador:
    ''' Classe que representa o processador da Arquitetura, tendo como campos uma lista de inteiros
    que representa os 32 Registradores de Uso Geral, inteiros para representar o Contador de
    Programa (PC), Ponteiro da Pilha (RSP) e Endereço de Retorno (RA), além de um bool que indica
    se houve oveflow na última operação.'''

    registradores: list[int]
    PC:int
    RSP:int
    RA:int
    OF:bool

    def __init__(self) -> None:
        ''' Construtor padrão da classe Processador.'''
        self.Registradores = [0] * 32
        self.PC = 0
        self.RSP = 0
        self.RA = 0
        self.OF = False

class Arquitetura:
    ''' Classe que simulada uma arquitetura simplificada com memória cache, composta por um
    conjunto de instruções aritméticas, lógicas, de desvio e de movimentação de dados entre
    registradores e memória. Nela, há campos específicos para o processador, memória principal
    (MP), cache de instruções, cache de dados e ciclo de instrução.'''
    
    processador:Processador
    MP:list[list[int|str]]
    cacheInst:list[list[list[str]]]
    cacheDados:list[list[list[int]]]
    cicloDeInstrucao:CicloDeInstrucao

    def __init__(self, palavrasPorLinha:int, linhasPorConjunto:int, numConjuntos:int, tamMP:int) -> None:
        ''' Construtor padrão da arquitetura que inicializa o processador e o ciclo de instrução em
        suas formas padrão e as memórias princial e cache conforme os parâmetros passados na
        entrada. Ressalta-se aqui que a MP é dividida em blocos de tamanho igual às linhas da
        cache, existindo a possibilidade de haver um último bloco menor que os demais, mas sem que
        isso influencie na cache '''

        self.processador = Processador()
        self.MP = [[0] * palavrasPorLinha ] * int(tamMP / palavrasPorLinha)
        self.MP += [[0] * (tamMP % palavrasPorLinha)]
        self.cacheInst = [[[''] * palavrasPorLinha ] * linhasPorConjunto ] * numConjuntos
        self.cacheDados = [[[0] * palavrasPorLinha ] * linhasPorConjunto ] * numConjuntos
        self.cicloDeInstrucao = CicloDeInstrucao()
    
    def rodarInstrucao(self):
        ''' Método que vai ler e executar uma operação alterando o Ciclo de Instruções. Você decodifica a
        Instrução que está em leitura e coloca ela no espaço da execução, você executa ela mudando o PC,
        aí você lê uma nova operação segundo essa nova informação em PC e coloca la na leitura'''

        return None    