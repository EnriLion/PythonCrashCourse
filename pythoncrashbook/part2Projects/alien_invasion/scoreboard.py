import pygame.font # we impor the pugame.font module

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):#we report the values we are tracking
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)# we set a text color
        self.font = pygame.font.SysFont(None, 48)# instantiate a font object

        # Prepare the initial score image.
        self.prep_score()#to turnt he text to be displayed into an image, we call prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)# we turn the numerical value stats.score into a string
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)# and then we pass the string render() and pass the screen's background color and text color to render

        # Display the score at the top  right of the screen.
        self.score_rect = self.score_image.get_rect()#A we create a variable called score_rect(score the upper-right cornert the score and the width of the number grows)
        self.score_rect.right = self.screen_rect.right - 20# we set its right edge of 20 pixels from the right edge of the screen
        self.score_rect.top = 20 # then place the top edge 20 pixels down from the top of the screen

    def show_score(self):# Draws the score image onscreen at the location socre_rect specifies
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
