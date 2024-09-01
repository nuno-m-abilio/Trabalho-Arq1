import arquitetura as arq
import funcoes

def executaInstrucao(instrucao:arq.Instrucao, arquitetura:arq.Arquitetura) -> None:
    '''Função que executa as instruções.'''
    match instrucao.Opcode:
        case 'add':
            arquitetura.processador.registradores[instrucao.a] = arquitetura.processador.registradores[instrucao.b] + arquitetura.processador.registradores[instrucao.c]
            arquitetura.processador.PC += 1
        case 'addi':
            arquitetura.processador.registradores[instrucao.a] = arquitetura.processador.registradores[instrucao.b] + instrucao.c
            arquitetura.processador.PC += 1
        case 'sub':
            arquitetura.processador.registradores[instrucao.a] = arquitetura.processador.registradores[instrucao.b] - arquitetura.processador.registradores[instrucao.c]
            arquitetura.processador.PC += 1
        case 'subi':
            arquitetura.processador.registradores[instrucao.a] = arquitetura.processador.registradores[instrucao.b] - instrucao.c
            arquitetura.processador.PC += 1
        case 'mul':
            arquitetura.processador.registradores[instrucao.a] = arquitetura.processador.registradores[instrucao.b] * arquitetura.processador.registradores[instrucao.c]
            arquitetura.processador.PC += 1
        case 'div':
            arquitetura.processador.registradores[instrucao.a] = arquitetura.processador.registradores[instrucao.b] // arquitetura.processador.registradores[instrucao.c]
            arquitetura.processador.PC += 1
        case 'not':
            arquitetura.processador.registradores[instrucao.a] = ~ arquitetura.processador.registradores[instrucao.b]
            arquitetura.processador.PC += 1
        case 'or':
            arquitetura.processador.registradores[instrucao.a] = arquitetura.processador.registradores[instrucao.b] & arquitetura.processador.registradores[instrucao.c]
            arquitetura.processador.PC += 1
        case 'and':
            arquitetura.processador.registradores[instrucao.a] = arquitetura.processador.registradores[instrucao.b] | arquitetura.processador.registradores[instrucao.c]
            arquitetura.processador.PC += 1
        case 'blti':
            if arquitetura.processador.registradores[instrucao.a] < arquitetura.processador.registradores[instrucao.b]:
                arquitetura.processador.PC = instrucao.c
            else:
                arquitetura.processador.PC += 1
        case 'bgti':
            if arquitetura.processador.registradores[instrucao.a] > arquitetura.processador.registradores[instrucao.b]:
                arquitetura.processador.PC = instrucao.c
            else:
                arquitetura.processador.PC += 1
        case 'beqi':
            if arquitetura.processador.registradores[instrucao.a] == arquitetura.processador.registradores[instrucao.b]:
                arquitetura.processador.PC = instrucao.c
            else:
                arquitetura.processador.PC += 1
        case 'blt':
            if arquitetura.processador.registradores[instrucao.a] < arquitetura.processador.registradores[instrucao.b]:
                arquitetura.processador.PC = arquitetura.processador.registradores[instrucao.c]
            else:
                arquitetura.processador.PC += 1
        case 'bgt':
            if arquitetura.processador.registradores[instrucao.a] > arquitetura.processador.registradores[instrucao.b]:
                arquitetura.processador.PC = arquitetura.processador.registradores[instrucao.c]
            else:
                arquitetura.processador.PC += 1
        case 'beq':
            if arquitetura.processador.registradores[instrucao.a] == arquitetura.processador.registradores[instrucao.b]:
                arquitetura.processador.PC = arquitetura.processador.registradores[instrucao.c]
            else:
                arquitetura.processador.PC += 1
        case 'jr':
            arquitetura.processador.PC = arquitetura.processador.registradores[instrucao.a]
        case 'jof':
            if arquitetura.processador.OF:
                arquitetura.processador.PC = arquitetura.processador.registradores[instrucao.a]
        case 'jal':
            arquitetura.processador.RA = arquitetura.processador.PC + 1
            arquitetura.processador.PC = instrucao.a
        case 'ret':
            arquitetura.processador.PC = arquitetura.processador.RA
        case 'lw':
            aux = arquitetura.MP[funcoes.blocoNaMP(arquitetura, instrucao.b + arquitetura.processador.registradores[instrucao.c])][funcoes.localNoBlocoNaMP(arquitetura, instrucao.b + arquitetura.processador.registradores[instrucao.c])]
            if type(aux) == int:
                arquitetura.processador.registradores[instrucao.a] = aux
            arquitetura.processador.PC += 1
        case 'sw':
            arquitetura.MP[funcoes.blocoNaMP(arquitetura, instrucao.b + arquitetura.processador.registradores[instrucao.c])][funcoes.localNoBlocoNaMP(arquitetura, instrucao.b + arquitetura.processador.registradores[instrucao.c])] = arquitetura.processador.registradores[instrucao.a]
            arquitetura.processador.PC += 1
        case 'mov':
            arquitetura.processador.registradores[instrucao.a] = arquitetura.processador.registradores[instrucao.b]
            arquitetura.processador.PC += 1
        case 'movi':
            arquitetura.processador.registradores[instrucao.a] = instrucao.b
            arquitetura.processador.PC += 1
        case _:
            print('Operação Inválida')
            arquitetura.processador.PC += 1