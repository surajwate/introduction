import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time /= 1000
    score_surface = test_font.render(f"Score: {int(current_time)}", False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0

# Surfaces
game_title = test_font.render("Running Man", False, (64, 64, 64))
game_title_rect = game_title.get_rect(center=(400, 50))

instructions_surface = test_font.render("Press Space to Run", False, (111, 196, 169))
instructions_rect = instructions_surface.get_rect(center=(400, 320))

sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()

# score_surface = test_font.render("My Game", False, (64, 64, 64))
# score_rect = score_surface.get_rect(center=(400, 50))

snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_reactange = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

# Introduction Screen
player_stand = pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rectangle = player_stand.get_rect(center=(400, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:

            if event.type == pygame.MOUSEBUTTONDOWN and player_reactange.bottom >= 300:
                if player_reactange.collidepoint(event.pos):
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_reactange.bottom >= 300:
                    player_gravity = -20

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rectangle.left = 800
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, "#c0e8ec", score_rect)
        # pygame.draw.rect(screen, "#c0e8ec", score_rect, 10)
        # screen.blit(score_surface, score_rect)
        display_score()

        if snail_rectangle.right <= 0:
            snail_rectangle.left = 800
        snail_rectangle.left -= 4
        screen.blit(snail_surface, snail_rectangle)

        player_gravity += 1
        player_reactange.bottom += player_gravity
        if player_reactange.bottom >= 300:
            player_reactange.bottom = 300
        screen.blit(player_surface, player_reactange)

        # Collision
        if player_reactange.colliderect(snail_rectangle):
            game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rectangle)
        screen.blit(game_title, game_title_rect)
        screen.blit(instructions_surface, instructions_rect)

    pygame.display.update()
    clock.tick(60)
