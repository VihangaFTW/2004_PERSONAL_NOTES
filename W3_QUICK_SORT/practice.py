def outplace_quick_sort(arr: list[int])-> list[int]:

    if len(arr) <= 1:
        return arr
    
    smaller_or_eq_arr = []
    bigger_arr = []

    pivot = arr.pop()

    for elem in arr:
        if elem > pivot:
            bigger_arr.append(elem)
        else:
            smaller_or_eq_arr.append(elem)

    return outplace_quick_sort(smaller_or_eq_arr) + [pivot] + outplace_quick_sort(bigger_arr)


def hoares_partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[low]
    smaller = low-1
    bigger = high+1

    while True:
        smaller += 1
        while  arr[smaller] < pivot:
            smaller += 1
        bigger -= 1
        while arr[bigger] > pivot:
            bigger -= 1
        if smaller >= bigger:
            return bigger
        arr[smaller], arr[bigger] = arr[bigger], arr[smaller]



def hoares_quick_sort(arr:list[int], low: int, high: int) -> list[int]:
    '''
    :time complexity: 
    
    '''
    if low < high:
        partition_index = hoares_partition(arr, low, high)
        hoares_quick_sort(arr, low, partition_index)
        hoares_quick_sort(arr, partition_index+1, high)
    return arr
    


if __name__ ==  "__main__":
    arr = [61,2,3,4,5,6,7]
    print(hoares_quick_sort(arr,0,len(arr)-1))