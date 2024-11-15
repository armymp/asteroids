import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT, OFF_SCREEN_TIMER


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.off_screen_timer = 0

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            2
        )

    def is_off_screen(self):
        return (self.position.x + self.radius < 0 or
                self.position.x - self.radius > SCREEN_WIDTH or
                self.position.y + self.radius < 0 or
                self.position.y - self.radius > SCREEN_HEIGHT)

    def update(self, dt):
        self.position += self.velocity * dt

        if self.is_off_screen():
            self.off_screen_timer += dt
            if self.off_screen_timer >= OFF_SCREEN_TIMER:
                self.kill()
        else:
            self.off_screen_timer = 0