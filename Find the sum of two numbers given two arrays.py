# Create a program in Python3 that
# finds the sum of two numbers m and n, 
# where m is part of the first array arr1
# and is is part of the secon array arr2
# and list all the sums that add up to a 
# given x value.
def findPairs (arr1, arr2, m, n, x):

    for i in range(0, m):
        for j in range(0, n):
            if (arr1[i] + arr2[j] == x):
                print(arr1[i], arr2[j])

# driver code
arr1 = [1, 0, 3, 4, 9]
arr2 = [3, 6, 7, 9, 10]
m = len(arr1)
n = len(arr2)
x = 12
findPairs (arr1, arr2, m, n, x)
