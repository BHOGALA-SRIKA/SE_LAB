"""
Balloon objects and their scoring types.
Balloon: falls from the top of the screen. The player must pop it
before it reaches the bottom. Balloons vary in size - this matters for
how click detection should work.
"""

import pygame


BALLOON_TYPES = {
    "normal": {"color": (220, 70, 100), "points": 10, "label": "+10"},
    "bonus": {"color": (50, 175, 95), "points": 25, "label": "+25"},
    "penalty": {"color": (80, 105, 220), "points": -15, "label": "-15"},
}


class Balloon:
    def __init__(self, x, y, radius, speed, balloon_type="normal", color=None):
        if balloon_type not in BALLOON_TYPES:
            raise ValueError(f"Unknown balloon type: {balloon_type}")

        self.x = x
        self.y = y
        self.radius = radius
        self.speed = speed
        self.balloon_type = balloon_type
        self.points = BALLOON_TYPES[balloon_type]["points"]
        self.label = BALLOON_TYPES[balloon_type]["label"]
        self.color = color if color is not None else BALLOON_TYPES[balloon_type]["color"]

    def update(self):
        self.y += self.speed

    def is_past_bottom(self, height):
        return self.y - self.radius > height

    def get_rect(self):
        return pygame.Rect(
            int(self.x - self.radius), int(self.y - self.radius),
            self.radius * 2, self.radius * 2,
        )
