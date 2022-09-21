def obtener_datos():
    f = open("segundo_problema.txt", "r")
    linea = f.readline().strip('\n')
    restricciones = {}
    tiempos = {}
    cantidad_prendas = 0
    cantidad_restricciones = 0
    while linea:
        terminos = linea.split(" ")
        if (terminos[0] == "p"):
            cantidad_prendas = terminos[2]
            cantidad_incompatibilidades = terminos[3]
        elif (terminos[0] == "e"):
            if terminos[1] not in restricciones:
                restricciones[terminos[1]] = set()
                restricciones[terminos[1]].add(terminos[2])
            else:
                restricciones[terminos[1]].add(terminos[2])
        elif (terminos[0] == "n"):
            tiempos[terminos[1]] = int(terminos[2])
        linea = f.readline().strip('\n')
    f.close()
    tiempos_ordenados = dict(sorted(tiempos.items(), key = lambda item: -item[1]))
    return cantidad_prendas, cantidad_incompatibilidades, restricciones, tiempos_ordenados

def lavar_prendas(restricciones, tiempos):
    solucion = open("solucion_entrega2.txt", "w")
    numero_lavado = 0
    tiempo_total = 0
    lavadas = set()
    for prenda in tiempos:
        if prenda not in lavadas:
            numero_lavado += 1
            grupo_lavado = [prenda]
            excluidos_lavado = restricciones[prenda]
            tiempo = tiempos[prenda]
            solucion.write(f"{prenda} {numero_lavado}\n")
            #print(f"Lavado de prenda: {prenda}. tiempo necesario: {tiempo}")
            lavadas.add(prenda)
            tiempo_total += tiempo
            for otra_prenda in tiempos:
                if otra_prenda != prenda and otra_prenda not in excluidos_lavado and otra_prenda not in lavadas:
                    #print(f"Lavado compatible con prenda {otra_prenda}")
                    grupo_lavado.append(otra_prenda)
                    excluidos_lavado = excluidos_lavado.union(restricciones[otra_prenda])
                    lavadas.add(otra_prenda)
                    solucion.write(f"{otra_prenda} {numero_lavado}\n")
    solucion.close()

    return tiempo_total, numero_lavado


def main():
    cantidad_prendas, cantidad_incompatibilidades, restricciones, tiempos = obtener_datos()
    print(f"Prendas: {cantidad_prendas}. Incompatibilidades: {cantidad_incompatibilidades}")
    tiempo_total, cantidad_lavados = lavar_prendas(restricciones, tiempos)
    print(f"Tiempo total consumido: {tiempo_total}. Lavados realizados: {cantidad_lavados}")
    




if __name__ == '__main__':
    main()