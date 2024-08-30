import arquitetura as arq

def executaInstrucao(instrucao:arq.Instrucao, arquitetura:arq.Arquitetura) -> None:
    '''Função que executa as instruções.'''
    match instrucao.Opcode:
        case 'add':
            arquitetura.processador.registradores[instrucao.a] = arquitetura.processador.registradores[instrucao.b] + arquitetura.processador.registradores[instrucao.c]
            arquitetura.processador.PC += 1
        case _:
            print('Operação Inválida')