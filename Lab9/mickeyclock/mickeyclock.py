import pygame
pygame.init()

icon = pygame.image.load("mickeyclock.jpeg")
minutes = pygame.image.load("right-hand.png")
seconds = pygame.image.load("left-hand.png")
background = pygame.image.load("main-clock.png")

sc = pygame.display.set_mode((829, 836), pygame.RESIZABLE)
pygame.display.set_caption("Mickey clock")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 60
anglemin = 0
anglesec = 0
center = (414, 418)

def rotmin(minutes, anglemin, x, y):
    rotated_min = pygame.transform.rotate(minutes, anglemin)
    new_rect = rotated_min.get_rect(center=minutes.get_rect(center=(x, y)).center)
    return rotated_min, new_rect

def rotsec(seconds, anglesec, x, y):
    rotated_sec = pygame.transform.rotate(seconds, anglesec)
    new_rect = rotated_sec.get_rect(center=seconds.get_rect(center=(x, y)).center)
    return rotated_sec, new_rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    anglemin -= 0.1/60
    anglesec -= 0.1

    sc.blit(background, (0, 0))

    rotated_min, min_rect = rotmin(minutes, anglemin, 414, 418)
    sc.blit(rotated_min, min_rect.topleft)

    rotated_sec, sec_rect = rotsec(seconds, anglesec, 414, 418)
    sc.blit(rotated_sec, sec_rect.topleft)

    pygame.display.flip()
    clock.tick(FPS)
