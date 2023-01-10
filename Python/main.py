from application_files.application import Application
from funciones.objetos_y_characteres import crear_character,crear_objeto

#Instancias

spider = crear_character('spider',(0,200),'spider.png',3,200)
enemy = crear_character('enemy',(200,200),'enemy.png')
pared = crear_objeto('wall',(400,0),'wall.png')

a = Application()

a.items_to_display['jugador'] = [spider]
a.items_to_display['enemigo'] =[enemy]
a.items_to_display['paredes'] = [pared]
a.items_to_display['objetos_tirados_del_jugador'] = []

a.run()

#a.run()


