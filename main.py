import pygame

pygame.init()

display_width = 400
display_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Tetris", largeText)
        button("GO!", 150, 350, 100, 50, red, black, )
        button("Settings", 150, 450, 100, 50, red, black, )
        TextRect.center = ((display_width / 2), (display_height / 4))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

game_intro()
pygame.quit()
quit()