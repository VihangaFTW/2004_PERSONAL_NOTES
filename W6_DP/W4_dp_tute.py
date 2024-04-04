# Tutorial 5
#? Problem 2
def calculate_salesman_profit(houses:list[int]) -> str:
    '''
    :param houses: a list of houses with their respective profits
    :return: maximum profit possible along with the houses to visit for this profit as a string.
    :time complexity: best/worst O(N) where N is the size of "houses" list
    :space complexity: auxillary complexity :- O(N+N+N/2) = O(N)
                       total complexity :- O(N+3N) = O(N)
    '''
    #! SEE [W4\PROB2_TABLE.png]

    memo = [0] * (len(houses) +1) # memoization array to keep track of the max profits
    backtrack_sol = [-1] * (len(houses) +1)
    for house in range(1,len(houses)+1):
        exclude = memo[house-1]   
        include = memo[house-2] + houses[house-1]  #* house-1 and house+1 are not accessible
        if include > exclude:
            memo[house] = include
            backtrack_sol[house] = house
        else:
            memo[house] = exclude
            backtrack_sol[house] = house-1
    
    house_combo = []
    index = len(memo)-1
    while index > 0:
        if index == backtrack_sol[index]: # if match, it means the current house is included 
            house_combo.append(index)
            index -= 2  # since this house is included, we cannot include house-1
        else:
            index -=1  # this house is not included so check the prev house

    return f'MAX PROFIT: {memo[len(houses)]}\nVISITED HOUSES: {house_combo}'


#? Problem 3
#* solution backtracking part in problem 2


#? Problem 4
def calculate_valid_paths(grid: list[list[bool]]) -> int:
    '''
    :param grid: n x n maze where the starting position is the bottom - left corner cell and the exit is the top right corner cell.
    :return: the total number of avaialble routes a person can take to reach the exit from the start position
    :time complexity: best/worst case:- O(N^2) where N is the size of the grid.
    :space complexity: auxillary complexity: O(N^2) due to memo list creation
                       total complexity: O(N^2 + N^2) = O(N^2) due to memo list and input list
    '''

    memo = [[0] * len(grid) for _ in range(len(grid))]
    n = len(grid)

    #* for top row and last column, the max number of possible paths will be 1;
    #* as we can only move right or up
    #* 0 indicates a wall

    #* start filling up these cells from the exit cuz if we find a wall that means there are no possible routes
    #  fill up top row with available no of paths
    for column in range(n-1,-1,-1):
        if grid[0][column]:
            memo[0][column] = 1
        else:  # no possible routes as there is a wall blocking the exit so stop traversing
            break

    #  fill up last column with available no of paths
    for row in range(n):
        if grid[row][n-1]:
            memo[row][n-1] = 1
        else: 
            break

    for row in range(1,n):
        for col in range(n-2,-1,-1):
            if grid[row][col]:
                memo[row][col] = memo[row-1][col] + memo[row][col+1]
    
    return memo[n-1][0]  # starting cell contains the total number of routes available to exit


#? Problem 5
def calculate_max_money(grid: list[list[bool]]) -> int:
    '''
    :pre-condition: exit has no money
    :param grid: n x n maze where the starting position is the bottom - left corner cell and the exit is the top right corner cell.
    :return: the max money a person can find until the exit from the start position
    :time complexity: best/worst case:- O(N^2) where N is the size of the grid.
    :space complexity: auxillary complexity: O(N^2) due to memo list creation
                       total complexity: O(N^2 + N^2) = O(N^2) due to memo list and input list
    '''

    memo = [[0] * len(grid) for _ in range(len(grid))]
    n = len(grid)


    #  fill up top row with max money per cell
    for column in range(n-2,-1,-1):
        if not grid[0][column]:
            break
        elif grid[0][column] == "$":  # no possible routes as there is a wall blocking the exit so stop traversing
            memo[0][column] = 1 + memo[0][column+1]

    #  fill up last column with max money per cell
    for row in range(1,n):
        if not grid[row][n-1]:
            break
        elif grid[row][n-1] == "$":
            memo[row][n-1] = 1 + memo[row-1][n-1]
            

    for row in range(1,n):
        for col in range(n-2,-1,-1):
            max_coins = max(memo[row-1][col],memo[row][col+1])
            if grid[row][col] and not grid[row][col] == "$":
                memo[row][col] = max_coins
            elif grid[row][col] == "$":
                memo[row][col] = max_coins+1
    
    return memo[n-1][0]  


#? Problem 6

def calculate_size_of_LIS(sequence: list[int]) -> str | int:

    '''
    :param sequence: a list of integers
    :return: a formatted string containing the size of the longest possible increasing subsequence
             and (one of the possible) subsequence with this size.
    :time complexity: best/worst case:- O(N^2) where N is the size of the input list
    :space complexity: auxillary complexity:- O(N+N+N+N) = O(N)
                       total compelxity:-  O(N+4N) = O(N)
    '''
    if not sequence:
        return 0

    #* memo[i] = max subsequence size including seqeunce[i] for a sequence of size i
    memo = [0] * (len(sequence) +1)
    memo[1] = 1                     # max subsequence size of single number is 1 as its the number itself
                                    #also follows memo constraint as the number is included in the subsequence

    backtrack_indices = [-1] * (len(sequence)+1)
    

    for i in range(1,len(sequence)):  # O(N^2) 
        max_length = 1
        prev_index = 0            
        for j in range(i):
            if (sequence[i] > sequence[j]):
                sub_length = 1 + memo[j+1]
                if sub_length > max_length:
                    max_length = sub_length
                    prev_index = j+1
        memo[i+1] = max_length
        backtrack_indices[i+1] = prev_index

    # find max subsequence length
    max_num = 0
    max_num_idx = 0
    for i in range(len(memo)):
        if memo[i] > max_num:
            max_num = memo[i]
            max_num_idx = i
    
    
    no_combo = []
    index = max_num_idx
    while index > 0:
        no_combo.append(sequence[index-1])
        index = backtrack_indices[index]

    # reverse ordering of solution
    reversed_combo  = []
    for i in range(len(no_combo)-1,-1,-1):
        reversed_combo.append(no_combo[i])

    return f"Given Sequence: {sequence}\nSize of Longest Increasing Subsequence: {max_num}\
        \nLongest Increasing Subsequence: {reversed_combo}"

#? Problem 7
def calculate_longest_common_subsequence(seq1:list[str] |str, seq2: list[str] |str) -> str:

    memo: list[list[int]] = [[0 for _ in range(len(seq1) +1)] for _ in range(len(seq2)+1)]
    backtrack_indices: list[tuple[int,int]] = []

    for row in range(1, len(memo)):
        for col in range(1,len(memo[0])):
            max_prev_lcs = 0
            top_cell = memo[row-1][col]
            left_cell = memo[row][col-1]
            diagonal_cell = memo[row-1][col-1]
            if top_cell >= left_cell and top_cell >= diagonal_cell:
                backtrack_indices.append((row-1,col))
                max_prev_lcs = top_cell
            elif diagonal_cell >= top_cell and diagonal_cell >= left_cell:
                backtrack_indices.append((row-1,col-1))
                max_prev_lcs = diagonal_cell
            else:
                backtrack_indices.append((row,col-1))
                max_prev_lcs = left_cell
            memo[row][col] = max_prev_lcs + 1 if seq1[col-1] == seq2[row-1] else max_prev_lcs

    lcs_length = memo[len(seq2)][len(seq1)]
    print(backtrack_indices)
    sol = []
    indices: tuple[int,int] = (len(memo)-1,len(memo[0])-1)
    while indices[0] != 0 or indices[1] != 0:
        if seq1[indices[1]-1] == seq2[indices[0]-1]:
            sol.append(seq1[indices[1]-1])
            indices = indices[0]-1,indices[1]-1
        else:
            indices = indices[indices[0]],indices[indices[1]-1]


    return f'Length of LCS: {lcs_length}\nLCS: {sol}'

# The longest common subsequence in Python

#* TAKEN FROM THE INTERNET
# Function to find lcs_algo
def lcs_algo(S1, S2, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    # Building the mtrix in bottom-up way
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]

    lcs_algo = [""] * (index+1)
    lcs_algo[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i-1] == S2[j-1]:
            lcs_algo[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    # Printing the sub sequences
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "".join(lcs_algo))

#? Problem 8    
def max_sum_subarrs(seq: list[int]) -> str:
    n = len(seq)
    
    # memo[i][j] = sum of seq[i....j] inclusive
    memo = [[0 for _ in range(n)] for _ in range(n)]  # Note: we only need the upper half of the matrix
    
    # Fill up the diagonal first as each subarray contains one element,
    # so the sum is that element; seq[i...i]
    for i in range(n):
        memo[i][i] = seq[i]

    # Iterate over the upper triangle of the matrix
    for i in range(n - 1):
        for j in range(n - i - 1):
            row = j
            col = j + i + 1
            memo[row][col] = memo[row][col - 1] + seq[col]  

    # Find the maximum sum
    max_sum = 0
    for row in range(n):
        for col in range(row, n):
            max_sum = max(memo[row][col], max_sum)

    return f'Maximum sum from subarrays: {max_sum}'

#* VINGU VERSION :)
def vingu_max_sum_subarray(arr: list[int]) -> str:
    n = len(arr)
    memo = [[0 for _ in range(n)] for _ in range(n)] #! lower triangle not used; can be optimised further but same time comp
    
    # fill up diagonal as the subarrays are of size 1
    for row in range(n):
        col = row
        memo[row][col] = arr[row]

    #* think in terms of the first cell for finding the formula for col 
    for i in range(n):
        for j in range(n-i-1):
            col = i +j+1
            memo[i][col] = memo[i][col-1] + arr[col]

    max_sum = 0
    for i in range(n):
        for j in range(n-i):
            col = i +j
            max_sum = max(memo[i][col], max_sum)
    
    return f'Maximum sum from subarrays: {max_sum}'
    

if __name__ == "__main__":
    #print(calculate_salesman_profit([50,10,12,65,40,95,100,12,20,30,11]))
    
    grid = [[False,False,True,True,False,False,True],
            [False,False,"$",True,"$",True,"$"],
            [True,True,True,True,True,False,True],
            [True,"$",True,"$",False,True,True],
            [True,False,True,True,True,"$",True],
            [True,False,False,True,True,False,False],
            [True,True,"$","$",True,False,True]]
    
    grid5 = [["$", "$", "$", "$", True],
         [True, False, "$", False, True],
         [True, True, "$", "$", True],
         [True, False, False, False, True],
         [True, True, True, True, True]]
 
    grid2 = [[False,False,True,True,False,False,True],
            [False,False,"$",True,"$",True,"$"],
            [True,True,True,True,True,False,"$"],
            [True,"$",True,"$",False,True,"$"],
            [True,False,True,True,True,"$",True],
            [True,False,False,True,True,False,False],
            [True,True,"$","$","$",False,True]]

    #print(calculate_max_money(grid5))
    # print(calculate_size_of_LIS([3]))
    #print(lcs_algo("aabcd","abxc",5,4))
    print(vingu_max_sum_subarray([]))