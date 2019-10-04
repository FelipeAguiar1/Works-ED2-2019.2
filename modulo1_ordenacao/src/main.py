from grafo import Grafo
from algoritmosDeOrdenacao import *
from utils import *

'''
Implemente o algoritmo de ordenação no arquivo algoritmosDeOrdenacao.py
Instruções básicas de como fazer a implementação estão no arquivo algoritmosDeOrdenacao.py
'''

if __name__ == "__main__":
# MENU PARA ORDENAÇÃO DA COLEÇÃO
	print("Operações com ordenação: ")
	print("[1] InsertionSort")
	print("[2] MergeSort")
	print("[3] QuickSort")
	print("[4] SelectionSort")
	print("[5] ShellSort")
	op = int(input("Digite: "))
# FUNÇÃO PARA BUSCAR ARQUIVO
	arquivoJson = acaoArquivo(op)
	if op==1:
		algoritimoDeOrdenacao = InsertionSort()
		print("")
		print("InsertionSort será executado...")
	if op==2:
		algoritimoDeOrdenacao = MergeSort()
		print("")
		print("MergeSort será executado...")
	if op==3:
		algoritimoDeOrdenacao = QuickSort()
		print("")
		print("QuickSort será executado...")
	if op==4:
		algoritimoDeOrdenacao = SelectionSort()
		print("")
		print("SelectionSort será executado...")
	if op==5:
		algoritimoDeOrdenacao = ShellSort()
		print("")
		print("ShellSort será executado...")
# FUNÇÃO PARA ENCAMINHAR ARQUIVO
	arquivoDeSaida = arquivoDest(arquivoJson)
	print("Encontre o arquivo ordenado em: ", arquivoDeSaida)

	grafo = Grafo()
	grafo.estabelecerAlgoritmoDeOrdencao(algoritimoDeOrdenacao)
	grafo.carregarGrafo(arquivoJson)

	arvoreGeradoraMinima =  grafo.executarKruskal()
	SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima)
