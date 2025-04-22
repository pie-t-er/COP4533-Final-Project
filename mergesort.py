import numpy as np

# General merge sort algorithm, recursively calls itself until the base case is reached.
def mergeSort(array):
  
  n = len(array)
  # base case of only one element in the array:
  if n <= 1:
    return array

  # setting the midpoint:
  if n%2 == 0:
      mid = int(n/2)
  else:
      mid = int(n/2)+1

  # splitting the array down the middle and recursively sorting the halves:
  left = mergeSort(array[0:mid])
  right = mergeSort(array[mid:n])

  # merging and returning the sorted halves of the array:
  return merge(left, right)

# Helper function for merging two already sorted halves of the array:
def merge(left, right):

  # initializing the resulting sorted array and the indices of interest:
  result = []
  i = 0
  j = 0

  # looping through the elements of both arrays to compare and place in sorted array:
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
   
  # the remaining elements can be assumed to be greater than all the elements already placed in the array, and will only come from one half of the array.

  # looping through the remaining elements to clean up and add to sorted array:
  while i < len(left):
    result.append(left[i])
    i += 1
  while j < len(right):
    result.append(right[j])
    j += 1

  # resulting array is fully sorted.
  return result

if __name__ == "__main__":

    given = input("Enter numbers separated by spaces: ")
    unsorted = list(map(int, given.split()))
    arr = mergeSort(unsorted)
    print("Sorted array:", arr)