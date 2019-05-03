import csv
import psutil
import time

def insertionsort(A):
    quantidadeDeTroca = 0
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while (i > -1) and key < A[i]:
            A[i+1]=A[i]
            i=i-1
            quantidadeDeTroca += 1
        A[i+1] = key
    return A, quantidadeDeTroca

def data100():
    lista = []
    inicio = time.time()
    fileName = 'DATA100.csv'    
    with open(fileName, 'rt', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';', quotechar=';')
        next(csv_reader)
        try:
            for row in csv_reader:
                lista.append(', '.join(row))
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, csv_reader.line_num, e))
    fim = time.time()
    
    listOrdenada = insertionsort(lista)
    
    cpu_usage = psutil.cpu_percent()
    memory_usage = dict(psutil.virtual_memory()._asdict())
    print('------------------------ Insertion Sort ------------------------')
    print("Quantidade de Trocas: ", listOrdenada[1])
    print("Tempo de Início: ", inicio / 60 / 60 / 60 / 60)
    print("Tempo de Fim: ", fim / 60 / 60 / 60 / 60)
    print("Tempo de Execução: ", fim - inicio)
    print("CPU: ", cpu_usage)
    print("RAM: ", memory_usage, "\n")

def data10000():
    lista = []
    inicio = time.time()
    fileName = 'DATA10000.csv'
    with open(fileName, 'rt', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';', quotechar=';')
        next(csv_reader)
        try:
            for row in csv_reader:
                lista.append(', '.join(row))
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, csv_reader.line_num, e))
    fim = time.time()

    listOrdenada = insertionsort(lista)
    cpu_usage = psutil.cpu_percent()
    memory_usage = dict(psutil.virtual_memory()._asdict())
    print('------------------------ Insertion Sort ------------------------')
    print("Quantidade de Trocas: ", listOrdenada[1])
    print("Tempo de Início: ", inicio / 60 / 60 / 60 / 60)
    print("Tempo de Fim: ", fim / 60 / 60 / 60 / 60)
    print("Tempo de Execução: ", fim - inicio)
    print("CPU: ", cpu_usage)
    print("RAM: ", memory_usage, "\n")

def data100000():
    lista = []
    inicio = time.time()
    fileName = 'DATA100000.csv'
    with open(fileName, 'rt', encoding='utf8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';', quotechar=';')
        next(csv_reader)
        try:
            for row in csv_reader:
                lista.append(', '.join(row))
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, csv_reader.line_num, e))
    fim = time.time()

    listOrdenada = insertionsort(lista)
    cpu_usage = psutil.cpu_percent()
    memory_usage = dict(psutil.virtual_memory()._asdict())
    print('------------------------ Insertion Sort ------------------------')
    print("Quantidade de Trocas: ", listOrdenada[1])
    print("Tempo de Início: ", inicio / 60 / 60 / 60 / 60)
    print("Tempo de Fim: ", fim / 60 / 60 / 60 / 60)
    print("Tempo de Execução: ", fim - inicio)
    print("CPU: ", cpu_usage)
    print("RAM: ", memory_usage, "\n")
    
if __name__=="__main__":
    data100()
    #data10000()
    #data100000()
