import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock= pygame.time.Clock()
  
test_surface = pygame.Surface((200,100))
test_surface.fill('Red')
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface,(200,200))
    pygame.display.update()
    clock.tick(60)
