import pygame


class InputManager:
    @staticmethod
    def handle_menu_input(menu_screen):
        keys = pygame.key.get_pressed()
        isMenu = True

        # handle position movement
        if keys[pygame.K_RETURN]:
            isMenu = False

        return isMenu

    @staticmethod
    def handle_player_input(player):
        keys = pygame.key.get_pressed()

        # handle angle movement
        if keys[pygame.K_LEFT] | keys[pygame.K_a]:
            player.move_left()
        elif keys[pygame.K_RIGHT] | keys[pygame.K_d]:
            player.move_right()

        # handle position movement
        if keys[pygame.K_UP] | keys[pygame.K_w]:
            player.move_forward()
        elif keys[pygame.K_DOWN] | keys[pygame.K_s]:
            player.move_backward()
