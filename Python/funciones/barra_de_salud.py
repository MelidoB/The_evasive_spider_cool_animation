from funciones.objetos_y_characteres import crear_character,crear_objeto

def crear_barra_de_salud(object,dictionary):

    health_percentage = object.current_health / object.max_health

    if health_percentage < 0.25:
        health_bar_image = 'health_bar_0.png'
        health_bar_adding_image = 'health_bar_adding_0.png'
    elif health_percentage < 0.50:
        health_bar_image = 'health_bar_1.png'
        health_bar_adding_image = 'health_bar_adding_1.png'
    elif health_percentage < 0.75:
        health_bar_image = 'health_bar_2.png'
        health_bar_adding_image = 'health_bar_adding_2.png'
    else:
        health_bar_image = 'health_bar_3.png'
        health_bar_adding_image = 'health_bar_adding_3.png'

    health_bar = crear_objeto('health_bar', (1050, 55), health_bar_image)
    dictionary['health_bar'] = [health_bar]


    health_bar_chunks = []

    x_initial = health_bar.point_a.x + health_bar.image.get_width() / 4.68
    y_initial = health_bar.point_a.y + health_bar.image.get_height() / 3
    x = x_initial


    for n in range(round((120*object.current_health)/object.max_health)):  # 17 is full # player health needs to be use hear
        health_bar = crear_objeto('health_bar_adding', (x, y_initial), health_bar_adding_image)
        health_bar_chunks.append(health_bar)
        x += health_bar.image.get_width()


    dictionary['health_bar_chunks'] = health_bar_chunks