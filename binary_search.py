def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = list[middle]
        if guess == item:
            return middle
        if guess < item:
            low = middle + 1
        else:
            high = middle - 1
    return low, high


if __name__ == '__main__':
    l = [1, 3, 5, 7, 8, 101]
    print(binary_search(l, 7))
