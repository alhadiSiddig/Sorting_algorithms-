def mergeSort(arr):
    if len(arr) > 1 : 
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0 
        while i < len(L) and j < len(R ) : 
            if L[i] <= R [j] : 
                arr[k] = L[i]
                i+= 1 
            else : 
                arr[k] = R[j]
                j+=1 
            k+=1 
        while i < len(L):
            arr[k] = L[i]
            i+=1 
            k+=1 
        while j< len(R): 
            arr[k] = R[j]
            j+=1 
            k+=1 
        


    
if __name__ == '__main__' :

    mylist =  [ 23,5,36,21,55,34] 
    print(' my list before mergeSort:' , mylist )
    mergeSort(mylist) 
    print(' mylist after mergeSort :' , mylist)
    
# in running has occured typeError problem , the return value of MergeSort hasn't been specified so the \
#  returned value was None when we used len(mergeSort) call ,then raised the error 

