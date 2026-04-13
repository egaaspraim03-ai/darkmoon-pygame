# config.py — все настройки игры в одном месте

# ==================== Основные настройки ====================
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
TITLE = "NÉXUS • DARK MOON"

# Цвета (тёмная тема Dark Moon)
BACKGROUND_COLOR = (15, 5, 35)
TEXT_COLOR = (220, 220, 255)
ACCENT_COLOR = (180, 0, 255)

# Размер тайлов
TILE_SIZE = 48

# Скорость игрока
PLAYER_SPEED = 5

# ==================== Пути к файлам ====================
ASSETS_DIR = "assets"
DATA_DIR = "data"

# Пути к спрайтам
PLAYER_SPRITES = {
    "down":  f"{ASSETS_DIR}/sprites/player/boy_down.png",
    "up":    f"{ASSETS_DIR}/sprites/player/boy_up.png",
    "left":  f"{ASSETS_DIR}/sprites/player/boy_left.png",
    "right": f"{ASSETS_DIR}/sprites/player/boy_right.png"
}

# Путь к тайлсету (пока можно использовать любой)
TILESET_PATH = f"{ASSETS_DIR}/tiles/tileset.png"

# Стартовые настройки
START_MONEY = 3000
START_ZONE = "saffron_city"
