import pygame

pygame.init()
colors = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 150, 0),
    (120, 60, 200),
    (255, 255, 255)
]
color_buttons = []
for i in range(10):
    rect = pygame.Rect(100 + i * 60, 540, 35, 35)
    color_buttons.append(rect)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
drawing = False
running = True
last = None
screen.fill((255, 255, 255))
sidebar_rect = pygame.Rect(30, 00, 20, 600)

circle_rect = pygame.Rect(25, 65, 30, 30)
white_circle_rect = pygame.Rect(25, 65, 30, 30)
panel_rect = pygame.Rect(0, 0, 80, 600)
moving_circle = False
circle_radius = circle_rect.width
current_color = colors[0]
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_color = False

            for i in range(len(color_buttons)):
                if color_buttons[i].collidepoint(event.pos):
                    current_color = colors[i]
                    clicked_color = True

            if clicked_color == False:
                if white_circle_rect.collidepoint(event.pos):
                    moving_circle = True
                else:
                    drawing = True
                    last = event.pos

        if event.type == pygame.MOUSEBUTTONUP :
            drawing = False
            last = None
            moving_circle = False
        if event.type == pygame.MOUSEMOTION :
            if moving_circle:
                x,y = event.pos
                circle_rect.center = (40, y)
                white_circle_rect.center = (40, y)
                circle_rect.width = y/10
                circle_rect.height = y/10

            elif drawing:
                current = event.pos
                pygame.draw.circle(screen,current_color,current, circle_rect.width)
                last = current
        pygame.draw.rect(screen, (255, 255, 255), panel_rect)
        pygame.draw.rect(screen, (80, 80, 80), sidebar_rect)
        pygame.draw.circle(screen, (255, 255, 255), white_circle_rect.center, white_circle_rect.width // 2)
        pygame.draw.circle(screen,(0, 0, 0),circle_rect.center,circle_rect.width // 2)
        for i in range(len(color_buttons)):
            pygame.draw.circle(screen,colors[i],color_buttons[i].center,color_buttons[i].width // 2)
            for i in range(len(color_buttons)):
                pygame.draw.circle(screen, colors[i], color_buttons[i].center, color_buttons[i].width // 2)
                pygame.draw.circle(screen, (0, 0, 0), color_buttons[i].center, color_buttons[i].width // 2, 2)

    pygame.display.update()
    clock.tick(200)
pygame.quit()