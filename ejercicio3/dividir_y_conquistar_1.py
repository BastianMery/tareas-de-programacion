def binary_search(arr, x):
    def buscar(izq, der):
        if izq > der:
            return -1
        medio = (izq + der) // 2

        if arr[medio] == x:
            return medio

        elif arr[medio] > x:
            return buscar(izq, medio - 1)

        else:
            return buscar(medio + 1, der)

    return buscar(0, len(arr) - 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while True:
    x = int(input("Numero a buscar, del 1 al 10: "))
    if x > 10 or x < 1:
        print("Numero invalido")
    else:
        print(binary_search(arr, x))



