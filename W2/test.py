
def binary_search(lst, key):
    low = 0
    high = len(lst)
    while low < high:
        mid = (low+high)//2
        if key >= lst[mid]:
            low = mid
        else:
            high = mid
    if len(lst) > 0 and lst[low] == key:
        print("key found at index" + str(low))
    else:
        print("key not found")


if __name__  == "__main__":
    binary_search([1,2,3,4], 2)
    print("cat")
