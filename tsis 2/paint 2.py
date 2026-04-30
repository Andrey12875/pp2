import pygame
from datetime import datetime

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

fill_button = pygame.Rect(680, 540, 55, 35)
save_button = pygame.Rect(740, 540, 55, 35)

shape_buttons = []
for i in range(5):
    rect = pygame.Rect(70, 140 + i * 55, 26, 26)
    shape_buttons.append(rect)

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

drawing = False
running = True
last = None

screen.fill((255, 255, 255))

sidebar_rect = pygame.Rect(30, 0, 20, 600)
circle_rect = pygame.Rect(25, 65, 30, 30)
white_circle_rect = pygame.Rect(25, 65, 30, 30)
panel_rect = pygame.Rect(0, 0, 80, 600)
drawing_area_rect = pygame.Rect(80, 0, 720, 540)

moving_circle = False
current_color = colors[0]

current_shape = "circle"
shape_start = None

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_color = False
            clicked_shape = False
            clicked_fill = False
            clicked_save = False

            for i in range(len(color_buttons)):
                if color_buttons[i].collidepoint(event.pos):
                    current_color = colors[i]
                    clicked_color = True

            if shape_buttons[0].collidepoint(event.pos):
                current_shape = "line"
                clicked_shape = True

            if shape_buttons[1].collidepoint(event.pos):
                current_shape = "diamond"
                clicked_shape = True

            if shape_buttons[2].collidepoint(event.pos):
                current_shape = "square"
                clicked_shape = True

            if shape_buttons[3].collidepoint(event.pos):
                current_shape = "right_triangle"
                clicked_shape = True

            if shape_buttons[4].collidepoint(event.pos):
                current_shape = "triangle"
                clicked_shape = True

            if fill_button.collidepoint(event.pos):
                pygame.draw.rect(screen, current_color, drawing_area_rect)
                clicked_fill = True
                drawing = False
                last = None
                shape_start = None
                current_shape = "circle"

            if save_button.collidepoint(event.pos):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"canvas_{timestamp}.png"
                canvas = screen.subsurface(drawing_area_rect).copy()
                pygame.image.save(canvas, filename)

                clicked_save = True
                drawing = False
                last = None
                shape_start = None
                current_shape = "circle"

            if clicked_color == False and clicked_shape == False and clicked_fill == False and clicked_save == False:
                if white_circle_rect.collidepoint(event.pos):
                    moving_circle = True
                else:
                    drawing = True

                    if current_shape != "circle":
                        shape_start = event.pos
                    else:
                        last = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            size = int(circle_rect.width)

            if drawing == True and current_shape == "line":
                pygame.draw.line(
                    screen,
                    current_color,
                    shape_start,
                    event.pos,
                    size
                )

                current_shape = "circle"
                shape_start = None

            if drawing == True and current_shape == "diamond":
                x1, y1 = shape_start
                x2, y2 = event.pos

                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2

                pygame.draw.polygon(
                    screen,
                    current_color,
                    [
                        (center_x, y1),
                        (x2, center_y),
                        (center_x, y2),
                        (x1, center_y)
                    ],
                    size
                )

                current_shape = "circle"
                shape_start = None

            if drawing == True and current_shape == "square":
                x1, y1 = shape_start
                x2, y2 = event.pos

                square_size = min(abs(x2 - x1), abs(y2 - y1))

                if x2 < x1:
                    x1 = x1 - square_size

                if y2 < y1:
                    y1 = y1 - square_size

                pygame.draw.rect(
                    screen,
                    current_color,
                    (x1, y1, square_size, square_size),
                    size
                )

                current_shape = "circle"
                shape_start = None

            if drawing == True and current_shape == "right_triangle":
                x1, y1 = shape_start
                x2, y2 = event.pos

                pygame.draw.polygon(
                    screen,
                    current_color,
                    [
                        (x1, y1),
                        (x1, y2),
                        (x2, y2)
                    ],
                    size
                )

                current_shape = "circle"
                shape_start = None

            if drawing == True and current_shape == "triangle":
                x1, y1 = shape_start
                x2, y2 = event.pos

                triangle_size = min(abs(x2 - x1), abs(y2 - y1))

                if y2 < y1:
                    pygame.draw.polygon(
                        screen,
                        current_color,
                        [
                            (x1, y1),
                            (x1 - triangle_size, y1 + triangle_size),
                            (x1 + triangle_size, y1 + triangle_size)
                        ],
                        size
                    )
                else:
                    pygame.draw.polygon(
                        screen,
                        current_color,
                        [
                            (x1, y1),
                            (x1 - triangle_size, y1 - triangle_size),
                            (x1 + triangle_size, y1 - triangle_size)
                        ],
                        size
                    )

                current_shape = "circle"
                shape_start = None

            drawing = False
            last = None
            moving_circle = False

        if event.type == pygame.MOUSEMOTION:
            if moving_circle:
                x, y = event.pos

                if y <= 600 and y >= 10:
                    circle_rect.center = (40, y)
                    white_circle_rect.center = (40, y)

                if y <= 600 and y >= 20:
                    circle_rect.width = int(y / 10)
                    circle_rect.height = int(y / 10)

            elif drawing and current_shape == "circle":
                current = event.pos
                pygame.draw.circle(
                    screen,
                    current_color,
                    last,
                    int(circle_rect.width)
                )
                last = current

    pygame.draw.rect(screen, (255, 255, 255), panel_rect)
    pygame.draw.rect(screen, (80, 80, 80), sidebar_rect)

    pygame.draw.circle(
        screen,
        (255, 255, 255),
        white_circle_rect.center,
        white_circle_rect.width // 2
    )

    pygame.draw.circle(
        screen,
        (0, 0, 0),
        circle_rect.center,
        circle_rect.width // 2
    )

    for rect in shape_buttons:
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            rect.center,
            rect.width // 2
        )

        pygame.draw.circle(
            screen,
            (0, 0, 0),
            rect.center,
            rect.width // 2,
            2
        )

    pygame.draw.line(
        screen,
        (0, 0, 0),
        (shape_buttons[0].centerx - 7, shape_buttons[0].centery),
        (shape_buttons[0].centerx + 7, shape_buttons[0].centery),
        2
    )

    pygame.draw.polygon(
        screen,
        (0, 0, 0),
        [
            (shape_buttons[1].centerx, shape_buttons[1].centery - 7),
            (shape_buttons[1].centerx + 7, shape_buttons[1].centery),
            (shape_buttons[1].centerx, shape_buttons[1].centery + 7),
            (shape_buttons[1].centerx - 7, shape_buttons[1].centery)
        ],
        2
    )

    pygame.draw.rect(
        screen,
        (0, 0, 0),
        (
            shape_buttons[2].centerx - 6,
            shape_buttons[2].centery - 6,
            12,
            12
        ),
        2
    )

    pygame.draw.polygon(
        screen,
        (0, 0, 0),
        [
            (shape_buttons[3].centerx - 6, shape_buttons[3].centery + 6),
            (shape_buttons[3].centerx - 6, shape_buttons[3].centery - 6),
            (shape_buttons[3].centerx + 6, shape_buttons[3].centery + 6)
        ],
        2
    )

    pygame.draw.polygon(
        screen,
        (0, 0, 0),
        [
            (shape_buttons[4].centerx, shape_buttons[4].centery - 7),
            (shape_buttons[4].centerx - 7, shape_buttons[4].centery + 5),
            (shape_buttons[4].centerx + 7, shape_buttons[4].centery + 5)
        ],
        2
    )

    for i in range(len(color_buttons)):
        pygame.draw.circle(
            screen,
            colors[i],
            color_buttons[i].center,
            color_buttons[i].width // 2
        )

        pygame.draw.circle(
            screen,
            (0, 0, 0),
            color_buttons[i].center,
            color_buttons[i].width // 2,
            2
        )

    pygame.draw.rect(screen, (255, 255, 255), fill_button)
    pygame.draw.rect(screen, (0, 0, 0), fill_button, 2)

    fill_text = pygame.font.SysFont("arial", 22).render(
        "fill",
        True,
        (0, 0, 0)
    )
    fill_text_rect = fill_text.get_rect(center=fill_button.center)
    screen.blit(fill_text, fill_text_rect)

    pygame.draw.rect(screen, (255, 255, 255), save_button)
    pygame.draw.rect(screen, (0, 0, 0), save_button, 2)

    save_text = pygame.font.SysFont("arial", 22).render(
        "save",
        True,
        (0, 0, 0)
    )
    save_text_rect = save_text.get_rect(center=save_button.center)
    screen.blit(save_text, save_text_rect)

    pygame.display.update()
    clock.tick(200)

pygame.quit()