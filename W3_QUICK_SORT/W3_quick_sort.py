# Out of place quick sort implementation. Higher space compelxity.
def basic_quick_sort(lst:list):
    '''
    :complexity: 
    time:- best O(N log N) where N is length of input list. (if the pivot chosen splits the list evenly)
        :- worst O(N^2) when  the chosen pivot is the smallest or largest element  in each recursive call
    space:- total O(N + log N) = O(N)
        :-aux O(log N) due to recursive stack
    '''
    #  <= to handle empty list as input.
    if len(lst) <= 1:
        return lst
    pivot = lst.pop()
    lower_items = []
    higher_items = []
    for item in lst:
        if item > pivot:
            higher_items.append(item)
        else:
            lower_items.append(item)
    return basic_quick_sort(lower_items) + [pivot] + basic_quick_sort(higher_items)


''' Python implementation of QuickSort using Hoare's  
partition scheme. '''
  
''' This function takes first element as pivot, and places 
      all the elements smaller than the pivot on the left side 
      and all the elements greater than the pivot on 
      the right side. It returns the index of the last element 
      on the smaller side '''
  
  
def hoares_partition(arr, low, high): 
  
    pivot = arr[low] 
    i = low - 1
    j = high + 1
  
    while True: 
  
        # Find leftmost element greater than 
        # or equal to pivot 
        i += 1
        while arr[i] < pivot: 
            i += 1
  
        # Find rightmost element smaller than 
        # or equal to pivot 
        j -= 1
        while arr[j] > pivot: 
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
  
  
def hoares_quickSort(arr, low, high): 
    ''' pi is partitioning index, arr[p] is now  
    at right place '''
    if (low < high): 
  
        pi = hoares_partition(arr, low, high) 
  
        # Separately sort elements before 
        # partition and after partition 
        hoares_quickSort(arr, low, pi) 
        hoares_quickSort(arr, pi + 1, high)             
    
    return arr

# * 3-way partitioning algorithm: useful for duplicate items

def dutch_flag_partition(arr, low, high, pivot):
    '''
    Useful when there are many identical elements or has a skewed distribution around the pivot, 
    this technique can significantly reduce the number of recursive calls and comparisons,  
    '''

    smaller = low  # Index for elements smaller than the pivot
    pointer = low    # Index for elements equal to the pivot
    larger = high  # Index for elements greater than the pivot
    
    while pointer <= larger:
        if arr[pointer] < pivot:
            arr[smaller], arr[pointer] = arr[pointer], arr[smaller]
            smaller += 1
            pointer += 1
        elif arr[pointer] == pivot:
            pointer += 1
        else:  # arr[equal] > pivot
            arr[pointer], arr[larger] = arr[larger], arr[pointer]
            #* we dont increment pointer as we dont know whether the new element 
            #* in pointer place after swap is smaller/equals/greater than pivot
            larger -= 1
    
    return smaller, larger  # Return indices for elements smaller and larger than the pivot

def dutch_quicksort(arr, low, high):
    if low < high:
        pivot = arr[low + (high - low) // 2]  # Choosing pivot as middle element
        smaller, larger = dutch_flag_partition(arr, low, high, pivot)
        
        # Recursively sort elements smaller and larger than the pivot
        dutch_quicksort(arr, low, smaller - 1)
        dutch_quicksort(arr, larger + 1, high)

    

    return arr

def vingu_dutch_partition(arr, low, high, pivot):
    smaller = low
    pointer = low
    bigger = high

    while pointer <= bigger:
        if arr[pointer] < pivot:
            arr[smaller], arr[pointer] = arr[pointer], arr[smaller]
            smaller += 1
            pointer += 1
        elif arr[pointer] == pivot:
            pointer += 1
        else:
            arr[bigger], arr[pointer] = arr[pointer], arr[bigger]
            bigger -= 1
    return smaller, bigger

def vingu_dutch_quicksort(arr,low,high):

    # * When low becomes equal to high, it means there's only one element in the partition, 
    # * indicating that the partition doesn't need further partitioning.
    if low <high:
        pivot = arr[low + (high-low)//2]
        smaller, bigger = vingu_dutch_partition(arr,low,high,pivot)
        vingu_dutch_quicksort(arr,low,smaller-1)
        vingu_dutch_quicksort(arr,bigger+1,high)
    return arr


def vingu_hoares_partition(arr,low,high):
    pivot = arr[low]
    #* i is initiliazed to low-1 so that the first element is not skipped
    i = low-1
    #* j is initiliazed to high+1 so that the last element is not skipped
    j = high+1

    while True:
        i +=1
        while arr[i] < pivot:
            i+=1
        j -= 1
        while arr[j]>pivot:
            j-=1
        if i >=j:
            return j
        arr[i],arr[j] = arr[j], arr[i]

def vingu_hoares_quicksort(arr,low,high):
    if low< high:
        partition_index = vingu_hoares_partition(arr,low,high)
        vingu_hoares_quicksort(arr,low,partition_index)
        vingu_hoares_quicksort(arr,partition_index+1,high)
    return arr

def naive_quick_select(arr,low,high,pivot):
    smaller = low
    pointer = low
    bigger = high

    while pointer <= bigger:
        if arr[pointer] < pivot:
            arr[smaller],



if __name__ == "__main__":
    arr = [2,6,2,4,10,8,4,6]
    arr2 = []
    print(vingu_hoares_quicksort(arr,len(arr)-1, 0))
    