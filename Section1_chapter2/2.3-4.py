"""
	递归实现插入排序
	举出一个最坏情况的实例
"""

def Insertion(A):
	if len(A) == 1:
		return A
	temp = A[len(A) - 1]
	for i in range(len(A) - 1, 0, -1):
		if A[i - 1] <= temp:
			A[i] = temp
			break
		else:
			A[i] = A[i - 1]
	if A[0] == A[1]:
		A[0] = temp
	return A

def InsSort(C, A): 
	if len(C) == len(A):
		return C
	else:
		C.append(A[len(C)])
		return InsSort(Insertion(C), A)


print(InsSort([3], [3,41,52,26,38,57,9,49]))