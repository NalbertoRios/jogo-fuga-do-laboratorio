import pygame
import random
from code import const


class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(
            random.randint(0, const.LARGURA - const.ENEMY_TAMANHO),
            random.randint(0, const.ALTURA - const.ENEMY_TAMANHO),
            const.ENEMY_TAMANHO,
            const.ENEMY_TAMANHO
        )

        self.vel_x = random.choice([-1, 1]) * const.ENEMY_VELOCIDADE
        self.vel_y = random.choice([-1, 1]) * const.ENEMY_VELOCIDADE

    def mover(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Bateu na parede? Inverte direção
        if self.rect.left <= 0 or self.rect.right >= const.LARGURA:
            self.vel_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= const.ALTURA:
            self.vel_y *= -1

    def desenhar(self, tela):
        pygame.draw.rect(tela, const.VERMELHO, self.rect)