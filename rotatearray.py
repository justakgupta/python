#takes name of array, and requried number of rotations
def rotate(arr, rotations):
	rotatedarray = arr[0-rotations:][::-1] + arr[:0-rotations]
	print("rotated array is : ")
	print(rotatedarray)
	pass

numberofelements = int(input("enter the number of elements in the array: "))
elements = input("enter " + str(numberofelements) + " CSV values: ")
arr = elements.split(',')
rot = int(input("how many rotations? : "))
print("default array is : ")
print(arr)
rotate(arr, int(rot % numberofelements))