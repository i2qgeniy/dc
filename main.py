import math

import pygame
from pygame.draw import *
a=50

def funcT(f=50):

    T = 1 / f
    return T


def maxfloat(x=20):
    y = x * 2 ** (1/2)
    return y

def algform():
    #print(maxfloat(50)) + 'e ** (j*' + input('введите значение') + ')'
    s = '%s * e ** (j * %s )' % (maxfloat(50), 30)
    print(s)
i = -1
start = [0, 0]
konec = [0, 0]
def grafik(i, start, konec, f=50):
    line(screen,  (0, 0, 255), (0, 200), (400, 200))
    while i < 5:
        w = 2 * math.pi * f
        t = (1/50) * i / 4
        #fi = i / 2 * math.pi
        fi = 0
        #kordinati_Y = maxfloat() * math.sin(w * t + fi)
        kordinati_Y = maxfloat() * math.sin(math.pi * (i / 2))
        print(math.sin(math.pi * (i / 2)))
        print(kordinati_Y)
        konec = i / 4 * 200, 0 - kordinati_Y
        line(screen,  (0, 0, 255), (start[0], start[1]+200), (konec[0],konec[1]+200))
        start = konec
        i += 0.25
    return kordinati_Y

    
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
grafik(i, start, konec)
'''new diff today2222'''





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
