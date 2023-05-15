import pygame
from network import Network
from Player import Player

width = 1200
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
chatLogMain = []

def redrawWindow(win,players):
    win.fill((255,255,255))
    for player in players:
        player.draw(win)
        player.drawName(win)
            
    players[0].drawChat(win, chatLogMain)
    pygame.display.update()

def CreateChat(players):
    for player in players:
        if len(player.chatLog) > 0:
            chatLogMain.append(player.chatLog[0])
    return players

def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()
    players = []
    print('Enter a username')
    p.name = input()

    while run:
        clock.tick(60)
        players = n.send(p)
        p.chatLog = []
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move(events)
        players = CreateChat(players)
        redrawWindow(win, players)

main()