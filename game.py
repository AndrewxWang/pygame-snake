import pygame
import random
import time
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")

x = 240
y = 240
width = 20
height = 20
vel = 10
x_move = 0
y_move = 0
score = 0
gameover = False
play_again = True
font = pygame.font.SysFont("Arial Black", 17)
randx, randy = round(random.randint(20,460) / 10) * 10, round(random.randint(20,460) / 10) * 10

def drawApple():
    global randx, randy, score
##    print(str(x) + " " + str(y))
##    print(str(randx) + " " + str(randy))
    pygame.draw.rect(win, (255,0,0), (randx, randy, width, height))
    if randx == x and randy == y:
        print("yes")
        randx, randy = round(random.randint(20,460) / 10) * 10, round(random.randint(20,460) / 10) * 10
        score+=1
    
def resetStats():
    global x, y ,x_move, y_move, score, randx, randy
    x = 240
    y = 240
    x_move = 0
    y_move = 0
    score = 0
    randx, randy = round(random.randint(20,460) / 10) * 10, round(random.randint(20,460) / 10) * 10

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
    if x > 460 or y > 460:
        return True
    elif x < 20 or y < 20:
        return True

while play_again:
    if not gameover:
        pygame.time.delay(40)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -vel
                    y_move = 0
                elif event.key == pygame.K_RIGHT:
                    x_move = vel
                    y_move = 0
                elif event.key == pygame.K_UP:
                    x_move = 0
                    y_move = -vel
                elif event.key == pygame.K_DOWN:
                    x_move = 0
                    y_move = vel
        x+=x_move
        y+=y_move
        win.fill((0,0,0))
        gameover = checkDeath()
        drawBorders()
        pygame.draw.rect(win, (255,255,255), (x, y, width, height))
        drawApple()
        if x_move == 0 and y_move == 0:
            label = font.render("Use the arrow keys to move", 1, (255,255,255))
            win.blit(label, (125, 200))
        displayScore()
        pygame.display.update()
    else:
        pygame.time.delay(30)
        
        pygame.draw.rect(win, (255,255,0), (x, y, width, height))
        font2 = pygame.font.SysFont("Arial Black", 50)
        label = font2.render("GAME OVER!", 1, (255,255,255))
        label2 = font.render("Press R to restart or X to exit", 1,  (255,255,255))
        win.blit(label, (75, 200))
        win.blit(label2, (75,275))
        pygame.display.update()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    resetStats()
                    gameover = False
                elif event.key == pygame.K_x:
                    play_again = False    
pygame.quit()
