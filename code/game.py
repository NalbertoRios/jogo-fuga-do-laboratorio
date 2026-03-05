import pygame
import sys
from code import const
from code.states import MenuState


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.tela = pygame.display.set_mode(
            (const.LARGURA, const.ALTURA)
        )
        pygame.display.set_caption(const.TITULO)
        self.clock = pygame.time.Clock()
        self.estado_atual = MenuState(self)

    def mudar_estado(self, novo_estado):
        self.estado_atual = novo_estado

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                self.estado_atual.handle_event(event)

            self.estado_atual.update()
            self.estado_atual.draw(self.tela)

            pygame.display.update()
            self.clock.tick(const.FPS)
