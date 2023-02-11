import pygame

# initialize pygame
pygame.init()

# define screen size
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# define initial ball position
x = 350
y = 250

# define ball speed
speed = 5

# define ball size
ball_size = 20

# start the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= speed
            if event.key == pygame.K_DOWN:
                y += speed
            if event.key == pygame.K_LEFT:
                x -= speed
            if event.key == pygame.K_RIGHT:
                x += speed

    # clear the screen to white
    screen.fill(white)

    # draw the red ball
    pygame.draw.circle(screen, red, (x, y), ball_size)

    # update the screen
    pygame.display.update()

# quit pygame
pygame.quit()
