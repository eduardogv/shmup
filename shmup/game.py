import pygame
import os
class Game:
    #variables privadas por eso el __ , para evitar magicnumbers
    #estas son variables/atributos de CLASE para todas las instancias
    __hero_image_path = ['shmup', 'assets', 'images', 'hero.png']
    __font_path = ['shmup', 'assets', 'fonts', 'Sansation.ttf']

    __screen_size = (640,480)
    __background_color = (145,96,80)
    __font_foreground_color = (255,255,255)
    __game_caption = "Shrump Game!!"
    __message = "Hello World"
    __font_size = 16
    __message_position = (10, 10)

    def __init__(self):

        pygame.init()
        #definimos las variables de instancia con self. y PRIVADAS con __
        self.__screen = pygame.display.set_mode(Game.__screen_size, 0, 32)
        pygame.display.set_caption(Game.__game_caption)
        # se hace join de la lista con la ruta para que de acuerdo
        # al sistema operativo se usen las barras adecuada con el
        # modulo os. Convert alpha hace que la imagen use el mismo formato
        # de la ventana
        self.__hero_image = pygame.image.load(os.path.join(*Game.__hero_image_path)).convert_alpha()

        font  = pygame.font.Font(os.path.join(*Game.__font_path), Game.__font_size)

        self.__my_text = font.render(Game.__message, True, Game.__font_foreground_color, Game.__background_color)

    def run(self):
        __hero_image_half_width = self.__hero_image.get_width() / 2
        __hero_image_half_height = self.__hero_image.get_height() / 2

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.__screen.fill(Game.__background_color) #borra y actualiza la img de fondo
            x,y = pygame.mouse.get_pos()
            x -= __hero_image_half_width
            y -= __hero_image_half_height
            self.__screen.blit(self.__hero_image, (x,y))
            self.__screen.blit(self.__my_text, Game.__message_position)

            pygame.display.update()

        self.quit()

    def quit(self):
        pygame.quit()
