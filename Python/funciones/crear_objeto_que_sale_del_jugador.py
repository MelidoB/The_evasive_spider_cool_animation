from display.object import Object

def crear_objeto_que_sale_del_jugador(jugador,diccionario,objeto):
    A = jugador.point_a
    B = jugador.point_b

    derecha = jugador.position_value == 0
    izquierda = jugador.position_value == 2
    arriba = jugador.position_value == 3




    if derecha:
        objeto.point_a.x,objeto.point_a.y = (B.x,(objeto.image.get_height()/2)+A.y)
    elif izquierda:
        objeto.point_a.x,objeto.point_a.y = (A.x,(objeto.image.get_height()/2)+A.y)
    elif arriba:
        objeto.point_a.x,objeto.point_a.y = ((objeto.image.get_width()/2)+A.x,A.y)
    else:
        objeto.point_a.x,objeto.point_a.y = ((objeto.image.get_width()/2) +A.x,B.y)

    objeto.set_point_b()

    diccionario['objetos_tirados_del_jugador'].append(objeto)