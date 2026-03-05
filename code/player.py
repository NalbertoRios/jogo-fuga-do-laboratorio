import pygame
from code import const


class Player:
    def __init__(self):
        self.rect = pygame.Rect(
            const.LARGURA // 2 - const.PLAYER_TAMANHO // 2,
            const.ALTURA // 2 - const.PLAYER_TAMANHO // 2,
            const.PLAYER_TAMANHO,
            const.PLAYER_TAMANHO
        )

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= const.PLAYER_VELOCIDADE
        if teclas[pygame.K_RIGHT]:
            self.rect.x += const.PLAYER_VELOCIDADE
        if teclas[pygame.K_UP]:
            self.rect.y -= const.PLAYER_VELOCIDADE
        if teclas[pygame.K_DOWN]:
            self.rect.y += const.PLAYER_VELOCIDADE

        self.rect.x = max(0, min(self.rect.x, const.LARGURA - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, const.ALTURA - self.rect.height))

    def desenhar(self, tela):
        pygame.draw.rect(tela, const.VERDE, self.rect)