from math import inf


# coin change buttom up (iterative) solution using memoization
def coin_change_dp(n: int, coins: list)-> int | float:
    '''
    :param n: sum of coins 
    :param coins: list of coins 
    :return: the least number of coins needed for sum or "inf" indicating no combination of coins possible for sum
    :complexity: O(NM) where N is the sum of coins and M is length of "coins" list
    '''
    memo = [inf] * (n+1)  #? O(N)
    memo[0] = 0

    for sum in range(1,n+1):  #? O(N)
        for coin_idx in range(len(coins)):   #? O(M)
            if coins[coin_idx] <= sum:
                balance = sum - coins[coin_idx]
                count = 1 + memo[balance]
                if count < memo[sum]:
                    memo[sum] = count
    
    return memo[n]



# coin change top down (recursion) solution using memoization
def coin_change_recur(n: int, coins: list):
    memo = [-1] * (n+1)
    memo[0] = 0
    return _coin_change_recur_aux(n,coins,memo)



def _coin_change_recur_aux(n: int, coins: list, memo_arr: list):
    if memo_arr[n] != -1:  # * -1 means min count not yet calculated for that sum
        return memo_arr[n]
    else: # need to find the min for this sum/index
        min_coins = inf  # placeholder for min combos
        for coin in coins:
            if coin <= n:
                count =  1 + _coin_change_recur_aux(n-coin, coins,memo_arr)
                if count < min_coins:
                    min_coins = count
        memo_arr[n] = min_coins
        return memo_arr[n]


if __name__ == "__main__":
    print(coin_change_dp(7,[1,24,6,9]))

