import pygame

pygame.init()

W, H = 400, 400
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Moving Ball")

ball_radius = 25
ball_color = (255, 0, 0)
ball_pos = [W, H] 

clock = pygame.time.Clock()
FPS = 30
speed = 20
flLeft = flRight = flup = fldown = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
            elif event.key == pygame.K_UP:
                flup = True
            elif event.key == pygame.K_DOWN:
                fldown = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                flLeft = flRight = flup = fldown = False

    if flup and ball_pos[1] - ball_radius >= 0:
        ball_pos[1] -= speed
    if fldown and ball_pos[1] + ball_radius <= H:
        ball_pos[1] += speed
    if flLeft and ball_pos[0] - ball_radius >= 0:
        ball_pos[0] -= speed
    if flRight and ball_pos[0] + ball_radius <= W:
        ball_pos[0] += speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (ball_pos[0], ball_pos[1]), ball_radius)
    pygame.display.update()
    clock.tick(60)
