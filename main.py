import pygame
import sys
from config import *
from core.player import Player
from core.camera import Camera

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Создаём объекты
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

    keys = pygame.key.get_pressed()

    if in_title_screen:
        # Красивая заставка
        screen.fill(BACKGROUND_COLOR)
        
        title = pygame.font.Font(None, 74).render("NÉXUS • DARK MOON", True, ACCENT_COLOR)
        subtitle = pygame.font.Font(None, 36).render("Параллельная реальность", True, TEXT_COLOR)
        start = pygame.font.Font(None, 36).render("Нажми ПРОБЕЛ чтобы войти", True, TEXT_COLOR)
        
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 80)))
        screen.blit(subtitle, subtitle.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 10)))
        screen.blit(start, start.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 80)))
    else:
        # Игровой мир
        screen.fill((10, 15, 30))
        
        # Обновляем игрока
        player.update(keys)
        
        # Обновляем камеру
        camera.update(player)
        
        # Рисуем игрока с учётом камеры
        draw_x = player.rect.x - camera.offset_x
        draw_y = player.rect.y - camera.offset_y
        screen.blit(player.image, (draw_x, draw_y))

        # Временный текст (пока нет карты)
        text = pygame.font.Font(None, 36).render("Мир Darkmon (карта скоро появится)", True, (180, 180, 255))
        screen.blit(text, (50, 50))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
