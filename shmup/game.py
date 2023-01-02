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
        self.__hero_image_half_width = self.__hero_image.get_width() / 2
        self.__hero_image_half_height = self.__hero_image.get_height() / 2
        self.__running = False #Por buenas prácticas se inicializa en el contructor
        self.__is_moving_left = False
        self.__is_moving_right = False
        self.__is_moving_up = False
        self.__is_moving_down = False
        # defino la posicion, es lo mismoq ue poner un simple (x,y)
        self.__hero_position = pygame.math.Vector2(self.__screen.get_width()/2 - self.__hero_image_half_width, self.__screen.get_height()/2  - self.__hero_image_half_height)
        self.__hero_speed = 0.1

    def run(self):
        self.__running = True
        while self.__running:
            self.__process_events()
            self.__update()
            self.__render()
        self.__quit()

    def __process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            if event.type == pygame.KEYDOWN:
                self.__handle_player_input(event.key, True)
            if event.type == pygame.KEYUP:
                self.__handle_player_input(event.key, False)

    def __handle_player_input(self, key, is_pressed):
        if key == pygame.K_LEFT:
            self.__is_moving_left = is_pressed
        if key == pygame.K_RIGHT:
            self.__is_moving_right = is_pressed
        if key == pygame.K_UP:
            self.__is_moving_up = is_pressed
        if key == pygame.K_DOWN:
            self.__is_moving_down = is_pressed

    def __update(self):
        movement = pygame.math.Vector2(0.0, 0.0)
        if self.__is_moving_left:
            movement.x -= self.__hero_speed
        if self.__is_moving_right:
            movement.x += self.__hero_speed
        if self.__is_moving_down:
            movement.y += self.__hero_speed
        if self.__is_moving_up:
            movement.y -= self.__hero_speed
        self.__hero_position += movement

        """x, y = pygame.mouse.get_pos()
        x -= self.__hero_image_half_width
        y -= self.__hero_image_half_height"""

    def __render(self):
        # borra y actualiza la img de fondo
        self.__screen.fill(Game.__background_color)
        self.__screen.blit(self.__hero_image, self.__hero_position.xy)
        self.__screen.blit(self.__my_text, Game.__message_position)
        pygame.display.update()

    def __quit(self):
        pygame.quit()
