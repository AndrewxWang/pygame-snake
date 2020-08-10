import pygame
import time
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")

x = 240
y = 240
width = 20
height = 20
vel = 5
x_move = 0
y_move = 0
score = 0
gameover = False
font = pygame.font.SysFont("Arial Black", 17)

def displayScore():
    label = font.render("Score: " + str(score), 1, (255,255,255))
    win.blit(label, (0, 0))
    pygame.display.update()

def drawBorders():
    pygame.draw.rect(win, (255,0,0), (0, 0, 20, 500))
    pygame.draw.rect(win, (255,0,0), (480, 0, 20, 500))
    pygame.draw.rect(win, (255,0,0), (0, 0, 500, 20))
    pygame.draw.rect(win, (255,0,0), (0, 480, 500, 20))
    
def checkDeath():
    global x, y
    if x > 460:
        return True
    elif x < 20:
        return True
    elif y > 460:
        return True
    elif y < 20:
        return True

while not gameover:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_move = -5
                y_move = 0
            elif event.key == pygame.K_RIGHT:
                x_move = 5
                y_move = 0
            elif event.key == pygame.K_UP:
                x_move = 0
                y_move = -5
            elif event.key == pygame.K_DOWN:
                x_move = 0
                y_move = 5
    x+=x_move
    y+=y_move
##    print(x)
##    print(y)
    win.fill((0,0,0))
    gameover = checkDeath()
    drawBorders()
    pygame.draw.rect(win, (255,255,255), (x, y, width, height))
    
    if x_move == 0 and y_move == 0:
        font1 = pygame.font.SysFont("Arial",20)
        label = font1.render("Use the arrow keys to move", 1, (255,255,255))
        win.blit(label, (75, 200))
    displayScore()
    pygame.display.update()

pygame.draw.rect(win, (255,255,0), (x, y, width, height))
font2 = pygame.font.SysFont("Arial Black", 50)
label = font2.render("GAME OVER!", 1, (255,255,255))
win.blit(label, (75, 225))
pygame.display.update()

print("GAME OVER!")
time.sleep(4)
pygame.quit()
