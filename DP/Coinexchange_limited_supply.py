

def find_min(a, b):
    if a <= b:
        return a
    else:
        return b


def find_min_coins(c, sum):
    # Storing total number of available coins:
    size = len(c)

    # Declaring a 2-D list, filled with zeroes:
    arr = [[0] * (sum + 1) for x in range(size + 1)]

    # Initialising first column of list with 0
    # because a sum of 0 can be made with zero coins:
    for i in range(size + 1):
        arr[i][0] = True
    #arr[0][0] = True
    # Initialising first row of list with +ve infinity
    # because a sum cannot be made with 0 coins:
    for j in range(sum + 1):
        arr[0][j] = False

    # Using recursive solution:
    for i in range(1, size + 1):
        for j in range(1, sum + 1):
            mm1 = arr[i - 1][j]
            mm2 = arr[i][j - c[i - 1]]
            if c[i - 1] > j:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = arr[i - 1][j] or arr[i-1][j - c[i - 1]] 

    return arr[size][s]


coins = [1,1,2,2,5,5]
s = 15
print("At least %s coins are required to make a sum of %s"
      % (find_min_coins(coins, s), s))
