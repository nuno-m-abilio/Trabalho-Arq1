import io, arquitetura as arq

#Bloco
def blocoNaMP(arquitetura:arq.Arquitetura, endereco:int) -> int:
    return endereco // arquitetura.infoMemoria[0]

#Palavra
def localNoBloco(arquitetura:arq.Arquitetura, endereco:int) -> int:
    return endereco % arquitetura.infoMemoria[0]

#Conjunto
def conjNaCache(arquitetura:arq.Arquitetura, endereco:int) -> int:
    return blocoNaMP(arquitetura, endereco) % arquitetura.infoMemoria[2]

# tag
def tag(arquitetura:arq.Arquitetura, endereco:int) -> int:
    return blocoNaMP(arquitetura, endereco) // arquitetura.infoMemoria[2]

def carregarInstrEmMP(arquitetura:arq.Arquitetura, arquivoDeOperacoes:io.TextIOWrapper) -> None:
    instLida:str = arquivoDeOperacoes.readline().strip()
    i:int = 0
    while instLida != '':
        arquitetura.MP[blocoNaMP(arquitetura, i)][localNoBloco(arquitetura, i)] = instLida
        instLida = arquivoDeOperacoes.readline().strip()
        i += 1