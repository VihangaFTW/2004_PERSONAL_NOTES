from my_queue import CircularQueue

def findPath(maze, start, destination):
    '''
    Function to find whether there is at least one valid path from start cell to destination cell.
    Blocked cells are represented by 1 and open cells are represented by 0.
    Uses a dynamic programming approach to find a valid path, starting from the end. Why? this ensures we are calcuating the 
    correct local optimal each step, we keep building up the local optimal iteratively using memoization until we hit the
    global optimal; the start cell. The result at the start cell (True/False) is the global optimal.
    : time complexity:- O(row*col) where row and colum are the dimensions of the same
    '''
    # validate start and destination
    try:
        start_check, end_check = maze[start[0]][start[1]], maze[destination[0]][destination[1]]
    except:
        return "Invalid maze indices for start and/or destination!"
    
    # make sure start and destination are open cells 
    if maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] ==  1:
        return False
    
    # memoization array for storing local optimals
    memo = [None] * len(maze)
    for i in range(len(maze)):
        memo[i]  = [False for _ in range(len(maze[i]))]

    # botth queue and stack will work here since problem only wants the existence of a valid path
    queue = CircularQueue(len(maze)*2)
    queue.append((destination[0],destination[1]))
    
    # perform a bfs search until we hit the start cell or run out of valid paths 
    while queue:
        cell = queue.serve()
        row = cell[0]
        col = cell[1]

        if row == start[0] and col == start[1]:
            memo[row][col] = True
            break
        
        # check up
        if row-1 >= 0  and maze[row-1][col] == 0 and not memo[row-1][col]:
            memo[row][col] = True
            queue.append((row-1,col))
        # check down
        if row+1 < len(maze)  and maze[row+1][col] == 0 and not memo[row+1][col]:
            memo[row][col] = True
            queue.append((row+1,col))

        # check left
        if col-1 >= 0 and maze[row][col-1] == 0 and not memo[row][col-1]:
            memo[row][col] = True
            queue.append((row,col-1))

        # check right
        if col+1 < len(maze[row]) and maze[row][col+1] == 0 and not memo[row][col+1]:
            memo[row][col] = True
            queue.append((row,col+1))

    return memo[start[0]][start[1]]



if __name__ == '__main__':
    print(findPath([[0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0]], [0,0], [4,4]))