from multiprocessing.spawn import _main


def insertion_sort(list):
    for i in range(len(list)):
        hand = list[i]

        j = i -1 
        while j >= 2 and list[j] > hand : 
            list[j+1] = list[j] 
            j = j-1 
        list[j] = hand 

mylist =  [23,34,35,6,45,7,567]



