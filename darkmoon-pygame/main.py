import pygame
import sys
from config import *
from core.player import Player
from core.camera import Camera

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Создаём игрока и камеру
player = Player()
camera = Camera()

running = True
in_title_screen = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and in_title_screen:
            if event.key == pygame.K_SPACE:
                in_title_screen = False
                print("→ Игра запущена! Переход в мир Darkmon...")

    if in_title_screen:
        # Заставка
        screen.fill(BACKGROUND_COLOR)
        title = pygame.font.Font(None, 74).render("NÉXUS • DARK MOON", True, ACCENT_COLOR)
        subtitle = pygame.font.Font(None, 36).render("Параллельная реальность", True, TEXT_COLOR)
        start = pygame.font.Font(None, 36).render("Нажми ПРОБЕЛ чтобы войти", True, TEXT_COLOR)
        
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 80)))
        screen.blit(subtitle, subtitle.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 10)))
        screen.blit(start, start.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 80)))
    else:
        screen.fill((10, 15, 30))
        # Здесь будет overworld позже
        text = pygame.font.Font(None, 36).render("Мир Darkmon загружается...", True, TEXT_COLOR)
        screen.blit(text, (SCREEN_WIDTH//2 - 140, SCREEN_HEIGHT//2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
