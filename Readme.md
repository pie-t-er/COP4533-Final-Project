Merge Sort

Overview -

Merge sort is a divide and conquer algorithm typically uses to sort very large datasets.

How It Works -

Merge sort breaks the original input into halves until each subproblem is of size one. It then recursively sorts each half until each subproblem is sorted. Finally it combines each sub-solution to reconstruct the sorted array.


Usage -

Run the script using Python:

$ python mergesort.py


Example Input & Output -

Sample Input (terminal):
3 2 5 7 4 4 3


Sample Output (terminal):
2 3 3 4 4 5 7


Data Structures Used -

List: used to store each subproblem and the final array.


Time Complexity Analysis -

The time complexity of this algorithm is guaranteed to alway be O(nlogn).

The space complexity of this algorithm is guaranteed to always be O(n).