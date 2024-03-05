def counting_sort(new_lst):

    # find max elem
    max_elem = new_lst[0]
    for item in new_lst:
        if item > max_elem:
            max_elem = item

    # create count array based on max range
    count_array = [0] * (max_elem+1)
    
    # populate count array with frequency
    for item in new_lst:
        count_array[item] = count_array[item] + 1

    # output sorted list
    index = 0
    for i in range(len(count_array)):
        frequency = count_array[i]
        for j in range(frequency):
            new_lst[index] = i
            index += 1
    
    return new_lst

# handles lowercase english letters from a-z
def counting_sort_alpha(new_lst):
    
    # subtracting 97 from the ASCII value of each lowercase character, 
    # you're effectively mapping 'a' to 0, 'b' to 1, 'c' to 2, 
    # and so forth up to 'z' being mapped to 25. 
    
    max_elem = ord(new_lst[0])-97

    for item in new_lst:
        item = ord(item) -97
        if item > max_elem:
            max_elem = item

    # create count array based on max range
    count_array = [0] * (max_elem+1)
    
    # populate count array with frequency
    for item in new_lst:
        item = ord(item)-97
        count_array[item] = count_array[item] + 1

    # output sorted list
    index = 0
    for i in range(len(count_array)):
        frequency = count_array[i]
        for j in range(frequency):
            # reversing the transformation done during sorting, 
            # mapping back from the range 0 to 25 to the ASCII values of 'a' to 'z' (97 to 122).
            new_lst[index] = chr(i+97)
            index += 1
    
    return new_lst


def counting_sort_stable(new_lst):

    # find max elem
    max_elem = new_lst[0]
    for item in new_lst:
        if item > max_elem:
            max_elem = item

    # create count array based on max range
    
    # initialize each slot to None so that we can create separate array slots
    count_array = [None] * (max_elem+1)
    # populate each slot in count array with a unique list
    for i in range(len(count_array)):
        count_array[i] = []

    # populate count array with frequency
    for item in new_lst:
        count_array[item].append(item)

    # output sorted list
    # keep track of index to increment after iteration
    index = 0
    for i in range(len(count_array)):
        inner_lst = count_array[i]
        for j in range(len(inner_lst)):
            new_lst[index] = inner_lst[j]
            index += 1
    
    return new_lst


arr = [2,3,6,4,5,6,2,3,5,12]
out = counting_sort(arr)

# testing
arr2 = ['z','x','y', 'd', 'a', 'b' ]
print(counting_sort_stable(arr))


def test_sort(array:list):
    for i in range(len(out)-1):
        if out[i] <= out[i+1]:
            continue
        else:
            print("FAIL")
            break

if __name__ == "__main__":
    print("meow")