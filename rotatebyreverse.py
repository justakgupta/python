def rotatebyreversing(arr, rotatestep):
	return (arr[:rotationstepsize-1][::-1] + arr[rotationstepsize:][::-1])[::-1]
	pass

inputarray = [3,4,5,6,7,8,9]
rotationstepsize = 3
print rotatebyreversing(inputarray, rotationstepsize)