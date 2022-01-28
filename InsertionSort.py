import random


#random numbers
def fillTable(n):
    table = []
    for i in range(n):
        table.append(random.randint(1,n))
    return table

def sortTable(i, table):
    for j in range(i, 0, -1):
        if table[j-1] > table[j]:
            table[j-1], table[j] = table[j], table[j-1]

def checkIfSorted(table):
    for i in range(len(table)-1):
        if(table[i] > table[i+1]):
            return False
    return True

def insertionSort(table):
    for i in range(len(table)):
        print(table)
        sortTable(i, table)

N =  10

tableArray = fillTable(N)

insertionSort(tableArray)
print(tableArray)