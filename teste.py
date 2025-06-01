import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Batalha RPG - Pygame")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
PRETO = (0, 0, 0)

# Fonte
fonte = pygame.font.SysFont("arial", 30)

# Atributos do jogador e inimigo
vida_jogador = 200
vida_inimigo = 300

# Loop principal
rodando = True
while rodando:
    tela.fill(PRETO)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_a:
                dano = random.randint(30, 50)
                vida_inimigo -= dano
            elif evento.key == pygame.K_s:
                dano = random.randint(60, 80)
                vida_inimigo -= dano
            elif evento.key == pygame.K_d:
                vida_jogador += 30
                if vida_jogador > 200:
                    vida_jogador = 200

    # Ataque do inimigo
    if random.random() < 0.01:
        dano = random.randint(40, 60)
        vida_jogador -= dano

    # Barras de vida
    pygame.draw.rect(tela, VERMELHO, (50, 50, 200, 25))
    pygame.draw.rect(tela, VERDE, (50, 50, max(0, vida_jogador), 25))

    pygame.draw.rect(tela, VERMELHO, (550, 50, 200, 25))
    pygame.draw.rect(tela, VERDE, (550, 50, max(0, vida_inimigo), 25))

    # Texto
    texto1 = fonte.render("A: Ataque Fraco", True, BRANCO)
    texto2 = fonte.render("S: Ataque Forte", True, BRANCO)
    texto3 = fonte.render("D: Curar", True, BRANCO)

    tela.blit(texto1, (50, 500))
    tela.blit(texto2, (50, 540))
    tela.blit(texto3, (50, 580))

    # Atualiza a tela
    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()
