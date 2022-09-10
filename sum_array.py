def sum_array(arr):
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])


if __name__ == '__main__':
    print(sum_array([1, 2, 3, 10, 15]))
