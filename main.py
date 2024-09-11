import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
TARGET_RADIUS = 30
TARGET_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)
BULLET_COLOR = (255, 255, 255)
FONT_COLOR = (255, 255, 255)
BULLET_RADIUS = 5

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тир")

# Шрифт
font = pygame.font.Font(None, 36)

# Функция для отображения текста
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Класс для мишени
class Target:
    def __init__(self):
        self.x = random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS)
        self.y = random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS)
        self.speed_x = random.choice([-4, -3, -2, 2, 3, 4])
        self.speed_y = random.choice([-4, -3, -2, 2, 3, 4])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= TARGET_RADIUS or self.x >= WIDTH - TARGET_RADIUS:
            self.speed_x = -self.speed_x
        if self.y <= TARGET_RADIUS or self.y >= HEIGHT - TARGET_RADIUS:
            self.speed_y = -self.speed_y

    def draw(self, surface):
        pygame.draw.circle(surface, TARGET_COLOR, (self.x, self.y), TARGET_RADIUS)

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    score = 0
    target = Target()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                distance = ((target.x - mouse_x) ** 2 + (target.y - mouse_y) ** 2) ** 0.5
                if distance <= TARGET_RADIUS:
                    score += 1
                    target = Target()

        screen.fill(BG_COLOR)
        target.move()
        target.draw(screen)

        draw_text(f'Очки: {score}', font, FONT_COLOR, screen, 10, 10)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()