def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m
    larr = [0]*n1
    rarr = [0]*n2

    for i in range(0, n1):
        larr[i] = arr[l+i]
    for j in range(0, n2):
        rarr[j] = arr[m+1+j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = larr[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = rarr[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        mid = l+(r-l)//2
        mergeSort(arr, l, mid)
        mergeSort(arr, mid+1, r)
        merge(arr, l, mid, r)


a = eval(input("Enter list :"))
n = len(a)
mergeSort(a, 0, n-1)
print("Sorted array : ")
for i in range(0, n):
    print(a[i], end=" ")
print()
