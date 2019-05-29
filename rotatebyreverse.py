#breaks the input array into two parts. first part is from 0 to rotatestepsize -1
#and second part is from rotatestepsize until the end of array. Finally rotate the combination
#arr : array input ; rotatestep: the number of rotations
def rotatebyreversing(arr, rotatestep):
	return (arr[:rotationstepsize-1][::-1] + arr[rotationstepsize:][::-1])[::-1]
	pass

inputarray = [3,4,5,6,7,8,9]
rotationstepsize = 3
print rotatebyreversing(inputarray, rotationstepsize)