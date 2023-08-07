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
        self.prep_high_score()
        self.prep_level()

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        #  The prep_level() method creates an image from the value stored in stats.level

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()# set's the image's right attribute to match the score's right attribute
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10# then sets the top attribute 10 pixels beneath the bottom of the score image to leave space betwen the score and the level

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)# we round the high score to the neares 10 and format it with commas
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)
        # generate an image from the high score

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx # center the high score rect horizontally
        self.high_score_rect.top = self.score_rect.top # set a top attribute to match the top of the score image

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        # score_str = str(self.stats.score)# we turn the numerical value stats.score into a string
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)# and then we pass the string render() and pass the screen's background color and text color to render

        # Display the score at the top  right of the screen.
        self.score_rect = self.score_image.get_rect()#A we create a variable called score_rect(score the upper-right cornert the score and the width of the number grows)
        self.score_rect.right = self.screen_rect.right - 20# we set its right edge of 20 pixels from the right edge of the screen
        self.score_rect.top = 20 # then place the top edge 20 pixels down from the top of the screen

    def show_score(self):# Draws the score image onscreen at the location socre_rect specifies
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def check_high_score(self):
        """Check to see it there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
