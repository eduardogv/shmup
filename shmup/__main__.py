import sys
from shmup.game import Game

def main(args = None):
    if args is None:
        #print(sys.argv[0])
        args = sys.argv[1:] #habitual en cualquier paquete python
    game = Game()
    game.run()
    print ("Hello desde main module 2")

if __name__ == '__main__':
    sys.exit(main())
#me quedo en minuto 08:00 del video modulo 6
