import pygame
import math
#initialise game
WIDTH, HEIGHT= 700,500

pygame.init()
#very important bracket inside bracket
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pong")

def main():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run=False
                break
        
    pygame.quit()





if __name__== '__main__':
    main()