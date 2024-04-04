def radix_sort_words_by_letter(word_lst):
    '''
    This function sorts a given list of lowercase words in alphabetical order using a non-comparison based algorithm called radix sort, 
    which utilizes counting sort.
    :param word_lst: a list of lowercase words
    :return: the given list sorted in alphabetical order where shorter words come before longer words
    #* time complexity: O(N*D)
    #* space complexity: Total: O(N+B) Aux: O(B) as size of count array depends on base.                   
     -N is the length of the word_list
     -D is the number of characters in the largest word in the list
    '''
    
    if len(word_lst) < 2:
        return word_lst
    
    # find longest word in list
    max_word = max(word_lst, key=len)
    
    # find the number of characters in this word
    max_chars = len(max_word)

    # loop thru each char of the words
    for char in range(max_chars-1, -1, -1):  # O(D) but final is O(N*D)
        temp_count_array: list = [[] for _ in range(27)]   # index 0 is for the empty string and indices [1..26] for lowercase letters

        # loop thru each char in list and add to the count array according to the word
        for word in word_lst:  # O(N)
            if char < len(word):
                index = ord(word[char]) - ord('a') + 1
            else:
                # we store this word in index 0
                index = 0
            temp_count_array[index].append(word)

        # sort the given list according to frequency of each character
        word_lst = [word for sublist in temp_count_array for word in sublist]
    
    return word_lst


def hoares_partition_for_strings_by_length(arr, low, high): 
  
    pivot = len(arr[low]) 
    i = low - 1
    j = high + 1
  
    while True: 
  
        # Find leftmost element greater than 
        # or equal to pivot 
        i += 1
        while len(arr[i]) < pivot: 
            i += 1
  
        # Find rightmost element smaller than 
        # or equal to pivot 
        j -= 1
        while len(arr[j]) > pivot: 
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
  
  
def hoares_quickSort_for_strings_by_length(arr, low, high): 
    ''' pi is partitioning index, arr[p] is now  
    at right place '''
    if (low < high): 
  
        pi = hoares_partition_for_strings_by_length(arr, low, high) 
  
        # Separately sort elements before 
        # partition and after partition 
        hoares_quickSort_for_strings_by_length(arr, low, pi) 
        hoares_quickSort_for_strings_by_length(arr, pi + 1, high)
    return arr
    



if __name__ ==  "__main__":
    arr = ["abd", "c", "abc", "aac", "bc","bac"]
    print(hoares_quickSort_for_strings_by_length(arr,0,len(arr)-1))