def radix_sort_suffixes(suffix_lst):
    '''
    This function sorts the suffixes in a given list of tuples (suffix, index) in alphabetical order using a non-comparison based algorithm called radix sort, 
    which utilizes counting sort.
    :param word_lst: a list of tuples of the form (suffix, index)
    :return: the given list with the suffixes sorted in alphabetical order
    #* time complexity: O(N*D)
    #* space complexity: Total: O(N+N) =O(N) Aux: O(N) as an index in the count array contains a list of all the suffixes of the word.
    In the worst case, if all words have the same character at the current position being considered, all words would go into the same bucket.                  
     -N is the length of the word_list
     -D is the number of characters in the largest word in the list
    '''
    max_chars = max(len(suffix) for suffix, _ in suffix_lst) #? O(N)
    
    for char in range(max_chars-1, -1, -1):
        temp_count_array: list = [[] for _ in range(27)]
        
        for suffix, index in suffix_lst:
            if char < len(suffix):
                idx = 0 if suffix[char] == '$' else ord(suffix[char]) - ord('a') + 1
            else:
                idx = 0
            temp_count_array[idx].append((suffix, index))
        
        suffix_lst = [item for sublist in temp_count_array for item in sublist]
    
    return suffix_lst

def generate_suffixes(word: str) -> list[str]:
    '''
    This function generates a list of all the suffixes of the given word, including the empty string.
    :param word: word to generate the suffixes from 
    :returns a list of tuples (suffix, starting index) generated from the given word, including empty string. 
    Each item in the list is a tuple consisting of the suffix and starting index of the suffix in the word.
    #! we store the suffixes as a tuple (suffix, index) to handle words with repeated characters like "aaaaa".
    #! This used in generating the suffix array for words with repeated characters in the function below.
    :time complexity: worst case is O(N^2) where N is the length of the word.
    :space complexity:- 
    total:- O(N+N) =  O(N)
    aux  :- O(N) for suffix list. Max size of this list is the N+1 so (N)
    '''
    
    suffixes_lst = []
    
    for i in range(len(word)):  #? O(N) but overall O(N^2) 
        suffix = word[i:]  #? O(N)
        # store both the suffix and its starting index in the original word
        suffixes_lst.append((suffix,i))
    # $ represents the empty string which is a suffix of every word
    suffixes_lst.append(("$",len(word)))
    return suffixes_lst

def generate_suffix_array(word:str) -> list[int]:
    '''
    This function generates a suffix array for the given word. The array consists of all the suffixes of the word (including the $ for empty string)
    sorted in alphabetical order. Each index corresponds to an integer representing the starting index of the suffix in the given word.
    :returns a suffix array consisting of suffix ids as elements for the given word.
    :time complexity:- O(N^2 + N^2+ N^2) = O(N^2) where N is the length of the given word.
    :space complexity:-
    total:- O(N+N+N+N) = O(N)
    aux:- O(3N) = O(N)
    '''
    suffixes: list[str] = generate_suffixes(word) #? O(N^2)
    sorted_suffix_lst = radix_sort_suffixes(suffixes) #? O(N*D) = O(N^2) as max size of D is N (the longestg suffix is the word itself)
    suffix_array = [] # O(N) space in worst case 
    for _,index in sorted_suffix_lst: #? O(N); total comp = O(N^2)
        suffix_array.append(index)
    
    return suffix_array


def find_longest_substring(word: str) -> str:
    suffix_arr = generate_suffix_array(word)
    suffix_index = 0
    longest_substring_length = 0

    for i in range(len(suffix_arr)-1):
        current_suffix = word[suffix_arr[i]:]
        next_suffix = word[suffix_arr[i+1]:]
        char_matches = 0
        for j in range(min(len(current_suffix), len(next_suffix))):  # use a different variable for this loop
            if current_suffix[j] == next_suffix[j]:
                char_matches += 1
            else:
                break
        if char_matches > longest_substring_length:
            longest_substring_length = char_matches
            suffix_index = suffix_arr[i]  # store the starting index of the suffix, not the loop variable

    longest_substring = word[suffix_index:suffix_index+longest_substring_length]
    return f'The longest common substring is "{longest_substring}" with length {longest_substring_length}.'


def binary_search(sequence: list, element) -> int:
    '''
    This function returns the index of the sequence where the element is stored if it exists.
    Otherwise, a ValueError Exception is raised.
    :prerequisite: the given sequence must be sorted in ascending order.
    :time complexity:- 
    worst case is O(k*log N) where k is the comparsion cost for elements and N is the length of sequence. 
    Best case is O(k) when the element to be found is in the middle of the sequence.
    :space complexity:-
    total:- O(N)
    aux:- O(1) 
    '''
    n = len(sequence)
    low,high = 0,n-1
    while low <= high:
        middle = (low+high)//2
        if sequence[middle] == element:
            return middle
        elif sequence[middle] > element:
            high = middle-1
        else:
            low = middle+1
    raise ValueError(f'{element} does not exist!')





if __name__ == "__main__":
    print(find_longest_substring("baaab"))
    
    