def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merge

#!=================================== Practice ============================================

def my_merge_sort(arr):
    '''
    This function sorts a given array of numbers in ascending order by recursively
    dividing the sample space into two sub arrays (by halving) until there is only one element in each array (which is sorted).
    It then travels up the recursive stack while combining the two arrays into one sorted array per level, leading to a fully sorted array.
    : param arr: a list of numbers preferrably unsorted.
    : return: a sorted list of the numbers in ascending order
    : time complexity:-
        worst case: O(N log N)
    '''
    if len(arr) <= 1:
        return arr
    
    middle = len(arr)//2
    left_arr = arr[:middle]  #? O(N)
    right_arr = arr[middle:] #? O(N)

    return my_merge(my_merge_sort(left_arr), my_merge_sort(right_arr))  #? O(N * log N)


def my_merge(left_arr, right_arr):
    '''
    This helper function for merge sort combines two sorted arrays into one sorted array.
    #* As long as the merge function moves equal “left” elements before “right” elements, it will be stable.
    : prereq: both the input arrays must be sorted
    : param right_arr: the right section of the arrays to be combined
    : param left_arr: the left section of the arrays to be combined
    : return: a single sorted array consisting of elements from both input arrays
    : time complexity:-  L and R are sizes of the left and right arrays respectively.
    best case: O(1) when the input is a list containing one element
        worst case: O(max(L,R))
    : space complexity:-
        aux space: O(L+R) as merged will contain all elements from left and right array.
    '''
    left_index = 0
    right_index = 0

    merged = []

    while left_index < len(left_arr) and right_index < len(right_arr):  #? O(max(L,R))
        if left_arr[left_index] <= right_arr[right_index]:
            merged.append(left_arr[left_index])
            left_index += 1
        else:
            merged.append(right_arr[right_index])
            right_index += 1

    merged.extend(left_arr[left_index:])  #? O(L)
    merged.extend(right_arr[right_index:]) #? O(R)


    return merged
#!============================================================================================

if __name__ == "__main__":
    arr = [3,1,5,2,8,323,765,214,454]
    print(my_merge_sort(arr))
