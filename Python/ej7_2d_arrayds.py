"""Given a 6x6 2D Array, arr:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:

a b c
  d
e f g

There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6x6."""


def hourglassSum(arr):
    otherList=[]
    for r in range(len(arr)-2):
        for s in range(len(arr)-2):
            otherList.append(sum([arr[r][s], arr[r][s+1], arr[r][s+2],
            arr[r+1][s+1],
            arr[r+2][s], arr[r+2][s+1], arr[r+2][s+2]]))

    return max(otherList)
