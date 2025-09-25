import sys

def insertionSort (array) :
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
# ------------------------------------------------------------------

def bubbleSort (array) :
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def selectionSort (array) :
    n = len(array)
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if array[j] < array[menor]:
                menor = j
        array[i], array[menor] = array[menor], array[i]
    return array
# ------------------------------------------------------------------

def mergeSort (array):
    if len(array) <= 1:
        return array
    
    meio = len(array) // 2
    esquerda = mergeSort (array[:meio])
    direita = mergeSort (array[meio:])
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado
# ------------------------------------------------------------------

def quickSort (array):
    if len(array) <= 1:
        return array
    
    pivo = array[len(array) // 2]
    esquerda = [x for x in array if x < pivo]
    meio = [x for x in array if x == pivo]
    direita = [x for x in array if x > pivo]
    
    return quickSort(esquerda) + meio + quickSort(direita)

def quickSort_inplace (array, baixo=0, alto=None):
    if alto is None:
        alto = len(array) - 1
    
    if baixo < alto:
        pi = partition(array, baixo, alto)
        quickSort_inplace(array, baixo, pi - 1)
        quickSort_inplace(array, pi + 1, alto)

def partition (array, baixo, alto):
    pivo = array[alto]
    i = baixo - 1
    
    for j in range(baixo, alto):
        if array[j] <= pivo:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[alto] = array[alto], array[i + 1]
    return i + 1
# ------------------------------------------------------------------

def heapSort (array):
    n = len(array)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    
    return array

def heapify (array, tamanho, raiz):
    maior = raiz
    esquerda = 2 * raiz + 1
    direita = 2 * raiz + 2
    
    if esquerda < tamanho and array[esquerda] > array[maior]:
        maior = esquerda
    
    if direita < tamanho and array[direita] > array[maior]:
        maior = direita
    
    if maior != raiz:
        array[raiz], array[maior] = array[maior], array[raiz]
        heapify(array, tamanho, maior)
# ------------------------------------------------------------------

def leitor (nome_arquivo):
    with open (nome_arquivo, 'r', encoding = 'utf-8') as arquivo_texto :
        conteudo = arquivo_texto.read()
    return conteudo
    




def main(args):
    print(f"Argumentos: {args}")
    print(leitor ('input1.txt'))
   


if __name__ == "__main__":
    main(sys.argv)