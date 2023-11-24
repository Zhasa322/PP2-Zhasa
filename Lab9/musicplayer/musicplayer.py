import pygame
import os

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Music Player")
display = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()
FPS = 60

music_list = "musiclist"
music_files = [musicname for musicname in os.listdir(music_list) if musicname.endswith(".mp3")]
current_track = 0

def play():
    pygame.mixer.music.load(os.path.join(music_list, music_files[current_track]))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(music_files)
    stop()
    play()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(music_files)
    stop()
    play()

play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play()
            elif event.key == pygame.K_s:
                stop()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()

    
    instructions = [
        "Press P to Play",
        "Press S to Stop",
        "Press N for Next",
        "Press B for Back"
    ]
    font = pygame.font.Font("arial.ttf", 24)
    for i, text in enumerate(instructions):
        text_render = font.render(text, True, (0, 0, 0))
        pygame.display.get_surface().blit(text_render, (10, 10 + i * 30))
    pygame.display.update()


    pygame.display.flip()
    clock.tick(FPS)