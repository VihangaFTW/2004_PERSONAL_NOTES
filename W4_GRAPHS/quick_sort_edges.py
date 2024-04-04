def hoares_partition(arr, low, high): 
  
    pivot = arr[low].w 
    i = low - 1
    j = high + 1
  
    while True: 
  
        # Find leftmost element greater than 
        # or equal to pivot 
        i += 1
        while arr[i].w < pivot: 
            i += 1
  
        # Find rightmost element smaller than 
        # or equal to pivot 
        j -= 1
        while arr[j].w > pivot: 
            j -= 1
  
        # If two pointers met. 
        if i >= j: 
            return j 
  
        arr[i], arr[j] = arr[j], arr[i] 
  
  
''' The main function that implements QuickSort  
arr --> Array to be sorted,  
low --> Starting index,  
high --> Ending index 
'''
  
  
def quick_sort_edges(arr, low, high): 
    ''' pi is partitioning index, arr[p] is now  
    at right place '''
    if (low < high): 
  
        pi = hoares_partition(arr, low, high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quick_sort_edges(arr, low, pi) 
        quick_sort_edges(arr, pi + 1, high)             
    
    return arr