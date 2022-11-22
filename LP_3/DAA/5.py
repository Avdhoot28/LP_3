import random


def partition(array, low, high, piv):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
	if low < high:
		if randomized:
			piv = random.randrange(low, high)
		else:
			piv = high
		pi = partition(array, low, high, piv)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)


randomized = bool(int(input("Enter 0 for fixed, 1 for randomized pivot : ")))
data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)
randomized = True
quickSort(data, 0, size - 1)
print("Sorted Array in Ascending Order:")
print(data)
