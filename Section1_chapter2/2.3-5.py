"""
	有序数列，二分查找，迭代，递归
"""

import math

# 迭代
def BinarySearch(c, A):
	mid = math.floor(len(A) - 1 / 2)
	left = 0
	right = len(A) - 1

	while right > left:
		if A[mid] > c:
			right = mid - 1
			mid = math.floor(( left + right ) / 2)
		elif A[mid] < c:
			left = mid + 1
			mid = math.floor(( left + right ) / 2)
		elif A[mid] == c:
			return mid

	return -1

# 递归
# def BinarySearch(c, right, left, A):
# 	if right < left:
# 		return -1

# 	mid = math.floor(( left + right ) / 2)
# 	if A[mid] > c:
# 		right = mid - 1
# 		return BinarySearch(c, right, left, A)
# 	elif A[mid] < c:
# 		left = mid + 1
# 		return BinarySearch(c, right, left, A)
# 	elif A[mid] == c:
# 		return mid

A = [1,3,5,7,9,19,100]
c = 8
print(BinarySearch(c, A))


