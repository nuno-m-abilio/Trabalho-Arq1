import arquitetura as arq
import argparse
import io

# Configurando a chamada dos argumentos na linha de comando
parser = argparse.ArgumentParser()
parser.add_argument('arquivoDeOperacoes', type=str)
parser.add_argument('palavrasPorLinha', type=int)
parser.add_argument('linhasPorConjunto', type=int)
parser.add_argument('numConjuntos', type=int)
parser.add_argument('tamMP', type=int)
args = parser.parse_args()


def main(arquivoDeOperacoes:io.TextIOWrapper, palavrasPorLinha:int, linhasPorConjunto:int, numConjuntos:int, tamMP:int):
    print('"Inicializando simulador de arquitetura simplificada com memória cache"\n')

    while palavrasPorLinha < 1 or palavrasPorLinha > 128:
        palavrasPorLinha = int(input('Valor de palavras por linha da cache inválido. O valor deve'
        'ser um inteiro entre 1 e 128. Por favor, insirar um valor correto:\n'))
    
    totalPalavrasCache = palavrasPorLinha * linhasPorConjunto * numConjuntos

    while tamMP <= (totalPalavrasCache):
        tamMP = int(input('Valor de palavras da memória principal inválido. O valor deve'
        'ser maior que o total de palavras da cache (%d). Por favor, insirar um valor correto:\n' % totalPalavrasCache))

    print('Informações de memória:')
    print('-> %d palavras por linha;' % palavrasPorLinha)
    print('-> %d linhas por conjunto;' % linhasPorConjunto)
    print('-> %d conjuntos;' % numConjuntos)
    print('-> %d palavras na memória principal;\n' % tamMP)

    arquitetura = arq.Arquitetura(palavrasPorLinha, linhasPorConjunto, numConjuntos, tamMP)

    

if __name__ == '__main__':
    arquivoDeOperacoes = open(args.arquivoDeOperacoes, 'rt') 
    main(arquivoDeOperacoes, args.palavrasPorLinha, args.linhasPorConjunto, args.numConjuntos, args.tamMP)