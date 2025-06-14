import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/spiderman.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a decimal value for the ships horizontal position
        self.x = self.rect.x
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ships position based on the movement flags."""
        # Update the ships x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # Update rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)