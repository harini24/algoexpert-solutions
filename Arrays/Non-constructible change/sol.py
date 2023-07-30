# O(nlogn) time and O(1) space

def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    minConstructableChange = 0
    for coin in coins:
        if coin > minConstructableChange + 1:
            break
        minConstructableChange+=coin
    return minConstructableChange+1
