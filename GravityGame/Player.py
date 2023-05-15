import numpy as np
import pygame
import math

pygame.init()

class Player():
    def __init__(self, x, y, w, l, vx1, vy1, image):
        self.coords = x,y
        self.size = w,l
        self.vx = vx1
        self.vy = vy1
        self.image = image
        self.angle = 0.0

    def rotate(self, image):
        ship_rect = image.get_rect()
        ship_rect.center = (800 // 2, 600 // 2)
        rotated_ship = pygame.transform.rotate(image, self.angle)
        rotated_rect = rotated_ship.get_rect()
        rotated_rect.center = ship_rect.center
        self.coords = rotated_rect[0], rotated_rect[1]
        return rotated_ship


    def takeInputs(self):
        try:
            if self.angle < -360 or self.angle > 360:
                self.angle = 0
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.angle -= 1

            if keys[pygame.K_LEFT]:
                self.angle += 1

            if keys[pygame.K_UP]:
                angle = (self.angle * -1)
                if angle < 0:
                    angle = 360 + angle
                print(angle)
                angle = angle *(3.141592/180)
                self.vy += math.cos(angle) * .05
                self.vx += math.sin(angle) * .05
                #print('Sin ' + str((math.sin(angle) * .2)))
                #print('Cos ' + str((math.cos(angle) * .2)))
            if keys[pygame.K_DOWN]:
                angle = (self.angle * -1)
                if self.angle < 0:
                    angle = 360 - angle
                #print(angle)
                angle = angle *(3.141592/180)
                self.vy += math.cos(angle) * -.05
                self.vx += math.sin(angle) * -.05
        except:
            pass
        

    def move(self, background, planets):
        x = int(background[0] + self.vx * -1)
        y = int(background[1] + self.vy)
        for planet in planets:
            x1 = int(planet.coords[0] + self.vx * -1)
            y1 = int(planet.coords[1] + self.vy)
            planet.coords = (x1,y1)
            print(planet.coords)
        return x,y
       