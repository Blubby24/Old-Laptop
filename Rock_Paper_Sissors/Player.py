import pygame

class Player():
    def __init__(self, x, y, width, height, color, number, name):
        pygame.init()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        self.name = name
        self.number = number
        self.chatLog = []
        self.is_typing = False
        self.message = ''
        self.t_pressed = False


    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def drawName(self, win):
        pygame.font.init()
        font = pygame.font.SysFont(None, 24)
        black = (0,0,0)
        img = font.render(self.name, True, black)
        win.blit(img, (self.x, self.y-30))


    def BruteForceTheAPI(self, key):
        k = str(key)
        output = ''
        reading = False
        for c in range(len(k)):
            check = k[c]
            if reading == True:
                c += 2
                while not k[c] == "'":
                    if k[c] + k[c+1] == r'\r':
                        output = 'Enter'
                        break
                    output += k[c]
                    c += 1
                break
            if check == ":":
                reading = not reading
            

        return output

    def typing(self, keys):
        for key in keys:
            if key.type == pygame.KEYDOWN:
                print(str(key))
                k = self.BruteForceTheAPI(key)
                if k == r'\x08':
                    k = 'Backspace'
                if k and not k == 'Backspace' and not k == 'Enter':
                    print('The added key is ' + str(k))
                    self.message += k
                if k == 'Backspace':
                    self.message = self.message[:-1]
                if k == 'Enter':
                    print('Enter pressed')
                    self.message = self.message[1:]
                    self.is_typing = False
                    return self.message
        return None
    def move(self, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_t]:
            if self.t_pressed == False:
                self.t_pressed = True
                #print('t pressed = ' + str(self.t_pressed))
                #print(self.is_typing)
                self.is_typing =  True
        else:
            self.t_pressed = False

        if self.is_typing == False:
            if keys[pygame.K_LEFT]:
                self.x -= self.vel

            if keys[pygame.K_RIGHT]:
                self.x += self.vel

            if keys[pygame.K_UP]:
                self.y -= self.vel

            if keys[pygame.K_DOWN]:
                self.y += self.vel

        if self.is_typing == True:
            message = self.typing(events)
            if message:
                print('message exists')
                final = self.name + ': ' + message
                self.chatLog.append(final)
                self.message = ''

        self.update()

    def drawChat(self, win, chatLog):
        pygame.font.init()
        #print(chatLog)
        font = pygame.font.SysFont(None, 24)
        black = (0,0,0)
        CY = 475
        for chat in reversed(chatLog):
            img = font.render(chat, True, black)
            win.blit(img, (400, CY))
            CY -= 25
        typing = self.message[1:]
        img = font.render(typing, True, black)
        win.blit(img, (800, 100))

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)