"""All pygame drawing lives here, separate from game logic."""

import pygame

WIDTH, HEIGHT = 700, 500
WINDOW_SIZE = (WIDTH, HEIGHT)

COLOR_BG = (200, 230, 245)
COLOR_TEXT = (30, 30, 30)
COLOR_STEM = (120, 120, 120)
COLOR_OVERLAY = (20, 30, 45)
COLOR_BUTTON = (50, 145, 90)
RESTART_BUTTON_RECT = pygame.Rect(WIDTH // 2 - 85, HEIGHT // 2 + 45, 170, 44)


def draw_scene(surface, balloons):
    surface.fill(COLOR_BG)
    for balloon in balloons:
        center = (int(balloon.x), int(balloon.y))
        pygame.draw.circle(surface, balloon.color, center, balloon.radius)
        pygame.draw.line(
            surface, COLOR_STEM,
            (balloon.x, balloon.y + balloon.radius),
            (balloon.x, balloon.y + balloon.radius + 12), 2,
        )
        # Display the scoring effect on the balloon so each type is identifiable.
        label_font = pygame.font.SysFont("consolas", max(12, min(18, balloon.radius // 2)))
        label = label_font.render(balloon.label, True, (255, 255, 255))
        surface.blit(label, label.get_rect(center=center))


def draw_text(surface, font, text, pos, color=COLOR_TEXT):
    surface.blit(font.render(text, True, color), pos)


def draw_game_over(surface, font, final_score):
    """Draw a clear game-over overlay and a clickable restart button."""
    overlay = pygame.Surface((surface.get_width(), surface.get_height()), pygame.SRCALPHA)
    overlay.fill((*COLOR_OVERLAY, 190))
    surface.blit(overlay, (0, 0))

    title_font = pygame.font.SysFont("consolas", 34, bold=True)
    title = title_font.render("GAME OVER", True, (255, 255, 255))
    surface.blit(title, title.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 - 55)))

    score_text = font.render(f"Final Score: {final_score}", True, (255, 255, 255))
    surface.blit(score_text, score_text.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 - 15)))

    pygame.draw.rect(surface, COLOR_BUTTON, RESTART_BUTTON_RECT, border_radius=8)
    button_font = pygame.font.SysFont("consolas", 22, bold=True)
    button_text = button_font.render("Restart", True, (255, 255, 255))
    surface.blit(button_text, button_text.get_rect(center=RESTART_BUTTON_RECT.center))
