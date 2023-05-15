import pygame
import numpy as np 
import Player
import planet

pygame.init()

window = pygame.display.set_mode((800, 600))
black = (0,0,0)
white = (255,255,255)
clock = pygame.time.Clock()
player = Player.Player(25, 25, 30, 30, 0, 0, 'Ship.png')
#planet.planet(100, 100, (500,500), 'RedPlanet.png')
planets = [planet.planet(100, 100, (500,500), 'RedPlanet.png')]
b = 'background.png'
#/Users/s1667435/Desktop/Space Game/assets/Ship.png
backC = (0,0)

def loadImages(image, size):
    try:
        image = pygame.image.load('assets/' + image)
    except pygame.error as message:
        print(f"Cannot load image: {image}")
        raise SystemExit(message)
    image = pygame.transform.scale(image, size)
    return image

def drawImage(image, coords, window):
    window.blit(image, coords)

background = loadImages(b, (1920,1080))


Running = True
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
    player.takeInputs()
    window.fill((0,0,0))
    image = loadImages(player.image, (50, 50))
    image = player.rotate(image)
    backC = player.move(backC, planets)
    drawImage(background, backC, window)
    for planet in planets:
        i = loadImages(planet.image, (planet.radius*2, planet.radius*2))
        drawImage(i, (planet.coords[0]-planet.radius, planet.coords[1]-planet.radius), window)
        planet.Gravity(player)
    drawImage(image, player.coords, window)
    player.takeInputs()
    pygame.display.update()
    clock.tick(60)

pygame.quit()