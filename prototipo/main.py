import pygame
from equipamentos import *
from personagens import *
from action import Disparo
from map import *

BLACK = (46, 46, 46)
GREEN = (0, 128, 0)


def init():
    pass

# iniciar pygame
pygame.init()
# tamanho da janela
display = pygame.display.set_mode([1024, 768])
# nome do display
pygame.display.set_caption("Jogo do grupo 2")

# Grupos de sprites. (uma das funcionalidades dos grupos de sprite são de detectar colisões entre eles.)
objectGroup = pygame.sprite.Group()
actionGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
blockGroup = pygame.sprite.Group()



# Objetos

#para testes arma
gun = Arma()
pocao = Item()

vida = 100
dano = 50


jogador = Player(100,50,gun,pocao,objectGroup)

imagem_inimigo = pygame.image.load("arquivos/enemy.png")


newEnemy0 = Enemy(vida, dano, gun , imagem_inimigo, objectGroup,enemyGroup)
newEnemy0.rect.center = [812, 584] # posição
newEnemy1 = Enemy(vida, dano, gun ,imagem_inimigo, objectGroup,enemyGroup)
newEnemy1.rect.center = [112, 284]




# barra de vida e barra de armamentos
font = pygame.font.Font('freesansbold.ttf', 32)
barraVida = font.render("Aqui quantas vidas o personagem tem", True, (255, 255, 255), (0, 0, 0))
barraVidaRect = barraVida.get_rect()
barraVidaRect.center = (512, 20)

barraArmamento = font.render("Aqui os armamentos", True, (255, 255, 255), (0, 0, 0))
barraArmamentoRect = barraArmamento.get_rect()
barraArmamentoRect.center = (512, 748)

font = pygame.font.Font('freesansbold.ttf', 18)
porta = font.render("next map", True, (255, 255, 255), (0, 0, 0))
portaRect = porta.get_rect()
portaRect.center = (980, 400)


# Draw
def draw_window(current_map):  # lógica para criação do map

    for y in range(len(current_map)):
        for x in range(len(current_map[y])):
            if current_map[y][x] == "X":
                rect1 = Block(blockGroup)
                rect1.rect.x = x * 32
                rect1.rect.y = y * 32

draw_window(map1)

#FPS
clock = pygame.time.Clock()
FPS = 120

# Main
def loop_principal():
    gameLoop = True
    while gameLoop:
        clock.tick(FPS)  # método tick, força gameLoop a rodar em FPS atribuido
        # eventos de mouse ou teclado
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                gameLoop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    novoDisparo = Disparo(objectGroup, actionGroup)
                    novoDisparo.rect.center = jogador.rect.center

                if event.key == pygame.K_d:
                    jogador.mover_direita()

                if event.key == pygame.K_a:
                    jogador.mover_esquerda()

                if event.key == pygame.K_w:
                    jogador.mover_cima()

                if event.key == pygame.K_s:
                    jogador.mover_baixo()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    jogador.parar_horizontal()
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    jogador.parar_vertical()

        # colliding
        pygame.sprite.groupcollide(actionGroup, enemyGroup, True, True)  # colisão entre tiro e inimigo
        collisionPlayerEnemy = pygame.sprite.spritecollide(jogador, enemyGroup, False, pygame.sprite.collide_mask) # colisão entre jogador e inimigo

        if collisionPlayerEnemy:
            print("Game Over")
            gameLoop = False

        jogador.teste_colisao(blockGroup)


        # draw
        display.fill(BLACK)
        display.blit(barraVida, barraVidaRect), (barraArmamento, barraArmamentoRect)
        display.blit(barraArmamento, barraArmamentoRect)
        display.blit(porta, portaRect)
        objectGroup.draw(display)
        blockGroup.draw(display)  # desenha os sprites

        # update
        objectGroup.update()
        pygame.display.update()

