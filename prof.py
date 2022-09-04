from sys import stdin
input = stdin.readline

def printVector(arr):
 
    if (len(arr) != 1):
 
        # Traverse the vector arr
        for i in range(len(arr)):
            print(arr[i], end = " ")
        print()   
 
# Recursive function to print different
# ways in which N can be written as
# a sum of at 2 or more positive integers
def findWays(arr, i, n):
 
    # If n is zero then print this
    # ways of breaking numbers
    if (n == 0):
        printVector(arr)
 
    # Start from previous element
    # in the representation till n
    for j in range(i, n + 1):
 
        # Include current element
        # from representation
        arr.append(j)
 
        # Call function again
        # with reduced sum
        findWays(arr, j, n - j)
 
        # Backtrack to remove current
        # element from representation
        del arr[-1]
	

def main():
	n = int(input())
	breakpoint()
	arr = []
	findWays(arr, 1, n)
main()
