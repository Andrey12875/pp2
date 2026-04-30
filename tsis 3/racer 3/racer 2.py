import pygame
import random

pygame.init()

WIDTH = 400
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Road Game")

clock = pygame.time.Clock()

font_big = pygame.font.SysFont("arial", 50)
font_medium = pygame.font.SysFont("arial", 35)
font_small = pygame.font.SysFont("arial", 28)
font_tiny = pygame.font.SysFont("arial", 22)

LANES = [20, 140, 260]

enemy = pygame.image.load("enemy.png")
enemy = pygame.transform.scale(enemy, (120, 100))
enemy_rect = enemy.get_rect(topleft=(random.choice(LANES), -200))

road1 = pygame.image.load("road.png")
road1 = pygame.transform.scale(road1, (WIDTH, HEIGHT))
road1_rect = road1.get_rect(topleft=(0, 0))

road2 = pygame.image.load("road.png")
road2 = pygame.transform.scale(road2, (WIDTH, HEIGHT))
road2_rect = road2.get_rect(topleft=(0, -HEIGHT))

coin = pygame.image.load("coin.png")
coin = pygame.transform.scale(coin, (30, 30))
coin_rect = coin.get_rect(topleft=(random.choice(LANES), -200))

many_coins = pygame.image.load("many coins.png")
many_coins = pygame.transform.scale(many_coins, (40, 40))
many_coins_rect = many_coins.get_rect(topleft=(random.choice(LANES), -2000))

shield = pygame.image.load("shield.png")
shield = pygame.transform.scale(shield, (45, 45))
shield_rect = shield.get_rect(topleft=(random.choice(LANES), -3500))

coins = pygame.image.load("coins.png")
coins = pygame.transform.scale(coins, (45, 45))
coins_rect = coins.get_rect(topright=(WIDTH - 10, 10))

base_player = pygame.image.load("main.png")
base_player = pygame.transform.scale(base_player, (120, 120))


def make_skin(image, color):
    skin = image.copy()
    overlay = pygame.Surface(skin.get_size(), pygame.SRCALPHA)
    overlay.fill(color)
    skin.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    return skin


player_skins = [
    base_player,
    make_skin(base_player, (180, 220, 255, 255)),
    make_skin(base_player, (255, 180, 180, 255))
]

selected_skin = 0
player = player_skins[selected_skin]
player_rect = player.get_rect(midbottom=(WIDTH // 2, HEIGHT - 30))

play_button = pygame.Rect(100, 240, 200, 55)
leaderboard_button = pygame.Rect(70, 310, 260, 55)
settings_button = pygame.Rect(100, 380, 200, 55)
quit_button = pygame.Rect(100, 450, 200, 55)

easy_button = pygame.Rect(45, 250, 140, 50)
hard_button = pygame.Rect(215, 250, 140, 50)

skin1_button = pygame.Rect(35, 410, 100, 50)
skin2_button = pygame.Rect(150, 410, 100, 50)
skin3_button = pygame.Rect(265, 410, 100, 50)

restart_button = pygame.Rect(100, 370, 200, 55)
menu_button = pygame.Rect(100, 440, 200, 55)
back_button = pygame.Rect(100, 570, 200, 55)

screen_state = "menu"

running = True

score = 0
best_score = 0

distance_ms = 0
best_distance_ms = 0

difficulty = "easy"
speed = 8

shield_active = False


def get_start_speed():
    if difficulty == "easy":
        return 8
    else:
        return 13


def get_shield_bar():
    return pygame.Rect(player_rect.left + 25, player_rect.top - 14, player_rect.width - 50, 7)


def draw_button(rect, text, selected=False):
    if selected:
        color = (160, 220, 160)
    else:
        color = (230, 230, 230)

    pygame.draw.rect(screen, color, rect, border_radius=12)
    pygame.draw.rect(screen, (40, 40, 40), rect, 3, border_radius=12)

    text_surface = font_small.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)


def reset_game():
    global score, speed, distance_ms, shield_active

    score = 0
    distance_ms = 0
    speed = get_start_speed()
    shield_active = False

    player_rect.midbottom = (WIDTH // 2, HEIGHT - 30)

    enemy_rect.topleft = (random.choice(LANES), -200)
    coin_rect.topleft = (random.choice(LANES), -200)
    many_coins_rect.topleft = (random.choice(LANES), -2000)
    shield_rect.topleft = (random.choice(LANES), random.randint(-6000, -2500))

    road1_rect.topleft = (0, 0)
    road2_rect.topleft = (0, -HEIGHT)


def draw_main_menu():
    screen.fill((25, 25, 25))

    title = font_big.render("Road Game", True, (255, 255, 255))
    title_rect = title.get_rect(center=(WIDTH // 2, 150))
    screen.blit(title, title_rect)

    draw_button(play_button, "Play")
    draw_button(leaderboard_button, "Leaderboard")
    draw_button(settings_button, "Settings")
    draw_button(quit_button, "Quit")


def draw_leaderboard():
    screen.fill((25, 25, 25))

    title = font_big.render("Leaderboard", True, (255, 255, 255))
    title_rect = title.get_rect(center=(WIDTH // 2, 150))
    screen.blit(title, title_rect)

    best_score_text = font_small.render(f"Best score: {best_score}", True, (255, 255, 255))
    best_score_rect = best_score_text.get_rect(center=(WIDTH // 2, 280))
    screen.blit(best_score_text, best_score_rect)

    best_distance_text = font_small.render(f"Best distance: {best_distance_ms} ms", True, (255, 255, 255))
    best_distance_rect = best_distance_text.get_rect(center=(WIDTH // 2, 330))
    screen.blit(best_distance_text, best_distance_rect)

    draw_button(back_button, "Back")


def draw_settings():
    screen.fill((25, 25, 25))

    title = font_big.render("Settings", True, (255, 255, 255))
    title_rect = title.get_rect(center=(WIDTH // 2, 110))
    screen.blit(title, title_rect)

    difficulty_text = font_small.render("Difficulty", True, (255, 255, 255))
    difficulty_rect = difficulty_text.get_rect(center=(WIDTH // 2, 210))
    screen.blit(difficulty_text, difficulty_rect)

    draw_button(easy_button, "Easy", difficulty == "easy")
    draw_button(hard_button, "Hard", difficulty == "hard")

    skin_text = font_small.render("Skins", True, (255, 255, 255))
    skin_rect = skin_text.get_rect(center=(WIDTH // 2, 370))
    screen.blit(skin_text, skin_rect)

    draw_button(skin1_button, "Skin 1", selected_skin == 0)
    draw_button(skin2_button, "Skin 2", selected_skin == 1)
    draw_button(skin3_button, "Skin 3", selected_skin == 2)

    draw_button(back_button, "Back")


def update_game():
    global screen_state, score, speed, best_score
    global distance_ms, best_distance_ms, shield_active

    distance_ms += clock.get_time()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_rect.x -= 10

    if keys[pygame.K_RIGHT]:
        player_rect.x += 10

    if player_rect.right >= 420:
        player_rect.right = 420

    if player_rect.left <= -20:
        player_rect.left = -20

    road1_rect.y += speed
    road2_rect.y += speed

    if road1_rect.y >= HEIGHT:
        road1_rect.y = road2_rect.y - HEIGHT

    if road2_rect.y >= HEIGHT:
        road2_rect.y = road1_rect.y - HEIGHT

    enemy_rect.y += speed
    coin_rect.y += speed
    many_coins_rect.y += speed
    shield_rect.y += speed

    if enemy_rect.y > HEIGHT + 50:
        enemy_rect.topleft = (random.choice(LANES), -100)

    if coin_rect.y > HEIGHT + 50:
        coin_rect.topleft = (random.choice(LANES), -100)

    if many_coins_rect.y > HEIGHT + 50:
        many_coins_rect.topleft = (random.choice(LANES), -3000)

    if shield_rect.y > HEIGHT + 50:
        shield_rect.topleft = (random.choice(LANES), random.randint(-6000, -2500))

    if player_rect.colliderect(shield_rect):
        shield_active = True
        shield_rect.topleft = (random.choice(LANES), random.randint(-6000, -2500))

    enemy_hitbox = enemy_rect.inflate(-50, -50)

    if shield_active:
        shield_bar = get_shield_bar()

        if shield_bar.colliderect(enemy_hitbox):
            enemy_rect.topleft = (random.choice(LANES), -100)
            shield_active = False

    if player_rect.colliderect(enemy_hitbox):
        best_score = max(best_score, score)
        best_distance_ms = max(best_distance_ms, distance_ms)
        screen_state = "game_over"

    if player_rect.colliderect(coin_rect):
        score += 1
        speed += 0.1
        coin_rect.topleft = (random.choice(LANES), -700)

    if player_rect.colliderect(many_coins_rect):
        score += 5
        speed += 0.5
        many_coins_rect.topleft = (random.choice(LANES), -3000)


def draw_game():
    screen.fill((250, 250, 250))

    screen.blit(road1, road1_rect)
    screen.blit(road2, road2_rect)

    score_text = font_small.render(str(score), True, (255, 255, 255))
    score_text_rect = score_text.get_rect(midright=(coins_rect.left - 8, coins_rect.centery))

    distance_text = font_tiny.render(f"{distance_ms} ms", True, (255, 255, 255))
    distance_text_rect = distance_text.get_rect(topright=(WIDTH - 10, coins_rect.bottom + 5))

    screen.blit(score_text, score_text_rect)
    screen.blit(coins, coins_rect)
    screen.blit(distance_text, distance_text_rect)

    screen.blit(many_coins, many_coins_rect)
    screen.blit(coin, coin_rect)
    screen.blit(shield, shield_rect)

    screen.blit(player, player_rect)

    if shield_active:
        shield_bar = get_shield_bar()
        pygame.draw.rect(screen, (80, 200, 255), shield_bar)

    screen.blit(enemy, enemy_rect)


def draw_game_over():
    screen.fill((0, 0, 0))

    text = font_big.render("Game Over", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, 210))
    screen.blit(text, text_rect)

    score_text = font_small.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(WIDTH // 2, 280))
    screen.blit(score_text, score_rect)

    distance_text = font_small.render(f"Distance: {distance_ms} ms", True, (255, 255, 255))
    distance_rect = distance_text.get_rect(center=(WIDTH // 2, 320))
    screen.blit(distance_text, distance_rect)

    draw_button(restart_button, "Restart")
    draw_button(menu_button, "Main Menu")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if screen_state == "menu":
                if play_button.collidepoint(mouse_pos):
                    reset_game()
                    screen_state = "game"

                elif leaderboard_button.collidepoint(mouse_pos):
                    screen_state = "leaderboard"

                elif settings_button.collidepoint(mouse_pos):
                    screen_state = "settings"

                elif quit_button.collidepoint(mouse_pos):
                    running = False

            elif screen_state == "settings":
                if easy_button.collidepoint(mouse_pos):
                    difficulty = "easy"

                elif hard_button.collidepoint(mouse_pos):
                    difficulty = "hard"

                elif skin1_button.collidepoint(mouse_pos):
                    selected_skin = 0
                    player = player_skins[selected_skin]

                elif skin2_button.collidepoint(mouse_pos):
                    selected_skin = 1
                    player = player_skins[selected_skin]

                elif skin3_button.collidepoint(mouse_pos):
                    selected_skin = 2
                    player = player_skins[selected_skin]

                elif back_button.collidepoint(mouse_pos):
                    screen_state = "menu"

            elif screen_state == "game_over":
                if restart_button.collidepoint(mouse_pos):
                    reset_game()
                    screen_state = "game"

                elif menu_button.collidepoint(mouse_pos):
                    screen_state = "menu"

            elif screen_state == "leaderboard":
                if back_button.collidepoint(mouse_pos):
                    screen_state = "menu"

    if screen_state == "menu":
        draw_main_menu()

    elif screen_state == "game":
        update_game()
        draw_game()

    elif screen_state == "game_over":
        draw_game_over()

    elif screen_state == "leaderboard":
        draw_leaderboard()

    elif screen_state == "settings":
        draw_settings()

    pygame.display.update()
    clock.tick(60)

pygame.quit()