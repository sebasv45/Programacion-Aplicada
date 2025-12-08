def firstOccurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid
            high = mid - 1   # seguir buscando a la izquierda
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return result


def lastOccurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid
            low = mid + 1    # seguir buscando a la derecha
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return result


def main():
    
    arr = [3, 5, 7, 9, 11, 11, 11, 11, 13, 15]
    print("Arreglo (ordenado):", arr)

    key = int(input("Ingrese el número a buscar: "))

    first = firstOccurrence(arr, key)
    last = lastOccurrence(arr, key)

    if first == -1:
        print(f"El número {key} NO se encuentra en el arreglo.")
    else:
        count = last - first + 1
        print(f"El número {key} aparece {count} veces.")
        print("Posiciones (índices 0-based):", list(range(first, last + 1)))


if __name__ == "__main__":
    main()
