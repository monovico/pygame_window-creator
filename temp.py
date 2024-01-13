import pygame

pygame.init()


#optional
clock = pygame.time.Clock()
fps = 60

#screen size change it to whatever you want
screen_width = 800
screen_height = 800

#name it whatever you want
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('example')


#start the window
run = True
while run:
    
    clock.tick(fps)
    
    #close the window by clicking the x button
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()

pygame.quit()
