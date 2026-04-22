import pygame
import random

# Initialize Pygame
pygame.init()

# Create game window
window = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Game")

# Load images
player_img = pygame.image.load('assets/player.png')
enemy_img = pygame.image.load('assets/enemy.png')
background_img = pygame.image.load('assets/background.png')
enemy_bullet_img = pygame.image.load('assets/enemy_bullet.png')

# Player setup
playerx = 170
playery = 500
playerx_change = 0
playery_change = 0
player_speed = 0.3

# Enemy setup
num_enemies = 3  
enemyx = []
enemyy = []
enemyx_change = []
enemy_speed = 0.1

# Enemy bullet setup
enemy_bullet_x = []
enemy_bullet_y = []
enemy_bullet_speed = 0.2


# Initialize enemies and bullets
for i in range(num_enemies):
    enemyx.append(random.randint(0, 336))
    enemyy.append(random.randint(0, 100))
    enemyx_change.append(enemy_speed)

    # Initialize bullet at enemy position
    enemy_bullet_x.append(enemyx[i])
    enemy_bullet_y.append(enemyy[i])

# Draw player
def player(x, y):
    window.blit(player_img, (x, y))

# Draw enemy
def enemy(x, y):
    window.blit(enemy_img, (x, y))

# Draw enemy bullet
def enemy_bullet(x, y):
    window.blit(enemy_bullet_img, (x, y))

# Main game loop
running = True
while running:
    window.blit(background_img, (0, 0))  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -player_speed
            if event.key == pygame.K_RIGHT:
                playerx_change = player_speed
            if event.key == pygame.K_UP:
                playery_change = -player_speed
            if event.key == pygame.K_DOWN:
                playery_change = player_speed

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerx_change = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                playery_change = 0

    # Update player position
    playerx += playerx_change
    playery += playery_change

    # Boundary checking for player
    playerx = max(0, min(playerx, 336))
    playery = max(0, min(playery, 536))

    # Draw player
    player(playerx, playery)

    # Create player's rectangle for collision
    player_rect = player_img.get_rect(topleft=(playerx, playery))

    # Loop through all enemies
    for i in range(num_enemies):
        # Move enemy
        enemyx[i] += enemyx_change[i]

        if enemyx[i] <= 0:
            enemyx[i] = 0
            enemyx_change[i] = enemy_speed
            enemyy[i] += 0
        elif enemyx[i] >= 336:
            enemyx[i] = 336
            enemyx_change[i] = -enemy_speed
            enemyy[i] += 0

        # Respawn enemy if it goes off screen
        if enemyy[i] > 600:
            enemyx[i] = random.randint(0, 336)
            enemyy[i] = random.randint(0, 100)

        # Draw enemy
        enemy(enemyx[i], enemyy[i])

        # Move enemy bullet
        enemy_bullet_y[i] += enemy_bullet_speed

        # Respawn bullet if off screen
        if enemy_bullet_y[i] > 600:
            enemy_bullet_x[i] = enemyx[i] + 16  # Centered under enemy
            enemy_bullet_y[i] = enemyy[i] + 32

        # Draw bullet
        enemy_bullet(enemy_bullet_x[i], enemy_bullet_y[i])

        # Collision detection between bullet and player
        bullet_rect = enemy_bullet_img.get_rect(topleft=(enemy_bullet_x[i], enemy_bullet_y[i]))
        if bullet_rect.colliderect(player_rect):
            print("Player hit by enemy bullet!")
            running = False

        # Collision detection between enemy and player
        enemy_rect = enemy_img.get_rect(topleft=(enemyx[i], enemyy[i]))
        if enemy_rect.colliderect(player_rect):
            print("Enemy collided with player!")
            running = False

    pygame.display.update()
