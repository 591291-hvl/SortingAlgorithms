import random


#random numbers
def fillTable(n):
    table = []
    for i in range(n):
        table.append(random.randint(0,n))
    return table


def partition(table, low, high):
    pivot = table[high]
    i = low - 1
    for j in range(low, high):
        if table[j] <= pivot:
            i = i + 1
            table[i], table[j] = table[j], table[i]
    table[i + 1], table[high] = table[high], table[i + 1]
    return i + 1


def quickSort(table, low, high):
    if low < high:
        pi = partition(table, low, high)
        print(table)
        quickSort(table, low, pi - 1)
        quickSort(table, pi + 1, high)
        


N =  10

tablearray = fillTable(N)

print(tablearray)
quickSort(tablearray,0, len(tablearray)-1)
 
