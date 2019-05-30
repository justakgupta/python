def rearrange(arr):
	#navigate the array until the length of the array
	for i in range(len(arr)):
		#if the element is not equal to -1 or the element is not at the correct position
		#then move in to the condition, else continue the loop.
		if(arr[i] != -1 and arr[i] != i): 
				#store the value of bad positioned element in a temp variable
				x = arr[i]
				#in a while loop, find if the correct position of the picked element is filled
				#correctly or not. if not then enter this loop else continue the mother loop
				while (arr[x] != -1 and arr[x] != x):
					#store the incorrectly placed element in a temporary variable
					y = arr[x]
					#place the right value to this position
					arr[x] = x
					#update the value of incorrect element and continue the quest to place
					#the new value at its right place
					x = y
				#when you are here, that means that the secondary bad placed elements
				#have been placed well. now its time to place the first bad positioned
				#element to its right place
				arr[x] = x
				#check if the value of the position is not right then, initialize it to -1
				if (arr[i] != i):
					arr[i] = -1	
					pass
		pass
	return arr #return the array. you did the right thing son!

inputarray = [-1, -1, 9, 1, 9, 3, 2, -1, 4, -1]
print rearrange(inputarray)