import random


#random numbers
def fillTable(n):
    table = []
    for i in range(n):
        table.append(random.randint(0,n))
    return table


def stalinSort(table):
    i = 0
    size = len(table)-1
    while size > i:
        if table[i] > table[i+1]:
            table.pop(i+1)
            size -= 1
        else:
            i += 1

        

        


N =  10

tablearray = fillTable(N)

print(tablearray)
stalinSort(tablearray)
print(tablearray)
 
