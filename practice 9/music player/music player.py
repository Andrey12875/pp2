import pygame

pygame.init()
pygame.mixer.init()

soundtracks = [
    r"C:\Users\User\PycharmProjects\pythonProject5\soundracks\Carefree(chosic.com).mp3",
    r"C:\Users\User\PycharmProjects\pythonProject5\soundracks\Fluffing-a-Duck(chosic.com).mp3",
    r"C:\Users\User\PycharmProjects\pythonProject5\soundracks\Kevin-MacLeod-Investigations(chosic.com).mp3",
    r"C:\Users\User\PycharmProjects\pythonProject5\soundracks\Monkeys-Spinning-Monkeys(chosic.com).mp3",
    r"C:\Users\User\PycharmProjects\pythonProject5\soundracks\Run-Amok(chosic.com).mp3",
    r"C:\Users\User\PycharmProjects\pythonProject5\soundracks\Sneaky-Snitch(chosic.com).mp3"
]

current_track = 0
playing = False

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
GREEN = (0, 255, 100)

font = pygame.font.SysFont(None, 30)
small_font = pygame.font.SysFont(None, 24)

play_rect = pygame.Rect(250, 520, 100, 40)
next_rect = pygame.Rect(370, 520, 100, 40)
back_rect = pygame.Rect(490, 520, 100, 40)
quit_rect = pygame.Rect(610, 520, 100, 40)

slider_rect = pygame.Rect(250, 480, 460, 12)

track_length = pygame.mixer.Sound(soundtracks[current_track]).get_length()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                if playing == False:
                    pygame.mixer.music.load(soundtracks[current_track])
                    pygame.mixer.music.play()
                    track_length = pygame.mixer.Sound(soundtracks[current_track]).get_length()
                    playing = True
                else:
                    pygame.mixer.music.stop()
                    playing = False

            if next_rect.collidepoint(event.pos):
                current_track += 1
                if current_track >= len(soundtracks):
                    current_track = 0
                pygame.mixer.music.load(soundtracks[current_track])
                pygame.mixer.music.play()
                track_length = pygame.mixer.Sound(soundtracks[current_track]).get_length()
                playing = True

            if back_rect.collidepoint(event.pos):
                current_track -= 1
                if current_track < 0:
                    current_track = len(soundtracks) - 1
                pygame.mixer.music.load(soundtracks[current_track])
                pygame.mixer.music.play()
                track_length = pygame.mixer.Sound(soundtracks[current_track]).get_length()
                playing = True

            if quit_rect.collidepoint(event.pos):
                running = False

    if playing == True and pygame.mixer.music.get_busy() == False:
        playing = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (0, 0, 200, HEIGHT), border_radius=20)

    pygame.draw.rect(screen, BLACK, play_rect, border_radius=10)
    pygame.draw.rect(screen, BLACK, next_rect, border_radius=10)
    pygame.draw.rect(screen, BLACK, back_rect, border_radius=10)
    pygame.draw.rect(screen, BLACK, quit_rect, border_radius=10)

    pygame.draw.rect(screen, GRAY, slider_rect, border_radius=6)

    if playing == True:
        current_time = pygame.mixer.music.get_pos() / 1000
        if current_time < 0:
            current_time = 0
    else:
        current_time = 0

    progress_width = 0
    if track_length > 0:
        progress_width = int((current_time / track_length) * slider_rect.width)

    if progress_width > slider_rect.width:
        progress_width = slider_rect.width

    pygame.draw.rect(screen, BLACK, (slider_rect.x, slider_rect.y, progress_width, slider_rect.height), border_radius=6)

    if playing == True:
        play_text = font.render("Stop", True, WHITE)
    else:
        play_text = font.render("Play", True, WHITE)

    next_text = font.render("Next", True, WHITE)
    back_text = font.render("Back", True, WHITE)
    quit_text = font.render("Quit", True, WHITE)

    screen.blit(play_text, play_text.get_rect(center=play_rect.center))
    screen.blit(next_text, next_text.get_rect(center=next_rect.center))
    screen.blit(back_text, back_text.get_rect(center=back_rect.center))
    screen.blit(quit_text, quit_text.get_rect(center=quit_rect.center))

    title_text = small_font.render("Songs", True, WHITE)
    screen.blit(title_text, (20, 20))

    if playing == True and current_track == 0:
        color0 = GREEN
    else:
        color0 = WHITE

    if playing == True and current_track == 1:
        color1 = GREEN
    else:
        color1 = WHITE

    if playing == True and current_track == 2:
        color2 = GREEN
    else:
        color2 = WHITE

    if playing == True and current_track == 3:
        color3 = GREEN
    else:
        color3 = WHITE

    if playing == True and current_track == 4:
        color4 = GREEN
    else:
        color4 = WHITE

    if playing == True and current_track == 5:
        color5 = GREEN
    else:
        color5 = WHITE

    song0 = small_font.render("Carefree", True, color0)
    song1 = small_font.render("Fluffing a Duck", True, color1)
    song2 = small_font.render("Investigations", True, color2)
    song3 = small_font.render("Spinning Monkeys", True, color3)
    song4 = small_font.render("Run Amok", True, color4)
    song5 = small_font.render("Sneaky Snitch", True, color5)

    screen.blit(song0, (20, 70))
    screen.blit(song1, (20, 105))
    screen.blit(song2, (20, 140))
    screen.blit(song3, (20, 175))
    screen.blit(song4, (20, 210))
    screen.blit(song5, (20, 245))

    pygame.display.update()

pygame.quit()