"""
 	两个n位的二进制整数分别存储在A和B中，把两个二进制整数相加
 	按照二进制形式存储在一个(n+1)元数组C中
"""

"""
	知识点：
		range()用法
		range(6,1,-1) 从6到1间隔-1, 从6到1（不包括1）
		range(5) 0到5 不包括 5
		
		len(array)求array数组的长度

		list.reverse()没有返回值，直接逆原list
"""

def binaryAdd(A, B):

 	carry = 0

 	C = []
 	for i in range(len(A)-1, -1, -1):
 		if(A[i] == B[i] and A[i] == 1):
 			C.append(0 + carry)
 			carry = 1
 		if(A[i] != B[i] and (A[i] == 0 or B[i] == 0)):
 			temp = 1 + carry
 			if(temp == 2):
 				temp = 0
 				carry = 1
 			else:
 				carry = 0
 			C.append(temp) 
 		if(A[i] == B[i] and A[i] == 0):
 			C.append(0 + carry) 
 			carry = 0
 		if(i == 0):
 			C.append(carry)
 	return C

A = binaryAdd([1,0,1,0,1,1,1,1,1,1], [1,0,1,0,1,1,0,1,0,1])
A.reverse()
print(A)

 		

