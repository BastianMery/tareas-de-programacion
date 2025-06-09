def gen_combinaciones_parentesis(n):
    resultado = []

    def backtrack(abierto, cerrado, cadena):
        if abierto == 0 and cerrado == 0:
            resultado.append(cadena)
            return

        if abierto > 0:
            backtrack(abierto - 1, cerrado, cadena + "(")

        if cerrado > abierto:
            backtrack(abierto, cerrado - 1, cadena + ")")

    backtrack(abierto = n, cerrado = n, cadena = "")

    return resultado

n = int(input("Seleccione un numero de parentesis: "))

print(gen_combinaciones_parentesis(n))