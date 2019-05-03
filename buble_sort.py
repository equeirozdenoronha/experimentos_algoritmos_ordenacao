import psutil
import time

def bubbleSort(alist):
    inicio = time.time()
    trocas = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                trocas = trocas +1
                alist[i+1] = temp
    fim = time.time()

    cpu_usage = psutil.cpu_percent()
    memory_usage = dict(psutil.virtual_memory()._asdict())
    print('------------------------ Bubble Sort ------------------------')
    print("Quantidade de Trocas: ", trocas)
    print("Tempo de Início: ", inicio / 60 / 60 / 60 / 60)
    print("Tempo de Fim: ", fim / 60 / 60 / 60 / 60)
    print("Tempo de Execução: ", fim - inicio)
    print("CPU: ", cpu_usage)
    print("RAM: ", memory_usage, "\n")

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

def bubble_sort_1(vetor):
    inicio = time.time()
    trocas = 0
    for i in range(len(vetor)):
        for j in range(i):
            if(vetor[j]>vetor[j+1]):
                aux = vetor[j]
                vetor[j]=vetor[j+1]
                trocas = trocas + 1
                vetor[j+1] = aux
    fim = time.time()
    cpu_usage = psutil.cpu_percent()
    memory_usage = dict(psutil.virtual_memory()._asdict())
    print('----------------------------- Bubble Sort Melhoria 1-------------------------')
    print("Quantidade de Trocas: ", trocas)
    print("Tempo de Início: ", inicio / 60 / 60 / 60 / 60)
    print("Tempo de Fim: ", fim / 60 / 60 / 60 / 60)
    print("Tempo de Execução: ", fim - inicio)
    print("CPU: ", cpu_usage)
    print("RAM: ", memory_usage, "\n")

alist = [54,26,93,17,77,31,44,55,20]
bubble_sort_1(alist)

def bubble_sort_2(vetor):
    inicio = time.time()
    trocas = 0
    mexeu = 0
    for i in range(len(vetor)):
        for j in range(i):
            if (vetor[j] > vetor[j + 1]):
                aux = vetor[j]
                vetor[j] = vetor[j + 1]
                trocas = trocas + 1
                vetor[j + 1] = aux
                mexeu = 1
        if(mexeu == 0):
            break

    fim = time.time()
    cpu_usage = psutil.cpu_percent()
    memory_usage = dict(psutil.virtual_memory()._asdict())
    print('----------------------------- Bubble Sort Melhoria 2-------------------------')
    print("Quantidade de Trocas: ", trocas)
    print("Tempo de Início: ", inicio / 60 / 60 / 60 / 60)
    print("Tempo de Fim: ", fim / 60 / 60 / 60 / 60)
    print("Tempo de Execução: ", fim - inicio)
    print("CPU: ", cpu_usage)
    print("RAM: ", memory_usage, "\n")

alist = [54,26,93,17,77,31,44,55,20]
bubble_sort_2(alist)