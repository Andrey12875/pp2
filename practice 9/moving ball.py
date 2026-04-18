import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ball")

image = pygame.image.load(r"C:\Users\User\PycharmProjects\pythonProject5\venv\img.png")
image = pygame.transform.scale(image, (300, 120))
image_rect = pygame.Rect(250, 290, 300, 120)
ellipse_rect = pygame.Rect(image_rect.x+90, 290, 110, 110)

gravity = 0
jump_force = -15
y_speed = 0
running = True
clock = pygame.time.Clock()
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and image_rect.bottom >= ground.top:
                y_speed = jump_force
                gravity = 1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        image_rect.x += 5
        angle -= 5
    if keys[pygame.K_LEFT]:
        image_rect.x -= 5
        angle += 5

    screen.fill((0, 0, 0))
    image_rect.y += y_speed
    y_speed += gravity
    ellipse_rect = pygame.Rect(image_rect.x + 90, 290, 110, 110)
    ground = pygame.Rect(0, 400, 800, 300)
    pygame.draw.rect(screen, (200, 200, 200), ground)
    wall1 = pygame.Rect(0,0 , 20, 400)
    pygame.draw.rect(screen, (200, 200, 200), wall1)
    wall2 = pygame.Rect(780, 0, 20, 400)
    pygame.draw.rect(screen, (200, 200, 200), wall2)
    if image_rect.bottom > ground.top:
        image_rect.bottom = ground.top +10
        gravity = 0
        y_speed = 0
    if image_rect.right - 100 > wall2.right:
        image_rect.right = 900
    if image_rect.left + 100 < wall1.left:
        image_rect.left = -100



    rotated_image = pygame.transform.rotate(image, angle)
    rotated_rect = rotated_image.get_rect(center=image_rect.center)
    screen.blit(rotated_image, rotated_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()