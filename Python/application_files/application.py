import pygame
from application_files.close_game import close_game_function
from funciones.barra_de_salud import crear_barra_de_salud
from funciones.jugador import mover_al_jugador
from funciones.object_collition import determina_si_los_objetos_colicionan,determina_si_los_objetos_estan_dentro
from funciones.crear_objeto_que_sale_del_jugador import crear_objeto_que_sale_del_jugador
from funciones.objetos_y_characteres import crear_character,crear_objeto

class Application:
    def __init__(self):
        self.gameDisplay = None
        self.clock = None
        self.items_to_display = {}


    def run(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((1400, 800))
        self.clock = pygame.time.Clock()
        while True:
            close_game_function()

            self.gameDisplay.fill((0,0,0))

            # Checkear si el jugador y el enemigo estan juntos

            # Checkear si el jugador y el objeto estan juntos

            for paredes in self.items_to_display['paredes']:
                izquierda, derecha, arriba, abajo = determina_si_los_objetos_colicionan(self.items_to_display['jugador'][0],
                                                                                    paredes)


            self.items_to_display['jugador'][0].se_puede_mover_para_izquierda = izquierda
            self.items_to_display['jugador'][0].se_puede_mover_para_derecha = derecha
            self.items_to_display['jugador'][0].se_puede_mover_para_arriba = arriba
            self.items_to_display['jugador'][0].se_puede_mover_para_abajo = abajo



            #determina_si_los_objetos_estan_dentro(self.items_to_display['jugador'][0],self.items_to_display['enemigo'][0])

            # Update all objects
            mover_al_jugador(self.items_to_display['jugador'][0]) # Mover al jugador

            ############SPIDERWEB##############
            if True:
                spiderweb = crear_objeto('spiderweb',(-9999,-9999),'spiderweb.png')
                crear_objeto_que_sale_del_jugador(self.items_to_display['jugador'][0],self.items_to_display,spiderweb)

            if len(self.items_to_display['objetos_tirados_del_jugador']) > 0:
                for i in self.items_to_display['objetos_tirados_del_jugador']:
                    i.point_a.x += 1
                    i.set_point_b()
            ############SPIDERWEB##############

            crear_barra_de_salud(self.items_to_display['jugador'][0], self.items_to_display)
            #Display all objects
            for i in self.items_to_display.values():
                for j in i:

                    self.gameDisplay.blit(j.image, (j.point_a.x, j.point_a.y))

            self.clock.tick(20)
            pygame.display.update()
            #keypress_select_direction(player)
            #randomly_select_direction(enemy)
            #show all instances into application
            #display instances ()
