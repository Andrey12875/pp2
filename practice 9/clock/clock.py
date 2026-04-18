import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()
running = True

image = pygame.image.load(r"C:\Users\User\PycharmProjects\pythonProject5\clock.png").convert_alpha()
image = pygame.transform.scale(image, (860, 660))
image_rect = image.get_rect(center=(400, 300))

cx, cy = image_rect.center

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.now()

    secs = now.second + now.microsecond / 1000000
    mins = now.minute + secs / 60
    hours = (now.hour % 12) + mins / 60

    second_end = pygame.Vector2(0, -210).rotate(secs * 6) + (cx, cy)
    minute_end = pygame.Vector2(0, -170).rotate(mins * 6) + (cx, cy)
    hour_end = pygame.Vector2(0, -120).rotate(hours * 30) + (cx, cy)

    screen.fill((255, 255, 255))
    screen.blit(image, image_rect)

    pygame.draw.line(screen, (0, 0, 0), (cx, cy), second_end, 2)
    pygame.draw.line(screen, (0, 0, 0), (cx, cy), minute_end, 6)
    pygame.draw.line(screen, (0, 0, 0), (cx, cy), hour_end, 10)
    pygame.draw.circle(screen, (0, 0, 0), (cx, cy), 8)

    pygame.display.update()
    clock.tick(60)

pygame.quit()