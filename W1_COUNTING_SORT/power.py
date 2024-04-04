# expotentiation by squaring 
def calculate_power(base: int, power: int) -> int:
    if power == 0:
        return 1
    elif power == 1:
        return base
    y = calculate_power(base,power//2)
    if power % 2 == 0:
        return y*y
    else:
        return base * y*y
    




if __name__  == "__main__":
    print(calculate_power(3,5))
