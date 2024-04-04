from W4_item_class import Item


# unbounded knapsack problem with memoization (bottom up) iterative algorithm
def unbounded_knapsack_iter(total_weight: int, items_arr: list[Item]) -> int:
    memo = [0] * (total_weight+1)
    for weight in range(1,total_weight+1):
        for item in items_arr:
            if item.get_weight() <= weight:
                difference = weight - item.get_weight()
                value = item.value + memo[difference]
                if value > memo[weight]:
                    memo[weight] = value
    return memo[total_weight]

# unbounded knapsack problem recursive alogorithm
def unbounded_knapsack_rec(total_weight: int, items_arr: list[Item]):
    memo = [-1] * (total_weight+1)
    memo[0] = 0
    return _unbounded_knapsack_rec_aux(total_weight,items_arr,memo)


def _unbounded_knapsack_rec_aux(total_weight: int, items_arr: list[Item], mem_arr: list[int]) -> int:
    if mem_arr[total_weight] != -1:
        return mem_arr[total_weight]
    else:
        max_value = 0
        for item in items_arr:
            if item.get_weight() <= total_weight:
                difference = total_weight-item.get_weight()
                value = item.get_value() + _unbounded_knapsack_rec_aux(difference,items_arr,mem_arr)
                if value > max_value:
                    max_value = value
        mem_arr[total_weight] = max_value
        return max_value

# bounded knapsack (2d problem) bottoms up algorithm using matrix3 for memoization
def bounded_knapsack_iter(total_weight: int, items_arr:list[Item]):
    # initialize a 2d matrix for memoization [#!SEE W4/BOUNDED_KNAPSACK_MATRIX.png]
    n = len(items)
    memo = [[0 for _ in range(total_weight+1)] for _ in range(n+1)] 

    for item_row in range(1,n+1):
        for weight_col in range(1,total_weight+1):
            exclude = memo[item_row-1][weight_col]
            include = 0
            if items[item_row-1].get_weight() <= weight_col:
                difference = weight_col - items[item_row-1].get_weight()
                include = items[item_row-1].get_value() + memo[item_row-1][difference]
            memo[item_row][weight_col] = max(exclude,include)
    return memo[n][total_weight]


if __name__ == "__main__":
    items = [Item(6,230),Item(1,40),Item(5,350), Item(9,550)]
    #print(unbounded_knapsack_rec(10,items))
    print(bounded_knapsack_iter(12,items))
    
    