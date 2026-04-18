import pygame
import random

pygame.init()

WIDTH = 400
HEIGHT = 700
font_big = pygame.font.SysFont("arial", 50)
font_small = pygame.font.SysFont("arial", 30)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Road Game")

clock = pygame.time.Clock()

enemy = pygame.image.load("enemy.png")
enemy = pygame.transform.scale(enemy, (120, 100))
enemy_rect = enemy.get_rect(topleft=(random.choice([20, 140, 260]), -200))
enemy_rect = enemy_rect.inflate(-50, -50)

road1 = pygame.image.load("road.png")
road1 = pygame.transform.scale(road1, (WIDTH, HEIGHT))
road1_rect = road1.get_rect(topleft=(0, 0))

coin = pygame.image.load("coin.png")
coin = pygame.transform.scale(coin, (30, 30))
coin_rect = coin.get_rect(topleft=(random.choice([20, 140, 260]), -200))

road2 = pygame.image.load("road.png")
road2 = pygame.transform.scale(road2, (WIDTH, HEIGHT))
road2_rect = road2.get_rect(topleft=(0, -HEIGHT))

coins = pygame.image.load("coins.png")
coins = pygame.transform.scale(coins, (45, 45))
coins_rect = coins.get_rect(topright=(WIDTH - 10, 10))

player = pygame.image.load("main.png")
player = pygame.transform.scale(player, (120, 120))
player_rect = player.get_rect(midbottom=(WIDTH / 2, HEIGHT - 30))

running = True
restart_button = pygame.Rect(100, 380, 200, 60)
game_over = False
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_over:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    game_over = False

                    player_rect.midbottom = (WIDTH // 2, HEIGHT - 30)

                    enemy_rect.y = -200
                    enemy_rect.x = random.choice([20, 140, 260])
                    score = 0
                    coin_rect.y = -200

                    road1_rect.topleft = (0, 0)
                    road2_rect.topleft = (0, -HEIGHT)
    keys = pygame.key.get_pressed()
    if game_over == False:
        if keys[pygame.K_LEFT]:
            player_rect.x -= 10

        if keys[pygame.K_RIGHT]:
            player_rect.x += 10
        screen.fill((250, 250, 250))
        screen.blit(road1, road1_rect)
        screen.blit(road2, road2_rect)
        road1_rect.y += 10
        road2_rect.y += 10
        if road1_rect.y >= HEIGHT:
            road1_rect.y = road2_rect.y - HEIGHT

        if road2_rect.y >= HEIGHT:
            road2_rect.y = road1_rect.y - HEIGHT

        if player_rect.right >= 420:
            player_rect.right = 420
        if player_rect.left <= -20:
            player_rect.left = -20
        enemy_rect.y += 10
        coin_rect.y += 10
        if enemy_rect.y > 750:
            enemy_rect.y = -100
            enemy_rect.x = random.randrange(30, 370, 30)
        if coin_rect.y > 750:
            coin_rect.y = -100
            coin_rect.x = random.randrange(30, 370, 30)
        if player_rect.colliderect(enemy_rect):
            game_over = True
        if player_rect.colliderect(coin_rect):
            score += 1
            coin_rect.y = -700
        score_text = font_small.render(str(score), True, (255, 255, 255))
        score_text_rect = score_text.get_rect(midright=(coins_rect.left - 8, coins_rect.centery))

        screen.blit(score_text, score_text_rect)
        screen.blit(coins, coins_rect)
        screen.blit(player, player_rect)
        screen.blit(coin, coin_rect)
        screen.blit(enemy, enemy_rect)


    else:
        screen.fill((0, 0, 0))
        text = font_big.render("game over", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH / 2, 250))
        screen.blit(text, text_rect)
        pygame.draw.rect(screen, (230, 230, 230), restart_button)
        restart_text = font_small.render("restart", True, (0, 0, 0))
        restart_text_rect = restart_text.get_rect(center=restart_button.center)
        screen.blit(restart_text, restart_text_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()