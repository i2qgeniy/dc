import pygame
from pygame.draw import *
a=50

def funcT(f=50):

    T = 1 / f
    return T


def maxfloat(x=20):
    y = x * 2 ** (1/2)
    return y


pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

'''new diff today2222'''
line(screen,  (0, 0, 255), (0, 200), (funcT() * (50/4) * 200, maxfloat()))
#ine(screen,  (0, 0, 255), (funcT() * (50/4) * 150, maxfloat()), (funcT() * (50/4) * 200 * 2, ))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()



#print(maxfloat(float(input('введите значение '))))
