def permutation(arr, n):
    result = []
    
arr=int(input())
n=int(input())

    if n == 0:
        return [[]]

    for i, elem in enumerate(arr):
        for PermResult in permutation(arr[:i] + arr[i + 1:], n - 1):
            result += [[elem] + PermResult]
    return result

arr = [1, 2]
print(permutation(arr, 2))