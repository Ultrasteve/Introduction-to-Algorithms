"""
	归并排序
	输入数组【3，41，52，26，38，57，9，49】
"""

# 方法一：
# import math

# def Merge(A, p, q, r):
# 	C = []
# 	D = []
# 	result = []
# 	for i in range(q - p + 1):
# 		C.append(A[p + i])
# 	for i in range(r - q):
# 		D.append(A[q + 1 + i])
	
# 	C.append(999999)
# 	D.append(999999)
# 	c = 0
# 	d = 0
# 	while C[c] != 999999 and D[d] != 999999:
# 		if C[c] > D[d]:
# 			result.append(D[d])
# 			d += 1
# 		else:
# 			result.append(C[c])
# 			c += 1
# 	if c == len(C) - 1:
# 		for i in range(d, len(D)-1):
# 			result.append(D[d])
# 	if d == len(D) - 1:
# 		for i in range(c, len(C)-1):
# 			result.append(C[c])
# 	for i in range(len(result)):
# 		A[p + i] = result[i]

# def MergeSort(A, p, r):
# 	if r > p:
# 		q = math.floor((p + r) / 2)
# 		MergeSort(A, p, q)
# 		MergeSort(A, q + 1, r)
# 		Merge(A, p, q, r)

# A = [3,41,52,26,38,57,9,49]
# MergeSort(A, 0, len(A)-1)
# print(A)


# 方法二：利用python list的性质
"""
	list[1:5] 下标为1 到 5 之间的的数 包括1 不包括 5
	list[1:] 下标为1之后的元素 包括1
	list[:5] 下标为5之前的元素 不包括5
"""


import math

def Merge(A, B):
	result = []
	A.append(9999999)
	B.append(9999999)

	a = 0
	b = 0

	while A[a] != 9999999 and B[b] != 9999999:
		if A[a] > B[b]:
			result.append(B[b])
			b += 1
		if A[a] < B[b]:
			result.append(A[a])
			a += 1
	if a == len(A) - 1:
		for i in range(b, len(B) - 1):
			result.append(B[b])
	if b == len(B) - 1:
		for i in range(a, len(A) - 1):
			result.append(A[a])
	return result

def MergeSort(A):
	if len(A) <= 1:
		return A
	temp = math.floor(len(A)/2)
	left = MergeSort(A[:temp])
	right = MergeSort(A[temp:])
	result = Merge(left, right)
	return result

print(MergeSort([3,41,52,26,38,57,9,49]))


