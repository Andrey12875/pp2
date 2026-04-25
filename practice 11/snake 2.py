import pygame
import random
clock = pygame.time.Clock()
pygame.init()


class segment:
    def __init__(self, x, y, size, direction):
        self.rect = pygame.Rect(x, y, size, size)
        self.direction = direction


    def move(self):
        if self.direction == "left":
            self.rect.x -= 3
        elif self.direction == "right":
            self.rect.x += 3
        elif self.direction == "up":
            self.rect.y -= 3
        elif self.direction == "down":
            self.rect.y += 3
class Snake:
    def __init__(self):
        self.segments = [segment(0, 0, 30, "right")]
        self.turns = []

    def death_check(self):
        head_rect = self.head().rect

        for seg in self.segments[2:]:
            if head_rect.colliderect(seg.rect):
                return True
        if head_rect.left < 0 or head_rect.right > 800 or head_rect.top < 0 or head_rect.bottom > 600:
            return True

        return False
    def head(self):
        return self.segments[0]
    def turn_check(self):
        for i in self.segments[1:]:
            for a in self.turns:
                if (i.rect.x, i.rect.y) == a[0]:
                    i.direction = a[1]
                    if i == self.segments[-1]:
                        self.turns.remove(a)
    def turn(self, new_direction):
        x = self.head().rect.x
        y = self.head().rect.y
        self.head().direction = new_direction
        self.turns.append(((x, y), new_direction))

    def add_segment(self):
        last = self.segments[-1]

        if last.direction == "left":
            new_x = last.rect.x + 30
            new_y = last.rect.y
        elif last.direction == "right":
            new_x = last.rect.x - 30
            new_y = last.rect.y
        elif last.direction == "up":
            new_x = last.rect.x
            new_y = last.rect.y + 30
        elif last.direction == "down":
            new_x = last.rect.x
            new_y = last.rect.y - 30

        self.segments.append(segment(new_x, new_y, 30, last.direction))


snake = Snake()
running = True
screen = pygame.display.set_mode((800,600))
font = pygame.font.Font(None, 50)
restart_rect = pygame.Rect(300, 250, 200, 60)
apple_rect = pygame.Rect(random.randrange(0, 800, 30),random.randrange(0, 600, 30),30,30)
yellow_apple_rect = pygame.Rect(random.randrange(0, 770, 30),random.randrange(0, 600, 30),30,30)
active = True
yellow_apple_time = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if active == False and restart_rect.collidepoint(event.pos):
                snake = Snake()
                apple_rect = pygame.Rect(random.randrange(0, 800, 30),
                                         random.randrange(0, 600, 30),30, 30)
                active = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.head().direction != "right":
                snake.turn("left")

            if event.key == pygame.K_RIGHT and snake.head().direction != "left":
                snake.turn("right")

            if event.key == pygame.K_UP and snake.head().direction != "down":
                snake.turn("up")

            if event.key == pygame.K_DOWN and snake.head().direction != "up":
                snake.turn("down")
    if active == True:
        screen.fill((170, 220, 170))

        for x in range(0, 800, 30):
            pygame.draw.line(screen, (100, 170, 120), (x, 0), (x, 600))

        for y in range(0, 600, 30):
            pygame.draw.line(screen, (100, 170, 120), (0, y), (800, y))

        pygame.draw.rect(screen, (0, 200, 200), apple_rect)
        pygame.draw.rect(screen, (255, 230, 0), yellow_apple_rect)
        if snake.head().rect.colliderect(apple_rect):
            apple_rect = pygame.Rect(random.randrange(0, 800, 30),random.randrange(0, 600, 30),30, 30)
            snake.add_segment()
        current_time = pygame.time.get_ticks()

        if current_time - yellow_apple_time >= 5000:
            yellow_apple_rect = pygame.Rect(random.randrange(0, 770, 30),random.randrange(0, 600, 30),30,30)
            yellow_apple_time = current_time
        if snake.head().rect.colliderect(yellow_apple_rect):
            yellow_apple_rect = pygame.Rect(random.randrange(0, 770, 30),random.randrange(0, 600, 30),30,30)
            yellow_apple_time = pygame.time.get_ticks()
            snake.add_segment()
            snake.add_segment()
            snake.add_segment()
        snake.turn_check()
        snake.head().move()
        for i in snake.segments[1:]:
            i.move()
        for i in snake.segments:
            pygame.draw.rect(screen, (200, 50, 50), i.rect)

        death = snake.death_check()
        if death == True:
            active = False

    if active == False:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (200, 200, 200), restart_rect)
        text = font.render("Restart", True, (0, 0, 0))
        screen.blit(text, (340, 265))


    pygame.display.update()
    clock.tick(60)
pygame.quit()