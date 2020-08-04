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


    return arr






# def fibonacci(start, iterations):
#     arr = start
#     for i in range(iterations):
#         if i >= 2:
#             print(i)
#             arr.append(arr[i-1]+arr[i-2])
#     print(arr)
    
# fibonacci([0,1], 100)


