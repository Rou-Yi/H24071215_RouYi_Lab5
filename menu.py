import pygame
import os

# load image
UPGRAGE_MENU = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRAGE_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "upgrade.png")), (70, 50))
SELL_BUTTON = pygame.transform.scale(pygame.image.load(os.path.join("images", "sell.png")), (50, 50))


class UpgradeMenu:
    def __init__(self, x, y):
        # Add buttons upgrade and sell
        self.__buttons = [Button(UPGRAGE_BUTTON, "upgrade", x, y-70),
                          Button(SELL_BUTTON, "sell", x, y+75)]

        self.image = pygame.transform.scale(UPGRAGE_MENU, (200, 200))  # image of the upgrade menu
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the menu image

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.image, self.rect)

        # draw button (Q2)
        for but in self.__buttons:
            win.blit(but.image, but.rect)

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.name = name    # name of the button
        self.image = image  # image of the button
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # center of the menu image

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name






