def heapify(arr, n, i):
    # place the max el at root
    max = i
    left = 2*i+1
    right = 2*i+2

    if (left < n and arr[left] > arr[max]):
        max = left
    if (right < n and arr[right] > arr[max]):
        max = right

    if max != i:
        arr[i], arr[max] = arr[max], arr[i]
        heapify(arr, n, max)


def heapsort(arr):
    n = len(arr)

    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


a = eval(input("Enter list :"))
n = len(a)
heapsort(a)
print("Sorted array : ")
for i in range(0, n):
    print(a[i], end=" ")
print()
