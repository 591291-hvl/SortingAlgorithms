import numpy as np
import matplotlib.pyplot as plt

import BubbleSort
import SelectionSort
import InsertionSort
import QuickSort
import MergeSort



table = BubbleSort.fillTable2(200)

def showBubbleSort():
    N = len(table) 
    barWidth = .5
    xloc = np.arange(N)
    p1 = plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))

    while not BubbleSort.checkIfSorted(table):
        BubbleSort.sortTable(table)
        plt.cla()
        plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
        plt.pause(0.05)
    plt.show()


def showSelectionSort():
    N = len(table)
    barWidth = .5
    xloc = np.arange(N)
    p1 = plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))

    for i in range(len(table)-1):
        SelectionSort.sortTable(i, table)
        plt.cla()
        plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
        plt.pause(0.05)
    plt.show()


def showInsertionSort():
    N = len(table)
    barWidth = .5
    xloc = np.arange(N)
    p1 = plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))

    for i in range(len(table)):
        InsertionSort.sortTable(i, table)
        plt.cla()
        plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
        plt.pause(0.05)
    plt.show()


def quickSort(table, low, high, xloc, barWidth):
    if low < high:
        pi = QuickSort.partition(table, low, high)
        #print
        plt.cla()
        plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
        plt.pause(0.01)

        quickSort(table,low, pi-1, xloc, barWidth)
        quickSort(table, pi +1, high, xloc, barWidth)

def showQuickSort():
    N = len(table)
    barWidth = .5
    xloc = np.arange(N)
    p1 = plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))

    quickSort(table, 0 , len(table)-1, xloc, barWidth)

    plt.show()

def mergeSort(table, low, high, xloc, barWidth):
    if low < high:
        mid = (low + high-1)//2
        mergeSort(table, low, mid, xloc, barWidth)
        mergeSort(table, mid +1, high, xloc, barWidth)
       
        MergeSort.merge(table,low,mid,high)
        #print
        plt.cla()
        plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
        plt.pause(0.01)

def showMergeSort():
    N = len(table)
    barWidth = .5
    xloc = np.arange(N)
    p1 = plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))

    mergeSort(table, 0 , len(table)-1, xloc, barWidth)

    plt.show()

#showBubbleSort()
#showSelectionSort()
#showInsertionSort()
#showQuickSort()
showMergeSort()