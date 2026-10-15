"""Game engine for Balloon Pop, including scoring, lives, and timed rounds."""

import random
import time

from game.balloon import BALLOON_TYPES, Balloon
from game.click_detection import check_pop
from game.renderer import WIDTH, HEIGHT, RESTART_BUTTON_RECT

ROUND_DURATION_SECONDS = 30

SPAWN_INTERVAL_FRAMES = 45
BALLOON_TYPE_CHOICES = ("normal", "normal", "normal", "bonus", "penalty")


class GameEngine:
    def __init__(self):
        self.restart()

    @property
    def time_left(self):
        """Whole seconds remaining, calculated from elapsed wall-clock time."""
        elapsed = time.monotonic() - self.round_started_at
        return max(0, int(ROUND_DURATION_SECONDS - elapsed + 0.999999))

    def restart(self):
        """Reset all round state, including timer and spawn timing."""
        self.balloons = []
        self.frames_until_spawn = 0
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.round_started_at = time.monotonic()

    def _finish_if_needed(self):
        if self.lives <= 0 or self.time_left <= 0:
            self.lives = max(0, self.lives)
            self.game_over = True

    def _spawn_balloon(self):
        radius = random.randint(16, 44)
        x = random.randint(radius + 10, WIDTH - radius - 10)
        speed = random.uniform(1.5, 3.0)
        balloon_type = random.choice(BALLOON_TYPE_CHOICES)
        self.balloons.append(
            Balloon(x=x, y=-radius, radius=radius, speed=speed, balloon_type=balloon_type)
        )

    def handle_click(self, pos):
        if self.game_over:
            if RESTART_BUTTON_RECT.collidepoint(pos):
                self.restart()
            return

        # Check the clock before allowing a gameplay click at the deadline.
        self._finish_if_needed()
        if self.game_over:
            return

        popped = check_pop(self.balloons, pos)
        if popped is not None:
            self.balloons.remove(popped)
            self.score += popped.points

    def update(self):
        self._finish_if_needed()
        if self.game_over:
            return

        self.frames_until_spawn -= 1
        if self.frames_until_spawn <= 0:
            self._spawn_balloon()
            self.frames_until_spawn = SPAWN_INTERVAL_FRAMES

        for b in self.balloons:
            b.update()

        # Process each missed balloon once. Normal and bonus balloons cost
        # one life; missed penalty balloons do not cost a life.
        missed = [b for b in self.balloons if b.is_past_bottom(HEIGHT)]
        if missed:
            life_losing_misses = sum(
                1 for b in missed if b.balloon_type in ("normal", "bonus")
            )
            self.lives = max(0, self.lives - life_losing_misses)
            missed_ids = {id(b) for b in missed}
            self.balloons = [b for b in self.balloons if id(b) not in missed_ids]

        self._finish_if_needed()

    def draw(self, surface, font):
        from game import renderer
        renderer.draw_scene(surface, self.balloons)
        renderer.draw_text(surface, font, f"Score: {self.score}", (10, 10))
        renderer.draw_text(surface, font, f"Lives: {self.lives}", (10, 38))
        renderer.draw_text(surface, font, f"Time: {self.time_left}s", (10, 66))
        if self.game_over:
            renderer.draw_game_over(surface, font, self.score)
