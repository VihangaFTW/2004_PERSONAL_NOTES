import math

# * CODE TAKEN FROM GITHUB REPO
def num_rad_sort(nums, b):
    """
    num_rad_sort takes in an unsorted NON-EMPTY list of numbers
    and will sort them according to the base which should be >= 2
    :param nums: the list of elements to be sorted
    :param b: the base of the numbers
    :return: a sorted list
    :complexity:    #* time -  O((n+b)*logbM
                    #* space - O(n+b) (Total space)
                    #* O(b) (aux space)
    Credit to Week 02 lecture video for the idea on how to make counting sort stable
    """
    if b < 2:
        print("Base needs to be higher")
        return
    if len(nums) < 2:
        return nums
    m = max(nums)
    k = math.ceil(math.log(m, b))
    
    #* ==== change made by me ====
    if b**k == m:
        k += 1
    #*============================

    for col in range(k):  # ? O(D)
        # Creating an empty count array
        count_array = [None] * b
        # Making sure that each element is a new list in the count array
        for i in range(len(count_array)):  # ? O(b)
            count_array[i] = []
        # Looping through nums to get the count
        for element in nums:  # ? O(n)
            item = (element // b ** col) % b
            count_array[item].append(element)
        index = 0
        # looping through the count array to get the order of nums
        for i in range(len(count_array)):  # ? O(b)
            frequency = len(count_array[i])
            for j in range(frequency):
                nums[index] = count_array[i][j]
                index += 1
    return nums


# *MY VERSION

def my_radix_sort(num_lst: list[int], base: int) -> list[int]:
    '''
    This function sorts a given list of positive numbers in ascending order using a non-comparison based algorithm called radix sort, 
    which utilizes counting sort as a subroutine.
    :param num_lst: a list of positive numbers
    :param base: base used for sorting the numbers.
    :return: the given list sorted in ascending order
    #* time complexity: O(N*D)
    #* space complexity: Total: O(N+B) Aux: O(B) as size of count array depends on base.
    #* NOTE FOR AUX SPACE: The temp_count_array is created anew for each digit, but it's also discarded after each digit. 
    #* This means that at any given time, there's only one temp_count_array in memory. So O(B)
    #! In terms of space complexity, we're interested in the total amount of space used at any point in time (peak memory usage), 
    #! not the cumulative total space used over time.                    
     -N is the length of the num_list
     -D is the number of digits of the largest number in the list
    '''
    if base < 2 :
        raise ValueError("Base must be 2 or greater!")
    
    if len(num_lst) < 2:
        return num_lst
    
    # find max num in list
    max_num = num_lst[0]
    for num in num_lst:  #? O(N)
        if num > max_num:
            max_num = num
    
    # find the number of digits in this number
    max_digits = math.ceil(math.log(max_num,base))  #?  O(1)

    # if the max number is an exact power of the base, we need to add 1 as logarithms are counted from 0
    #! REFER TO [logarithms and exact power of bases.md]
    if max_num == base**max_digits:
        max_digits += 1

    #print(f'max digits: {max_digits}')
    
    # loop thru each col of the numbers
    for col in range(max_digits):  #? O(D) but final is O(N*D)
        temp_count_array: list = [None] * base   # for base 10 this is [0...9]

        # populate each index with a list to preserve stability of numbers with equal digit values
        for i in range(len(temp_count_array)):  #? O(B) but does not scale with input list so this is dominated by O(N) below
            temp_count_array[i] = []  # each index contains a unique list

        # loop thru each number in list and add to the count array according to the number
        for num in num_lst:  #? O(N)
            #*  num//base**col =“shifting” the digits of num to the right by col positions.
            #* % base gives the rightmost digit
            #* 0 is returned if the column does not contain a digit; 23 col 2 would return 0
            digit = (num//base**col)%base
            temp_count_array[digit].append(num)

        # sort the given list according to frequency of each digit
        index = 0
        #* B doesn’t change with the size of the input, it’s not the dominant factor in the time complexity.
        for i in range(len(temp_count_array)):  #? O(B) but final is O(N)
            frequency = len(temp_count_array[i])
            #* the inner loop iterates once for each number in num_lst. 
            #* So, if num_lst contains n numbers, the inner loop will run n times in total (across all iterations of the outer loop).
            for j in range(frequency):  #? O(N)
                num_lst[index] = temp_count_array[i][j]
                index += 1

    return num_lst

def radix_sort_words_by_size(word_lst):
    '''
    This function sorts a given list of lowercase words in ascending order using a non-comparison based algorithm called radix sort, 
    which utilizes counting  as a subroutine.
    :param word_lst: a list of lowercase words
    :return: the given list sorted in ascending order where shorter words come before longer words
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
    for char in range(max_chars):  # O(D) but final is O(N*D)
        temp_count_array: list = [[] for _ in range(27)]   # index 0 is for the empty string and indices [1..26] for lowercase letters

        # loop thru each char in list and add to the count array according to the word
        for word in word_lst:  # O(N)
            if char < len(word):
                current_char = word[-(char+1)]
                index = ord(current_char) - ord('a') + 1
            # length of current word is smaller than current char column
            else:
                # we store this word in index 0
                index = 0
            temp_count_array[index].append(word)

        # sort the given list according to frequency of each character
        word_lst = [word for sublist in temp_count_array for word in sublist]
    
    return word_lst

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


if __name__ == "__main__":
    arr = [234,254,2334,6,4,23,345345]
    arr2 = [16,7,4,1,12]
    #print(my_radix_sort(arr2,2))
    arr3 = ["apple", "pple", "ple", "le", "e"]
    print(radix_sort_words_by_letter(arr3))
    
    

