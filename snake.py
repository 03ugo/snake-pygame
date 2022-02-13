import pygame
# Initializes all of the imported Pygame modules
pygame.init() 
# Title of the Window
title = "Snake" 
# Set the screen size
display = pygame.display.set_mode((800, 600)) 
# Set the title
pygame.display.set_caption(title) 

### Colors
blue = (0,0,255)
white = (255, 255, 255) 

# Position of the Snake
x = 300
y = 300
x_update = 0
y_update = 0

# Initialize the class Clock
clock = pygame.time.Clock()

running = False

# Keep the window open
while not running:
    for event in pygame.event.get():
        # Si l'on clique sur la croix pour quitter
        if event.type == pygame.QUIT:
            running = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_update = -10
                y_update = 0
            elif event.key == pygame.K_RIGHT:
                x_update = 10
                y_update = 0
            elif event.key == pygame.K_UP:
                y_update = -10
                x_update = 0
            elif event.key == pygame.K_DOWN:
                y_update = 10
                x_update = 0

    x += x_update
    y += y_update
    display.fill(white)
    pygame.draw.rect(display, blue, [x, y , 10, 10]) # draw the snake (surface, color, position and dimensions)
    pygame.display.update() # update the screen
    clock.tick(30)


pygame.quit() # Used to uninitialize everything
quit()