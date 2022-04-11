import math

import pygame
from pygame.draw import *


screen = pygame.display.set_mode((400, 400))
def funcT(f=50):

    T = 1 / f
    return T


def maxfloat(x = 20):
    y = x * 2 ** (1/2)
    return y


def algform():
    #print(maxfloat(50)) + 'e ** (j*' + input('введите значение') + ')'
    s = '%s * e ** (j * %s )' % (maxfloat(50), 30)
    print(s)


def grafik(bool=1, f = 50, t = 0): #bool 
    i = -1
    start = [0, 0]
    konec = [0, 0]
    line(screen,  (0, 0, 255), (0, 200), (400, 200))
    while i < 5:
        w = 2 * math.pi * f
        if bool == 1:
            kordinati_Y = maxfloat() * math.sin(w * t + (math.pi * (i / 2)))
        else:
            kordinati_Y = Izc(maxfloat(), Zc()) * math.sin(w * t + (math.pi * (i / 2)))
        print(math.sin(math.pi * (i / 2)))
        print(kordinati_Y)
        konec = i / 4 * 200, 0 - kordinati_Y
        line(screen,  (0, 0, 255), (start[0], start[1]+200), (konec[0],konec[1]+200))
        start = konec
        i += 0.25
        
    return kordinati_Y


def Zc(c = 15900 * 10 ** -6, f = 50):
    w = 2 * math.pi * f
    Xc = 1 / (w * c)
    s = '%s * j' % Xc
    print(s)
    return Xc


def Zl(l = 64 * 10 ** -3, f = 50):
    w = 2 * math.pi * f
    Xl = w * l
    s = '%s * j' % Xl
    print(s)
    return Xl


def Izc(u, z):
    i = u / z #максмальное значение тока
    return i
#Izc(maxfloat(), Zc())
    

def Izc(u, z):
    i = u / z
    return i #максмальное значение тока
#Izc(maxfloat(), Zl())
    


pygame.init()
FPS = 30
grafik(int(0))
grafik(int(1))
#  grafik(int(input('Введите какой график рисовать ')))
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
