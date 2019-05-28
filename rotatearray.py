def rotate(arr, length, rotations):
	rotatedarray = arr[0-rotations:][::-1] + arr[:0-rotations]
	print rotatedarray
	pass

arr = [4,5,6,7,2,1]
print arr
rotate(arr, len(arr), 2)