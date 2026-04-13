import pygame
import sys
from config import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Шрифты
title_font = pygame.font.Font(None, 74)
subtitle_font = pygame.font.Font(None, 36)

def draw_title_screen():
    screen.fill(BACKGROUND_COLOR)
    
    title = title_font.render("NÉXUS • DARK MOON", True, ACCENT_COLOR)
    title_rect = title.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 80))
    screen.blit(title, title_rect)

    subtitle = subtitle_font.render("Параллельная реальность", True, TEXT_COLOR)
    subtitle_rect = subtitle.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 10))
    screen.blit(subtitle, subtitle_rect)

    start_text = subtitle_font.render("Нажми ПРОБЕЛ чтобы войти в мир", True, TEXT_COLOR)
    start_rect = start_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 80))
    screen.blit(start_text, start_rect)

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
        draw_title_screen()
    else:
        screen.fill((10, 15, 30))
        text = subtitle_font.render("Мир Darkmon загружается...", True, TEXT_COLOR)
        screen.blit(text, (SCREEN_WIDTH//2 - 140, SCREEN_HEIGHT//2))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
