def linearSearch(arr, key):
    """Devuelve la primera aparición de key o -1 si no existe."""
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def linearSearchAll(arr, key):
    """Devuelve una lista con todos los índices donde aparece key."""
    indices = []
    for i in range(len(arr)):
        if arr[i] == key:
            indices.append(i)
    return indices


def main():
    # Arreglo de ejemplo
    arr = [4, 9, 2, 7, 5, 7, 9, 7]
    print("Arreglo:", arr)

    key = int(input("Ingrese el número a buscar: "))

   
    pos = linearSearch(arr, key)

    if pos == -1:
        print(f"El número {key} NO se encuentra en el arreglo.")
    else:
        print(f"El número {key} se encuentra (al menos) en la posición {pos} (índice 0-based).")


    indices = linearSearchAll(arr, key)

    if len(indices) == 0:
        print(f"No se encontraron ocurrencias de {key}.")
    else:
        print(f"El número {key} aparece {len(indices)} veces, en las posiciones: {indices}")


if __name__ == "__main__":
    main()
