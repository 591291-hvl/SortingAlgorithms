import random


#random numbers
def fillTable(n):
    table = []
    for i in range(n):
        table.append(random.randint(0,n))
    return table


def mergeSort(table, low, high):
    if low < high:
        mid = (low + high-1)//2
        mergeSort(table, low, mid)
        mergeSort(table, mid+1, high)
        print(table)
        merge(table, low, mid, high)


def merge(table, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid 

    left = []
    right = []
    for i in range(n1):
        left.append(table[i+low])
    for j in range(n2):
        right.append(table[j + mid + 1])
    
    i,j = 0,0
    for k in range(low, high+1):
        if j >= n2 or i < n1 and left[i] <= right[j]:
            table[k] = left[i]
            i += 1
        else:
            table[k] = right[j]
            j += 1
        
        


N =  10

tablearray = fillTable(N)

print(tablearray)
mergeSort(tablearray, 0, len(tablearray)-1)
print(tablearray)