import math
import pygame

pygame.init()

class planet:
    def __init__(self, mass, radius, coords, image):
        self.mass = mass
        self.radius = radius
        self.coords = coords
        self.image = image
    
    def Gravity(self, player):
        try:
            # a = Gm/r^2
            G = 15
            xdis = player.coords[0]-self.coords[0]
            ydis = self.coords[1] - player.coords[1]
            r = math.sqrt((xdis*xdis)+(ydis*ydis))
            a = -1* (self.mass*G)/(r*r)
            #print(a)
            #now I need the angle of the player to the planet
            angle = math.atan(ydis/xdis)
            if r <= self.radius:
                a = 0
            vx = math.sin(angle)*a
            vy = math.cos(angle)*a
            player.vx += vx
            player.vy += vy
            #print('vx is ' + str(vx))
            #print('vy is ' + str(vy))

        except:
            print('Gravity Failed')

