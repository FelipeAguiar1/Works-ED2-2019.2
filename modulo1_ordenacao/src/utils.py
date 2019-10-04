from algoritmosDeOrdenacao import *

def SalvarArvoreGeradoraMinimaEmArquivo(arquivoDeSaida, arvoreGeradoraMinima):
    with open(arquivoDeSaida, 'w') as arquivo:
        for aresta in arvoreGeradoraMinima:
            arquivo.write('fonte: {}, destino: {}, peso: {}\n'.format(aresta['source'], aresta['target'], aresta['weight']))
# BUSCANDO ARQUIVO PARA PEGAR COLEÇÃO
def acaoArquivo(n):
	if n==1:
		print("Opções para ordenar: ")
		print("[1] 7 vértices")
		print("[2] 100 vértices")
		print("[3] 1000 vértices")
		print("[4] 10000 vértices")
		print("[5] 100000 vértices")
		num = int(input("Digite: "))

		algoritimoDeOrdenacao = InsertionSort()
		if num==1:
			arquivoJson = 'grafos/7vertices.json'
		elif num==2:
			arquivoJson = 'grafos/100vertices.json'
		elif num==3:
			arquivoJson = 'grafos/1000vertices.json'
		elif num==4:
			arquivoJson = 'grafos/10000vertices.json'
		elif num==5:
			arquivoJson = 'grafos/100000vertices.json'
		return arquivoJson

	if n==2:
		print("Opções para ordenar: ")
		print("[1] 7 vértices")
		print("[2] 100 vértices")
		print("[3] 1000 vértices")
		print("[4] 10000 vértices")
		print("[5] 100000 vértices")
		num1 = int(input("Digite: "))

		algoritimoDeOrdenacao = MergeSort()
		if num1==1:
			arquivoJson = 'grafos/7vertices.json'
		elif num1==2:
			arquivoJson = 'grafos/100vertices.json'
		elif num1==3:
			arquivoJson = 'grafos/1000vertices.json'
		elif num1==4:
			arquivoJson = 'grafos/10000vertices.json'
		elif num1==5:
			arquivoJson = 'grafos/100000vertices.json'
		return arquivoJson

	if n==3:
		print("Opções para ordenar: ")
		print("[1] 7 vértices")
		print("[2] 100 vértices")
		print("[3] 1000 vértices")
		print("[4] 10000 vértices")
		print("[5] 100000 vértices")
		num2 = int(input("Digite: "))

		algoritimoDeOrdenacao = QuickSort()
		if num2==1:
			arquivoJson = 'grafos/7vertices.json'
		elif num2==2:
			arquivoJson = 'grafos/100vertices.json'
		elif num2==3:
			arquivoJson = 'grafos/1000vertices.json'
		elif num2==4:
			arquivoJson = 'grafos/10000vertices.json'
		elif num2==5:
			arquivoJson = 'grafos/100000vertices.json'
		return arquivoJson

	if n==4:
		print("Opções para ordenar: ")
		print("[1] 7 vértices")
		print("[2] 100 vértices")
		print("[3] 1000 vértices")
		print("[4] 10000 vértices")
		print("[5] 100000 vértices")
		num3 = int(input("Digite: "))

		algoritimoDeOrdenacao = SelectionSort()
		if num3==1:
			arquivoJson = 'grafos/7vertices.json'
		elif num3==2:
			arquivoJson = 'grafos/100vertices.json'
		elif num3==3:
			arquivoJson = 'grafos/1000vertices.json'
		elif num3==4:
			arquivoJson = 'grafos/10000vertices.json'
		elif num3==5:
			arquivoJson = 'grafos/100000vertices.json'
		return arquivoJson

	if n==5:
		print("Opções para ordenar: ")
		print("[1] 7 vértices")
		print("[2] 100 vértices")
		print("[3] 1000 vértices")
		print("[4] 10000 vértices")
		print("[5] 100000 vértices")
		num4 = int(input("Digite: "))

		algoritimoDeOrdenacao = ShellSort()
		if num4==1:
			arquivoJson = 'grafos/7vertices.json'
		elif num4==2:
			arquivoJson = 'grafos/100vertices.json'
		elif num4==3:
			arquivoJson = 'grafos/1000vertices.json'
		elif num4==4:
			arquivoJson = 'grafos/10000vertices.json'
		elif num4==5:
			arquivoJson = 'grafos/100000vertices.json'
		return arquivoJson
# ARQUIVO DESTINO
def arquivoDest(arquivoJson):
	if arquivoJson == 'grafos/7vertices.json':
		return 'arvores_geradas/mst7Vertices.txt'
	elif arquivoJson == 'grafos/100vertices.json':
		return 'arvores_geradas/mst100Vertices.txt'
	elif arquivoJson == 'grafos/1000vertices.json':
		return 'arvores_geradas/mst1000Vertices.txt'
	elif arquivoJson == 'grafos/10000vertices.json':
		return 'arvores_geradas/mst10000Vertices.txt'
	elif arquivoJson == 'grafos/100000vertices.json':
		return 'arvores_geradas/mst100000Vertices.txt'

