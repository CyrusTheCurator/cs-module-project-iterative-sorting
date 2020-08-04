# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)): 
            if arr[smallest_index] > arr[j]: 
                smallest_index = j 

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]





        # TO-DO: swap
        # Your code here

    return arr

selecto_perfecto = selection_sort([8,3,6,7,10,10,10,99,99,300])


print("Selection Sort: ",selecto_perfecto)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here


    return arr



def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr 
  
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 2] 
  
zee = bubbleSort(arr) 
  
print ("Bubble Sort: ",zee) 




'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    #declare a bucket array sized to "maximum" in indices, with starting vals of 0
    bucket_list = [0] * (maximum+1)


    # Fill our "Buckets" with a log of each instance of a value
    for i, elem in enumerate(arr):
        bucket_list[elem] += 1


    # modify all bucket list entries: for all indices beyond 1, modify that indexes value to be the sum of itself----
    # and the previous index. Don't question the magic.
    for i, elem in enumerate(bucket_list):
        if i < 1:
            continue
        bucket_list[i] +=  bucket_list[i-1]


    #Create a new array into which we will throw our sorted elements
    new_arr = [None] * len(arr)


# COOL STUFF HERE: loop through original array. for each value in original, assign the corresponding value
# of bucket_list[elem], which returns the count of how many instances of elem there are, as the index of new_arr to insert the current element.
# Also don't forget to shift the index -1 (as seen on line 116) in order to start at index 0 instead of 1.
    for i, elem in enumerate(arr):

        #We have a condition here to prevent accidental traversal into negatives from decrementing
        if bucket_list[elem] > 0:
            new_arr[bucket_list[elem]-1] = elem
            bucket_list[elem] -= 1

    arr = new_arr

    return arr

test_arr = [1,7,9,2,5,10,8]

print("Counting Sort: ",counting_sort(test_arr, 10))




# def fibonacci(start, iterations):
#     arr = start
#     for i in range(iterations):
#         if i >= 2:
#             print(i)
#             arr.append(arr[i-1]+arr[i-2])
#     print(arr)
    
# fibonacci([0,1], 100)


