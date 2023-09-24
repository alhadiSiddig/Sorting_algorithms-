def findsmallest(arr): 
    smallest = arr[0]
    smallest_index =  0 
    for i in range(len(arr)):
        if arr[i] < smallest : 
            smallest = arr[i] 
            smallest_index = i 

    return smallest_index 


def selection_sort(arr):
    newArr= [] 
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newArr.append(arr.pop(smallest_index))
    return newArr



