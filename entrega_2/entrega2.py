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
            cantidad_prendas = int(terminos[2])
            cantidad_incompatibilidades = int(terminos[3])
            for i in range (1, cantidad_prendas + 1):
                restricciones[str(i)] = set()
        elif (terminos[0] == "e"):
            restricciones[terminos[1]].add(terminos[2])
            restricciones[terminos[2]].add(terminos[1])
        elif (terminos[0] == "n"):
            tiempos[terminos[1]] = int(terminos[2])
        linea = f.readline().strip('\n')
    f.close()
    tiempos_ordenados = dict(sorted(tiempos.items(), key = lambda item: -item[1]))
    restricciones_ordenadas = dict(sorted(restricciones.items(), key = lambda item: len(item[1])))
    return cantidad_prendas, cantidad_incompatibilidades, restricciones_ordenadas, tiempos_ordenados

def lavar_prendas(restricciones, tiempos, diccionario_a_iterar):
    solucion = open("solucion_entrega2.txt", "w")
    numero_lavado = 0
    tiempo_total = 0
    lavadas = set()
    for prenda in diccionario_a_iterar:
        if prenda not in lavadas:
            numero_lavado += 1
            grupo_lavado = [prenda]
            excluidos_lavado = restricciones[prenda]
            tiempo = tiempos[prenda]
            solucion.write(f"{prenda} {numero_lavado}\n")
            #print(f"Lavado de prenda: {prenda}. tiempo necesario: {tiempo}")
            lavadas.add(prenda)
            #tiempo_total += tiempo
            for otra_prenda in diccionario_a_iterar:
                if otra_prenda != prenda and otra_prenda not in excluidos_lavado and otra_prenda not in lavadas:
                    #print(f"Lavado compatible con prenda {otra_prenda}")
                    grupo_lavado.append(otra_prenda)
                    excluidos_lavado = excluidos_lavado.union(restricciones[otra_prenda])
                    lavadas.add(otra_prenda)
                    solucion.write(f"{otra_prenda} {numero_lavado}\n")
            tiempo_max = 0
            for miembro in grupo_lavado:
                if tiempos[miembro] > tiempo_max:
                    tiempo_max = tiempos[miembro]
            tiempo_total += tiempo_max
    solucion.close()

    return tiempo_total, numero_lavado

def obtener_scores(restricciones, tiempos, constante):
    scores = {}
    for prenda in restricciones:
        suma_tiempos_incompatibles = 0
        incompatibles = restricciones[prenda]
        for incompatible in incompatibles:
            suma_tiempos_incompatibles += tiempos[incompatible]
        scores[prenda] = tiempos[prenda] - (suma_tiempos_incompatibles * constante)
    scores = dict(sorted(scores.items(), key = lambda item: -item[1]))
    return scores

def main():
    cantidad_prendas, cantidad_incompatibilidades, restricciones, tiempos = obtener_datos()
    print(f"Prendas: {cantidad_prendas}. Incompatibilidades: {cantidad_incompatibilidades}")
    tiempo_total_1, cantidad_lavados = lavar_prendas(restricciones, tiempos, tiempos)
    print(f"Metodo 1 \nTiempo total consumido: {tiempo_total_1}. Lavados realizados: {cantidad_lavados}")
    tiempo_total_2, cantidad_lavados = lavar_prendas(restricciones, tiempos, restricciones)
    print(f"Metodo 2 \nTiempo total consumido: {tiempo_total_2}. Lavados realizados: {cantidad_lavados}")
    scores = obtener_scores(restricciones, tiempos, 0.001)
    tiempo_total_3, cantidad_lavados = lavar_prendas(restricciones, tiempos, scores)
    print(f"Metodo 3 \nTiempo total consumido: {tiempo_total_3}. Lavados realizados: {cantidad_lavados}")
    if (tiempo_total_1 < tiempo_total_2): #Vuelvo a correr el mejor metodo para que quede en el archivo de la solucion
        lavar_prendas(restricciones, tiempos, tiempos)
    else:
        lavar_prendas(restricciones, tiempos, restricciones)
    




if __name__ == '__main__':
    main()