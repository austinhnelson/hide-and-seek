import pygame


class InputManager:
    @staticmethod
    def is_enter_selected():
        keys = pygame.key.get_pressed()
        is_enter_key = False

        if keys[pygame.K_RETURN]:
            is_enter_key = True

        return is_enter_key

    @staticmethod
    def handle_player_input(player):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] | keys[pygame.K_a]:
            player.look_left()
        elif keys[pygame.K_RIGHT] | keys[pygame.K_d]:
            player.look_right()

        if keys[pygame.K_UP] | keys[pygame.K_w]:
            player.move_forward()
        elif keys[pygame.K_DOWN] | keys[pygame.K_s]:
            player.move_backward()
