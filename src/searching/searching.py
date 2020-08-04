def linear_search(arr, target):
    # Your code here
    for i, elem in enumerate(arr):
        if elem==target:
            return i

    return -1   # not found
# print(linear_search([3,5,6], 8))

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        middle = (low+high)//2
        guess = arr[middle]
        if guess == target:
            return middle
        elif guess >= target:
            high = middle - 1
        elif guess <= target:
            low = middle + 1
    # Your code here
    


    return -1  # not found


