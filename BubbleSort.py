import random

#N = 10

#random numbers
def fillTable(n):
    table = []
    for i in range(n):
        table.append(random.randint(1,n))
    return table

def fillTable2(n):
    table = []
    for i in range(n):
        table.append(i)
    table = random.shuffle(table)
    return table


def sortTable(table):
    for i in range(len(table)-1):
        if(table[i] > table[i+1]):
            table[i], table[i+1] = table[i+1], table[i]
    return table

def checkIfSorted(table):
    for i in range(len(table)-1):
        if(table[i] > table[i+1]):
            return False
    return True


def bubbleSort(table):
    while not checkIfSorted(table):
        print(table)
        sortTable(table)

#tableArray = fillTable(N)

#bubbleSort(tableArray)
#print(tableArray)