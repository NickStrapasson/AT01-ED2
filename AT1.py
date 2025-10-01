import sys
import random as rd
import time
import copy

# Função de ordenação Insertion Sort
def insertionSort(array):
    array_copia = copy.deepcopy(array)
    tempoInicial = time.perf_counter()
    comparacoes = 0
    
    for i in range(1, len(array_copia)):
        key = array_copia[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if array_copia[j] > key:
                array_copia[j + 1] = array_copia[j]
                j -= 1
            else:
                break
        array_copia[j + 1] = key
    
    tempoFinal = time.perf_counter()
    tempo_execucao = (tempoFinal - tempoInicial) * 1000  # Converter para milissegundos
    return array_copia, tempo_execucao, comparacoes

# Função Bubble Sort
def bubbleSort(array):
    array_copia = copy.deepcopy(array)
    tempoInicial = time.perf_counter()
    comparacoes = 0
    n = len(array_copia)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1
            if array_copia[j] > array_copia[j + 1]:
                array_copia[j], array_copia[j + 1] = array_copia[j + 1], array_copia[j]
    
    tempoFinal = time.perf_counter()
    tempo_execucao = (tempoFinal - tempoInicial) * 1000
    return array_copia, tempo_execucao, comparacoes

# Função Selection Sort
def selectionSort(array):
    array_copia = copy.deepcopy(array)
    tempoInicial = time.perf_counter()
    comparacoes = 0
    n = len(array_copia)
    
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if array_copia[j] < array_copia[menor]:
                menor = j
        array_copia[i], array_copia[menor] = array_copia[menor], array_copia[i]
    
    tempoFinal = time.perf_counter()
    tempo_execucao = (tempoFinal - tempoInicial) * 1000
    return array_copia, tempo_execucao, comparacoes

# Função Merge Sort
def mergeSort(array):
    def merge_sort_recursive(arr, comparacoes_ref):
        if len(arr) <= 1:
            return arr
        
        meio = len(arr) // 2
        esquerda = merge_sort_recursive(arr[:meio], comparacoes_ref)
        direita = merge_sort_recursive(arr[meio:], comparacoes_ref)
        
        return merge(esquerda, direita, comparacoes_ref)

    def merge(esquerda, direita, comparacoes_ref):
        resultado = []
        i = j = 0
        
        while i < len(esquerda) and j < len(direita):
            comparacoes_ref[0] += 1
            if esquerda[i] <= direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
        
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado

    array_copia = copy.deepcopy(array)
    tempoInicial = time.perf_counter()
    comparacoes_ref = [0]
    
    array_ordenado = merge_sort_recursive(array_copia, comparacoes_ref)
    
    tempoFinal = time.perf_counter()
    tempo_execucao = (tempoFinal - tempoInicial) * 1000
    return array_ordenado, tempo_execucao, comparacoes_ref[0]

# Função Quick Sort (não in-place)
def quickSort(array):
    def quick_sort_recursive(arr, comparacoes_ref):
        if len(arr) <= 1:
            return arr
        
        pivo = arr[len(arr) // 2]
        esquerda = []
        meio = []
        direita = []
        
        for x in arr:
            comparacoes_ref[0] += 1
            if x < pivo:
                esquerda.append(x)
            elif x == pivo:
                meio.append(x)
            else:
                direita.append(x)
        
        return (quick_sort_recursive(esquerda, comparacoes_ref) + 
                meio + 
                quick_sort_recursive(direita, comparacoes_ref))

    array_copia = copy.deepcopy(array)
    tempoInicial = time.perf_counter()
    comparacoes_ref = [0]
    
    array_ordenado = quick_sort_recursive(array_copia, comparacoes_ref)
    
    tempoFinal = time.perf_counter()
    tempo_execucao = (tempoFinal - tempoInicial) * 1000
    return array_ordenado, tempo_execucao, comparacoes_ref[0]

# Função Quick Sort in-place
def quickSort_inplace(array):
    def partition(arr, baixo, alto, comparacoes_ref):
        pivo = arr[alto]
        i = baixo - 1
        
        for j in range(baixo, alto):
            comparacoes_ref[0] += 1
            if arr[j] <= pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
        return i + 1

    def quick_sort_inplace_recursive(arr, baixo, alto, comparacoes_ref):
        if baixo < alto:
            pi = partition(arr, baixo, alto, comparacoes_ref)
            quick_sort_inplace_recursive(arr, baixo, pi - 1, comparacoes_ref)
            quick_sort_inplace_recursive(arr, pi + 1, alto, comparacoes_ref)

    array_copia = copy.deepcopy(array)
    tempoInicial = time.perf_counter()
    comparacoes_ref = [0]
    
    if len(array_copia) > 0:
        quick_sort_inplace_recursive(array_copia, 0, len(array_copia) - 1, comparacoes_ref)
    
    tempoFinal = time.perf_counter()
    tempo_execucao = (tempoFinal - tempoInicial) * 1000
    return array_copia, tempo_execucao, comparacoes_ref[0]

# Função Heap Sort
def heapSort(array):
    def heapify(arr, tamanho, raiz, comparacoes_ref):
        maior = raiz
        esquerda = 2 * raiz + 1
        direita = 2 * raiz + 2
        
        if esquerda < tamanho:
            comparacoes_ref[0] += 1
            if arr[esquerda] > arr[maior]:
                maior = esquerda
        
        if direita < tamanho:
            comparacoes_ref[0] += 1
            if arr[direita] > arr[maior]:
                maior = direita
        
        if maior != raiz:
            arr[raiz], arr[maior] = arr[maior], arr[raiz]
            heapify(arr, tamanho, maior, comparacoes_ref)

    array_copia = copy.deepcopy(array)
    tempoInicial = time.perf_counter()
    comparacoes_ref = [0]
    n = len(array_copia)
    
    # Construir heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(array_copia, n, i, comparacoes_ref)
    
    # Extrair elementos do heap um por um
    for i in range(n - 1, 0, -1):
        array_copia[i], array_copia[0] = array_copia[0], array_copia[i]
        heapify(array_copia, i, 0, comparacoes_ref)
    
    tempoFinal = time.perf_counter()
    tempo_execucao = (tempoFinal - tempoInicial) * 1000
    return array_copia, tempo_execucao, comparacoes_ref[0]

# Função Cycle Sort
def cycleSort(array):
    array_copia = copy.deepcopy(array)
    tempoInicial = time.perf_counter()
    comparacoes = 0
    n = len(array_copia)
    
    # Percorre o array para encontrar ciclos
    for inicio_ciclo in range(0, n - 1):
        item = array_copia[inicio_ciclo]
        
        # Encontra a posição correta do item
        pos = inicio_ciclo
        for i in range(inicio_ciclo + 1, n):
            comparacoes += 1
            if array_copia[i] < item:
                pos += 1
        
        # Se o item já está na posição correta, pula
        if pos == inicio_ciclo:
            continue
        
        # Ignora duplicatas
        while item == array_copia[pos]:
            comparacoes += 1
            pos += 1
        
        # Coloca o item na posição correta
        array_copia[pos], item = item, array_copia[pos]
        
        # Rotaciona o resto do ciclo
        while pos != inicio_ciclo:
            pos = inicio_ciclo
            
            # Encontra a posição do elemento deslocado
            for i in range(inicio_ciclo + 1, n):
                comparacoes += 1
                if array_copia[i] < item:
                    pos += 1
            
            # Ignora duplicatas
            while item == array_copia[pos]:
                comparacoes += 1
                pos += 1
            
            # Coloca o item na posição correta
            array_copia[pos], item = item, array_copia[pos]
    
    tempoFinal = time.perf_counter()
    tempo_execucao = (tempoFinal - tempoInicial) * 1000
    return array_copia, tempo_execucao, comparacoes

# Função para ler arquivo de entrada
def leitor(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_texto:
        conteudo = arquivo_texto.readlines()
        conteudo = [line.strip() for line in conteudo]
    return conteudo

# Função para gerar vetor conforme especificação do arquivo de entrada
def geraVetor(array_input):
    tamanho = int(array_input[0])
    
    if tamanho < 0:
        print("Erro: Não é possível gerar vetor com tamanho negativo")
        return None
    
    array = [0] * tamanho
    
    if array_input[1] == 'c':  # crescente
        for i in range(1, len(array) + 1, 1):
            array[i - 1] = i
    
    elif array_input[1] == 'd':  # decrescente
        for i in range(int(array_input[0]), 0, -1):
            array[len(array) - i] = i
    
    elif array_input[1] == 'r':  # randômico
        for i in range(0, len(array)):
            array[i] = rd.randint(0, 32000)
    
    else:
        print("Erro ao gerar o vetor, confira o formato do input")
        return None
    
    return array

# Função para escrever resultado em arquivo de saída
def escrever_resultado(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)

# Função principal do programa
def main(args):
    # Verifica se os argumentos no Bash foram passados corretamente
    if len(args) < 3:
        print("Uso: python programa.py [arquivo_de_entrada] [arquivo_de_saida]")
        return
    
    arquivo_entrada = args[1]
    arquivo_saida = args[2]
    
    print(f"Arquivo de entrada: {arquivo_entrada}")
    print(f"Arquivo de saída: {arquivo_saida}")
    
    try:
        # Lê os dados do arquivo de entrada
        dados_entrada = leitor(arquivo_entrada)
        vetor_original = geraVetor(dados_entrada)
        
        if vetor_original is None:
            return
        
        resultado_texto = ""
        
        # Dicionário com os algoritmos de ordenação
        algoritmos = {
            "Insertion Sort": insertionSort,
            "Bubble Sort": bubbleSort,
            "Selection Sort": selectionSort,
            "Merge Sort": mergeSort,
            "Quick Sort": quickSort,
            "Quick Sort In-place": quickSort_inplace,
            "Heap Sort": heapSort,
            "Cycle Sort": cycleSort
        }
        
        # Executar cada algoritmo e coletar resultados
        for nome_algoritmo, funcao_algoritmo in algoritmos.items():
            try:
                array_ordenado, tempo, comparacoes = funcao_algoritmo(vetor_original)
                resultado_texto += f"{nome_algoritmo}: {array_ordenado}, {comparacoes} comp, {tempo:.6f} ms\n"
                print(f"{nome_algoritmo} concluído")
                
            except Exception as e:
                resultado_texto += f"{nome_algoritmo}: Erro na execução: {str(e)}\n"
                print(f"Erro em {nome_algoritmo}: {str(e)}")
        
        # Escrever resultados no arquivo de saída
        escrever_resultado(arquivo_saida, resultado_texto)
        print(f"Resultados salvos em '{arquivo_saida}'")
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
    except Exception as e:
        print(f"Erro durante a execução: {str(e)}")

# Executa o programa se for chamado diretamente
if __name__ == "__main__":
    main(sys.argv)
