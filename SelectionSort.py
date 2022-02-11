import random

#N = 10

#random numbers
def fillTable(n):
    table = []
    for i in range(n):
        table.append(random.randint(1,n))
    return table


def sortTable(i,table):
    smallest = len(table)-1
    for j in range(i, len(table)-1):
        if table[smallest] > table[j]:
            smallest = j
    table[smallest], table[i] = table[i], table[smallest]

def checkIfSorted(table):
    for i in range(len(table)-1):
        if(table[i] > table[i+1]):
            return False
    return True

def selectionSort(table):
    for i in range(len(table)-1):
        print(table)
        sortTable(i,table)

N =  10

tableArray = fillTable(N)

selectionSort(tableArray)
print(tableArray)