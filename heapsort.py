
#i index of the element in list ,

def max_heapify(list, i):

    # N is number of elements in list 
    # parent and childern computaion function : 
    l = LEFT[i] 
    r = right[i]

    if l <= heap_size(list)and list[l]> list[i] : 
        largest = l 
    else : largest = i 

    if r <= heap_size(list) and list[r]> list[i]:
        largest = l 
    else : 
        largest = r 

    if largest != i : 
        list[i] , list[largest] = list[largest] , list[i]
        max_heapify(list , largest)    


def parent(list :list , i:int ): 
    i = i//2
    return list[i]    

def LEFT (list, i ): 
     return list[i*2]

     
def RIHGT (list, i ):
    return list[(i*2)+1]

if __name__ == '__main__':
    mylist = [i for i in range(10)]
    parent_ = parent(mylist , 6 ) 
    print('this should be 3' , parent_ )
    print('thsi sould be 13 :' ,  RIHGT(mylist, 6))
    print('this should be 12 :' , LEFT(mylist, 6))