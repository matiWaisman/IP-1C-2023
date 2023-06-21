from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json

# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"


def procesamiento_pedidos(pedidos: Queue, stock_productos: Dict[str, int], precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    res: List[Dict[str, Union[int, str, float, Dict[str, int]]]] = []
    while not pedidos.empty():
        pedido_actual = armar_pedido(
            pedidos.get(), stock_productos, precios_productos)
        res.append(pedido_actual)
    return res


def armar_pedido(pedido: Dict[str, Union[int, str, Dict[str, int]]], stock_productos: Dict[str, int], precios_productos: Dict[str, float]) -> Dict[str, Union[int, str, float, Dict[str, int]]]:
    res: Dict[str, Union[int, str, float, Dict[str, int]]] = {}
    res['id'] = pedido['id']
    res['cliente'] = pedido['cliente']
    res['productos'] = calcular_productos(
        pedido['productos'], stock_productos)
    res['precio_total'] = calcular_precio(res['productos'], precios_productos)
    if res['productos'] == pedido['productos']:
        res['estado'] = "completo"
    else:
        res['estado'] = "incompleto"
    return res


def calcular_productos(productos_esperados: Dict[str, int], stock: Dict[str, int]) -> Dict[str, int]:
    res: Dict[str, int] = {}
    for clave in productos_esperados:
        cantidad_posible: int = calcular_cantidad_disponible(
            stock[clave], productos_esperados[clave])
        res[clave] = cantidad_posible
        stock[clave] = stock[clave] - cantidad_posible
    return res


def calcular_cantidad_disponible(stock: int, cantidad_cliente: int) -> int:
    if cantidad_cliente <= stock:
        return cantidad_cliente
    else:
        return stock


def calcular_precio(productos: Dict[str, int], precios: Dict[str, float]) -> float:
    res: float = 0
    for clave in productos:
        res += productos[clave] * precios[clave]
    return res


if __name__ == '__main__':
    pedidos: Queue = Queue()
    list_pedidos = json.loads(input())
    [pedidos.put(p) for p in list_pedidos]
    stock_productos = json.loads(input())
    precios_productos = json.loads(input())
    print("{} {}".format(procesamiento_pedidos(
        pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}
