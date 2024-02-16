import pygame
from sys import exit

pygame.init()
screen =pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock=pygame.time.Clock()
test_font=pygame.font.Font('font/Pixeltype.ttf',50)

sky_surface =pygame.image.load('SM_background_Sky.png')
ground_surface=pygame.image.load('SM_background.png')
text_surface=test_font.render('test game',False,'Blue')

char_1=pygame.image.load('SuperMario Char.jpeg')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.Quit:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))