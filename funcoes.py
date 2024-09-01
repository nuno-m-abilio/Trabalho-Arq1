import io
import arquitetura as arq

def blocoNaMP(arquitetura:arq.Arquitetura, endereco:int) -> int:
    return endereco // arquitetura.infoMemoria[0]
        
def localNoBlocoNaMP(arquitetura:arq.Arquitetura, endereco:int) -> int:
    return endereco % arquitetura.infoMemoria[0]

def carregarInstrEmMP(arquitetura:arq.Arquitetura, arquivoDeOperacoes:io.TextIOWrapper) -> None:
    return None
    