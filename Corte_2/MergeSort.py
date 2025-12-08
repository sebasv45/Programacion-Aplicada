def merge(arr, l, m, r):
    # Tamaños de los subarreglos
    n1 = m - l + 1
    n2 = r - m

    # Subarreglos temporales
    L = arr[l : l + n1]
    R = arr[m + 1 : m + 1 + n2]

    # Índices iniciales
    i = 0   # índice de L[]
    j = 0   # índice de R[]
    k = l   # índice de arr[]

   
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

   
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2   # punto medio

        mergeSort(arr, l, m)       # Ordenar mitad izquierda
        mergeSort(arr, m + 1, r)   # Ordenar mitad derecha
        merge(arr, l, m, r)        # Mezclar ambas


def main():
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    mergeSort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    for x in arr:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    main()
