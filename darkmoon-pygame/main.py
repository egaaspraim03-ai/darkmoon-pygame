import pygame
import sys

# ====================== НАСТРОЙКИ ======================
WIDTH, HEIGHT = 800, 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NÉXUS • DARK MOON")
clock = pygame.time.Clock()

# Шрифты
title_font = pygame.font.Font(None, 74)
subtitle_font = pygame.font.Font(None, 36)

def draw_title_screen():
    screen.fill((15, 5, 35))  # тёмно-фиолетовый фон

    # Главный заголовок
    title = title_font.render("NÉXUS • DARK MOON", True, (180, 0, 255))
    title_rect = title.get_rect(center=(WIDTH//2, HEIGHT//2 - 80))
    screen.blit(title, title_rect)

    # Подзаголовок
    subtitle = subtitle_font.render("Параллельная реальность", True, (220, 220, 255))
    subtitle_rect = subtitle.get_rect(center=(WIDTH//2, HEIGHT//2 + 10))
    screen.blit(subtitle, subtitle_rect)

    # Инструкция
    start_text = subtitle_font.render("Нажми ПРОБЕЛ чтобы войти в мир", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=(WIDTH//2, HEIGHT - 80))
    screen.blit(start_text, start_rect)

running = True
in_title = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and in_title:
            if event.key == pygame.K_SPACE:
                in_title = False
                print("→ Игра запущена! Переход в мир...")

    if in_title:
        draw_title_screen()
    else:
        screen.fill((10, 15, 25))
        text = subtitle_font.render("Мир Darkmon загружается...", True, (200, 200, 255))
        screen.blit(text, (WIDTH//2 - 140, HEIGHT//2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
