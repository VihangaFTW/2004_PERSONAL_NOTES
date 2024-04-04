# tute 1
# finding min in unsorted array algorithm

def find_min_val(lst: list):
    min = lst[0]
    idx = 1
    while idx < len(lst):
        if lst[idx] < min:
            min = lst[idx]
        idx += 1
    return min

# testing
arr = [-1,3,6,2,5,67]
print(find_min_val(arr))

def binary_search(lst: list, key: int):
    low,high = 0,len(lst)-1
    while low <= high:
        mid = (low+high)//2
        if lst[mid] ==  key:
            return mid
        elif lst[mid] < key:
            low = mid+1
        else:
            high = mid-1
    return -1
        

def fibonacchi(n):
    if n<=2:
        return n
    else:
        return fibonacchi(n-1) + fibonacchi(n-2)
    
def fibonacci_iterative2(n):
    if n <= 1:
        return n

    prev, current = 0, 1
    for _ in range(2, n + 1):
        prev, current = current, prev + current

    return current
    
def fibonacci_iterative(n):
    if n <= 1:
        return n

    prev, current = 0, 1
    count = 2  # Counter to keep track of the current position in the sequence

    while count <= n:
        prev, current = current, prev + current
        count += 1

    return current

def iterative_power(x,n):
    result = 1
    for _ in range(n):
        result = result * x

    return result

print(iterative_power(3,3))



if __name__ == "__main__":
    print("Hello World")