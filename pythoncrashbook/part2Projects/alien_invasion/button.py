import pygame.font

class Button:

    def __init__(self, ai_game, msg):#The __init__() method thakes the parameters self, the ai_game object and msg which contains the button's text
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50# we set the button dimensions
        self.button_color = (0, 255, 0)#We set button_color the button's rect object bright green and set aswell the text color to render the text in white
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)#We prepare a font attribute for rendering text(The None argument tells Pygame to use the default font(48 specifies the size of the text)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)#We center the button on the screen and we create a rect for the button and center attribute to mathc that of the screen.
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once
        self._prep_msg(msg)# we call _prep_msg() to handle the rendering


    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)# we stored the ms into an image and the font.render() methods also takes a Boolean value to turn antialiasing on or off (antialiasing makes the edges of the text smoother)
        self.msg_image_rect = self.msg_image.get_rect()#we center the text image on the butotn by creatin a rect from the image and setting its center attribute to match that of the button.
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
