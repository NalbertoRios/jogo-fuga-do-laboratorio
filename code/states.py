import pygame
import sys
from code import const
from code.player import Player
from code.enemy import Enemy


class MenuState:
    def __init__(self, game):
        self.game = game
        self.fonte_titulo = pygame.font.SysFont(None, 60)
        self.fonte_texto = pygame.font.SysFont(None, 30)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game.mudar_estado(GameState(self.game))
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self, tela):
        tela.fill(const.PRETO)

        titulo = self.fonte_titulo.render(
            "FUGA DO LABORATÓRIO", True, const.VERDE
        )
        tela.blit(
            titulo,
            (const.LARGURA // 2 - titulo.get_width() // 2, 150)
        )

        textos = [
            "SETAS - Mover",
            "ESC - Sair",
            "",
            "Pressione ENTER para jogar"
        ]

        y = 300
        for linha in textos:
            texto = self.fonte_texto.render(linha, True, const.BRANCO)
            tela.blit(
                texto,
                (const.LARGURA // 2 - texto.get_width() // 2, y)
            )
            y += 40


class GameState:
    def __init__(self, game):
        self.game = game
        self.player = Player()
        self.enemies = [Enemy() for _ in range(const.ENEMY_QUANTIDADE)]

        # variável para sons de colisão
        self.som_colisao = pygame.mixer.Sound("assets/colisao.wav")

        # música do level
        pygame.mixer.music.load("assets/game_level.wav")
        pygame.mixer.music.play(-1)

        # contador de tempo
        self.tempo_inicio = pygame.time.get_ticks()
        self.fonte_tempo = pygame.font.SysFont(None, 30)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                self.game.mudar_estado(MenuState(self.game))

    def update(self):
        teclas = pygame.key.get_pressed()
        self.player.mover(teclas)

        for enemy in self.enemies:
            enemy.mover()

            # Colisão
            if self.player.rect.colliderect(enemy.rect):
                tempo_final = (pygame.time.get_ticks() - self.tempo_inicio) // 1000
                self.som_colisao.play()
                pygame.mixer.music.stop()
                self.game.mudar_estado(GameOverState(self.game, tempo_final))

    def draw(self, tela):
        tela.fill(const.PRETO)
        self.player.desenhar(tela)

        for enemy in self.enemies:
            enemy.desenhar(tela)
        # contador de tempo
        tempo_atual = (pygame.time.get_ticks() - self.tempo_inicio) // 1000
        texto_tempo = self.fonte_tempo.render(f"Tempo: {tempo_atual}s", True, const.BRANCO)

        tela.blit(texto_tempo, (10, 10))


class GameOverState:
    def __init__(self, game, tempo_final):
        self.game = game
        self.tempo_final = tempo_final
        self.fonte = pygame.font.SysFont(None, 50)

        pygame.mixer.Sound("assets/game_over.wav").play()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game.mudar_estado(MenuState(self.game))

    def update(self):
        pass

    def draw(self, tela):
        tela.fill(const.PRETO)

        texto = self.fonte.render("GAME OVER", True, const.VERMELHO)
        tempo_texto = self.fonte.render(
            f"Você sobreviveu: {self.tempo_final} segundos",
            True,
            const.BRANCO
        )
        instrucao = self.fonte.render(
            "Pressione ENTER para voltar ao menu", True, const.BRANCO
        )

        tela.blit(
            texto,
            (const.LARGURA // 2 - texto.get_width() // 2, 250)
        )
        tela.blit(
            tempo_texto,
            (const.LARGURA // 2 - tempo_texto.get_width() // 2, 300)
        )
        tela.blit(
            instrucao,
            (const.LARGURA // 2 - instrucao.get_width() // 2, 350)
        )