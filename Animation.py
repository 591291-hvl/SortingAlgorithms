import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
import ffmpeg



import BubbleSort
import SelectionSort
import InsertionSort
import QuickSort
import MergeSort



table = BubbleSort.fillTable2(200)

def animateBubbleSort():
    N = len(table) 
    barWidth = .5
    xloc = np.arange(N)
    fig = plt.figure()
    plt.title('BubbleSort')
    plt.xticks([])
    plt.yticks([])
    camera = Camera(fig)
    p1 = plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
    
    while not BubbleSort.checkIfSorted(table):
        BubbleSort.sortTable(table)
        plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
        camera.snap()
    animation = camera.animate(interval = 200, repeat = True, repeat_delay = 500)
 
    #Saving the animation
    plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\47472\\Downloads\\ffmpeg-2021-12-20-git-631e31773b-full_build\\ffmpeg-2021-12-20-git-631e31773b-full_build\\bin\\ffmpeg.exe'
    animation.save('BubbleSort.mp4')

def animateSelectionSort():
    N = len(table)
    barWidth = .5
    xloc = np.arange(N)
    fig = plt.figure()
    plt.title('SelectionSort')
    plt.xticks([])
    plt.yticks([])
    camera = Camera(fig)
    p1 = plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))

    for i in range(len(table)-1):
        SelectionSort.sortTable(i, table)
        plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
        camera.snap()
    animation = camera.animate(interval = 200, repeat = True, repeat_delay = 500)
 
    #Saving the animation
    plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\47472\\Downloads\\ffmpeg-2021-12-20-git-631e31773b-full_build\\ffmpeg-2021-12-20-git-631e31773b-full_build\\bin\\ffmpeg.exe'
    animation.save('SelectionSort.mp4')

def animateInsertionSort():
    N = len(table)
    barWidth = .5
    xloc = np.arange(N)
    fig = plt.figure()
    plt.title('InsertionSort')
    plt.xticks([])
    plt.yticks([])
    camera = Camera(fig)
    p1 = plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))

    for i in range(len(table)):
        InsertionSort.sortTable(i, table)
        plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
        camera.snap()
    animation = camera.animate(interval = 200, repeat = True, repeat_delay = 500)
 
    #Saving the animation
    plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\47472\\Downloads\\ffmpeg-2021-12-20-git-631e31773b-full_build\\ffmpeg-2021-12-20-git-631e31773b-full_build\\bin\\ffmpeg.exe'
    animation.save('InsertionSort.mp4')

def quickSort(table, low, high, xloc, barWidth, camera):
    if low < high:
        
        pi = QuickSort.partition(table, low, high)
        plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
        camera.snap()
        
        quickSort(table,low, pi-1, xloc, barWidth, camera)
        quickSort(table, pi +1, high, xloc, barWidth, camera)

def animateQuickSort():
    N = len(table)
    barWidth = .5
    xloc = np.arange(N)
    fig = plt.figure()
    plt.title('QuickSort')
    camera = Camera(fig)
    plt.xticks([])
    plt.yticks([])

    quickSort(table, 0 , len(table)-1, xloc, barWidth, camera)

    animation = camera.animate(interval = 200, repeat = True, repeat_delay = 500)
 
    #Saving the animation
    plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\47472\\Downloads\\ffmpeg-2021-12-20-git-631e31773b-full_build\\ffmpeg-2021-12-20-git-631e31773b-full_build\\bin\\ffmpeg.exe'
    animation.save('QuickSort.mp4')

def mergeSort(table, low, high, xloc, barWidth, camera):
    if low < high:
        mid = (low + high-1)//2
        mergeSort(table, low, mid, xloc, barWidth, camera)
        mergeSort(table, mid +1, high, xloc, barWidth, camera)
       
        MergeSort.merge(table,low,mid,high)
        #print
        plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
        camera.snap()

def animateMergeSort():
    N = len(table)
    barWidth = .5
    xloc = np.arange(N)
    fig = plt.figure()
    plt.title('MergeSort')
    camera = Camera(fig)
    plt.xticks([])
    plt.yticks([])

    mergeSort(table, 0 , len(table)-1, xloc, barWidth, camera)

    animation = camera.animate(interval = 200, repeat = True, repeat_delay = 500)
 
    #Saving the animation
    plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\47472\\Downloads\\ffmpeg-2021-12-20-git-631e31773b-full_build\\ffmpeg-2021-12-20-git-631e31773b-full_build\\bin\\ffmpeg.exe'
    animation.save('MergeSort.mp4')

def stalinSort(table, xloc, barWidth, camera):
    i = 0
    size = len(table)-1
    while size > i:
        if table[i] > table[i+1]:
            table.pop(i+1)
            size -= 1
        else:
            i += 1
        xloc = np.arange(len(table))
        plt.bar(xloc, table, width=barWidth, color=(0.2, 0.4, 0.6, 0.6))
        camera.snap()

def animateStalinSort():
    N = len(table)
    barWidth = .5
    xloc = np.arange(N)
    fig = plt.figure()
    plt.title('StalinSort')
    camera = Camera(fig)
    plt.xticks([])
    plt.yticks([])

    stalinSort(table, xloc, barWidth, camera)

    animation = camera.animate(interval = 200, repeat = True, repeat_delay = 500)
 
    #Saving the animation
    plt.rcParams['animation.ffmpeg_path'] ='C:\\Users\\47472\\Downloads\\ffmpeg-2021-12-20-git-631e31773b-full_build\\ffmpeg-2021-12-20-git-631e31773b-full_build\\bin\\ffmpeg.exe'
    animation.save('StalinSort.mp4')



#animateBubbleSort()
#animateSelectionSort()
#animateInsertionSort()
#animateQuickSort()
#animateMergeSort()
animateStalinSort()