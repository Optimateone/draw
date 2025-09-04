import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

pygame.draw.line(screen, (0, 0, 0), (100, 380), (540, 380)) # Draw a black line

# Draw the ground
pygame.draw.line(screen, (102,0,0),(0,380),(640,380),5)
# Draw the bottom of the house
pygame.draw.line(screen, (0,0,204),(200,375),(400,375),3)
# Draw two walls
pygame.draw.line(screen, (0,0,204),(200,200),(200,375),3)
pygame.draw.line(screen, (0,0,204),(400,200),(400,375),3)
# Draw the roof
pygame.draw.polygon(screen, (200,0,0),[(200,200),(400,200),(300,100)],3)
# Draw a door
pygame.draw.rect(screen, (153,76,0),(275,300,50,75),1)
# Draw two windows
pygame.draw.circle(screen, (0,204,204),(250,250),25,1)
pygame.draw.circle(screen, (0,204,204),(350,250),25,1)
# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears