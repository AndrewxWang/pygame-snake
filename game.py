import pygame
import random
import time
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")
print("Snake Remake by Andrew Wang")
x = 240
y = 240
width = 20
height = 20
vel = 20
x_move = 0
y_move = 0
score = 0
highscore = 0
gameover = False
play_again = True
font = pygame.font.SysFont("Arial Black", 17)
snake = []

def randxy():
    randx, randy = -1, -1
    while randx % 20 != 0: 
        randx = round(random.randint(20,460) / 10) * 10
    while randy % 20 != 0: 
        randy = round(random.randint(20,460) / 10) * 10

    return randx, randy
randx, randy = randxy()

def drawSnake():
    global snake
    for x1 in snake:
        pygame.draw.rect(win, (255,255,255), (x1[0], x1[1], width, height))

def drawApple():
    global randx, randy, score
    pygame.draw.rect(win, (255,0,0), (randx, randy, width, height))
    if randx == x and randy == y:
        randx, randy = randxy()
        score+=1
    
def resetStats():
    global x, y ,x_move, y_move, score, randx, randy, snake
    x = 240
    y = 240
    x_move = 0
    y_move = 0
    score = 0
    randx, randy = randxy()
    snake.clear()

def displayScore():
    label = font.render("Score: " + str(score), 1, (255,255,255))
    win.blit(label, (0, 0))
    label2 = font.render("High Score: " + str(highscore), 1, (255,255,255))
    win.blit(label2, (350, 0))
    
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
        pygame.time.delay(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_move != vel:
                    x_move = -vel
                    y_move = 0
                elif event.key == pygame.K_RIGHT and x_move != -vel:
                    x_move = vel
                    y_move = 0
                elif event.key == pygame.K_UP and y_move != vel:
                    y_move = -vel
                    x_move = 0

                elif event.key == pygame.K_DOWN and y_move != -vel:
                    y_move = vel
                    x_move = 0
                elif event.key == pygame.K_r:
                    resetStats()
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
            
        if score > highscore:
            highscore = score
        displayScore()

        snakeLen = []
        snakeLen.append(x)
        snakeLen.append(y)
        snake.append(snakeLen)

        if len(snake) > score+1:
            del snake[0]

        for x1 in snake[:-1]:
            if x1 == snakeLen:
                gameover = True
        drawSnake()
        
        pygame.display.update()
    else:
        pygame.draw.rect(win, (255,255,0), (x, y, width, height))
        pygame.time.delay(30)
        font2 = pygame.font.SysFont("Arial Black", 50)
        label = font2.render("GAME OVER!", 1, (255,255,255))
        label2 = font.render("Press R to restart or X to exit", 1,  (255,255,255))
        label_1 = font2.render("GAME OVER!", 1, (0,0,0))
        label_2 = font.render("Press R to restart or X to exit", 1,  (0,0,0))
        win.blit(label_1, (76,201))
        win.blit(label_2, (76,276))
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
print("Thanks for playing!")
time.sleep(2)

pygame.quit()
