import csv
import time

lista = open('DATA100.csv', 'r')

lido = csv.reader(lista)

lista2 = []

for linha in lido:
    lista2.append(linha)

inicio = time.time()
def selectionSort(lista):
    qtComparacoes = 0
    qtTrocas = 0
    
    for i in range(len(lista)):
        minPosition = i
        for j in range(i+1, len(lista)):
            qtComparacoes = qtComparacoes + 1
            if lista[minPosition] > lista[j]:
                minPosition = j
                qtTrocas += 1
            qtComparacoes += 1
            
        temp = lista[i]
        lista[i] = lista[minPosition]
        lista[minPosition] = temp

    print("Teve ", qtComparacoes, " comparações.")
    print("Teve ", qtTrocas, " trocas.")
    return lista

selectionSort(lista2)
fim = time.time()

print("Demorou ", fim - inicio, " segundos")
