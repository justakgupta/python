def rearrange(arr):
	#navigate the array if a[i] = -1 then leave
	for i in range(len(arr)):
		#print arr[i]
		if(arr[i] != -1 and arr[i] != i):
				x = arr[i]
				while (arr[x] != -1 and arr[x] != x):
					y = arr[x]
					arr[x] = x
					x = y
				arr[x] = x
				if (arr[i] != i):
					arr[i] = -1	
					pass
	return arr
		# pass

inputarray = [-1, -1, 9, 1, 9, 3, 2, -1, 4, -1]
print rearrange(inputarray)