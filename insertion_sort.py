def insertion_sort ( list ): 
    for i in range (len(list)):
        j = i 
        while j >= 0 and list [j] < list[j-1]: 
            hand = list[j]
            list[j]= list[j-1]
            list[j-1] = hand 
            
            j = j-1 
        hand = list[j]


mylist = [23,35,2,3,4,4,5,6]
print(insertion_sort(mylist))


# geek for geek insertion sort algorithm : 
'''def insertion_sort(list):
    for i in range(1, len(list)):
        j = i -1 
        head = list [i]
        while j >= 0 and list[j]>head : 
            list[j+1] = list[j]
            j = j-1 
        list[j+1] = head '''

mylist = [23,35,2,3,4,4,5,6]
print(insertion_sort(mylist))

