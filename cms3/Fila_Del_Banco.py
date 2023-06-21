from queue import Queue

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"


def avanzarFila(fila: Queue, min: int):
    contador_minutos: int = 0  # Empieza en 0 y voy agregando minutos
    cliente_en_caja_3: int = -1
    cantidad_clientes: int = fila.qsize()
    while(contador_minutos <= min):
        if(contador_minutos % 4 == 0):  # Llega nuevo cliente
            cantidad_clientes += 1
            fila.put(cantidad_clientes)
        if((contador_minutos % 10 == 1) and not (fila.empty())):  # Caja 1
            fila.get()
        if((contador_minutos % 4 == 3) and not (fila.empty())):  # Caja 2
            fila.get()
        if(contador_minutos % 4 == 2):  # Meto cliente en caja 3
            if(fila.empty()):
                cliente_en_caja_3 = -1
            else:
                cliente_en_caja_3 = fila.get()
        # Agrego al cliente colgado de la caja 3 a la fila
        if (contador_minutos % 4 == 1) and not(cliente_en_caja_3 == -1):
            fila.put(cliente_en_caja_3)
            cliente_en_caja_3 = -1
        contador_minutos += 1
    return fila


if __name__ == '__main__':
    fila: Queue = Queue()
    fila_inicial: int = int(input())
    for numero in range(1, fila_inicial+1):
        fila.put(numero)
    min: int = int(input())
    avanzarFila(fila, min)
    res = []
    for i in range(0, fila.qsize()):
        res.append(fila.get())
    print(res)


# Caja1: Empieza a atender 10:01, y atiende a una persona cada 10 minutos
# Caja2: Empieza a atender 10:03, atiende a una persona cada 4 minutos
# Caja3: Empieza a atender 10:02, y atiende una persona cada 4 minutos, pero no le resuelve el problema y la persona debe volver a la fila (se va al final y tarda 3 min en llegar. Es decir, la persona que fue atendida 10:02 vuelve a entrar a la fila a las 10:05)
# La fila empieza con las n personas que llegaron antes de que abra el banco. Cuando abre (a las 10), cada 4 minutos llega una nueva persona a la fila (la primera entra a las 10:00)
