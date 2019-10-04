'''
Introdução:
- Implementar algoritmo de ordenação que receba uma colecão
- A coleção é uma lista de arestas
- Para comparar o peso as arestas entre dois item da coleção basta usar a chave 'weight' (peso)

Exemplos:
- Modo convencional
colecao[i] operador de comparacao colecao[j]
colecao[i] < colecao[j]

- Modo que você vai usar
int(colecao[i]['weight']) operador de comparacao int(colecao[j]['weight'])
int(colecao[i]['weight']) < int(colecao[j]['weight'])

É nescessário converter o valor pra Interger no momento da comparação a fim de evitar erros
'''

# Sua classe algoritmo de ordenação precisar ter um método ordenar
class InsertionSort(object):
	def ordenar(self, colecao):
		cont = 0
		for i in range(1, len(colecao)): # COMEÇA A PERCORRER A PARTIR DO SEGUNDO
			key = colecao[i]

			j = i - 1
			cont = cont + 1
			while j>=0 and int(key['weight']) < int(colecao[j]['weight']): # LAÇO PARA VOLTAR AS POSIÇÕES DOS DADOS COMPARADOS DA COLEÇÃO
				colecao[j+1] = colecao[j]
				j = j - 1

			colecao[j+1] = key

		return colecao

class SelectionSort(object):
	def ordenar(self, colecao):
		cont = 0
		for i in range(len(colecao)):
			
			min_idx = i # SELECIONA O PRIMEIRO DADO DA COLEÇÃO COMO MENOR
			
			for j in range(i+1, len(colecao)):
				cont = cont + 1
				if int(colecao[min_idx]['weight']) > int(colecao[j]['weight']): # LAÇO PARA PERCORRER A COLEÇÃO E COMPARAR PARA ACHAR UM MENOR
					min_idx = j
			
			colecao[i], colecao[min_idx] = colecao[min_idx], colecao[i]
		
		return colecao

class ShellSort(object):
	def ordenar(self, colecao):
		cont = 0
		n = len(colecao)
		gap = n//2

		while gap > 0:
			for i in range(gap, n):
				temp = colecao[i]
				j=i

				cont = cont + 1
				while j >= gap and int(colecao[j-gap]['weight']) > int(temp['weight']):
					colecao[j] = colecao[j-gap]
					j = j - gap

				colecao[j] = temp
			gap//=2

		return colecao

class MergeSort(object):
	def ordenar(self, colecao):
		cont = 0
		if len(colecao)>1:
			mid = int(len(colecao))//2 #divide o tamanho da colecao recebida em dois
			L = colecao[:mid] #pega o lado esquerdo da colecao
			R = colecao[mid:] #pega o lado direito da colecao

			self.ordenar(L) #ordena lado esquerdo
			self.ordenar(R) #ordena lado direito

			i = j = k = 0
			#compara as sub colecao
			while i < len(L) and j < len(R):
				cont = cont + 1
				if int(L[i]['weight']) < int(R[j]['weight']):
					colecao[k] = L[i]
					i = i + 1
				else:
					cont = cont + 1
					colecao[k] = R[j]
					j = j + 1
				k = k + 1

			while i < len(L):
				colecao[k] = L[i]
				i = i + 1
				k = k + 1

			while j < len(R):
				colecao[k] = R[j]
				j = j + 1
				k = k + 1

		return colecao

class QuickSort(object):
	def ordenar(self, colecao):
		#VERIFICA SE A COLEÇÃO E INICIA O METODO "TESTE" COM SEU INICIO (LOW) E FIM (HIGH)
		if colecao is not None:
			self.teste(colecao, 0, len(colecao)-1)
		return colecao
		#METODO RECURSIVO PARA ORDENAR A COLEÇÃO, SEJA ELA DIVIDIDA OU NÃO
	def teste(self, colecao, low, high):
		if low < high:
			pi = self.partition(colecao, low, high)
			self.teste(colecao, low, pi-1) #DIVIDE A COLEÇÃO PELA METADE
			self.teste(colecao, pi+1, high)	#DIVIDE A COLEÇÃO PELA METADE
		return colecao
		#RECEBE A COLEÇÃO DIVIDIDA OU NÃO
	def partition(self, colecao, low, high):
		cont = 0
		i = (low-1)
		pivot = colecao[high]

		for j in range(low, high):
			cont = cont + 1
			if int(colecao[j]['weight']) <= int(pivot['weight']):
				i = i + 1
				colecao[i], colecao[j] = colecao[j], colecao[i]

		colecao[i+1], colecao[high] = colecao[high], colecao[i+1]
		return (i+1)
