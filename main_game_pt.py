import random
import os
import time
from colorama import init, Fore, Back, Style # trocar cor
import dragon as dg
import personagem as pg

# Constantes
DANO_FRACO = 40
DANO_FORTE = 60
DANO_ESPECIAL = 100
VIDA_PERSONAGEM = 200
VIDA_DRAGAO = 300
CURA = 30
MANA = 100 # recupera 5 a cada turno

init()

# Imprime a descrição do inimigo
def descricaoMenu(): # acrescentar uma "imagem"
    print(f"{Fore.RED}  █████  ████████  █████   ██████  ██    ██ ███████     ██████   ██████      ██████  ██████   █████   ██████   █████   ██████\n", 
                      "██   ██    ██    ██   ██ ██    ██ ██    ██ ██          ██   ██ ██    ██     ██   ██ ██   ██ ██   ██ ██       ██   ██ ██    ██\n", 
                      "███████    ██    ███████ ██    ██ ██    ██ █████       ██   ██ ██    ██     ██   ██ ██████  ███████ ██   ███ ███████ ██    ██\n",
                      "██   ██    ██    ██   ██ ██ ▄▄ ██ ██    ██ ██          ██   ██ ██    ██     ██   ██ ██   ██ ██   ██ ██    ██ ██   ██ ██    ██\n",
                      "██   ██    ██    ██   ██  ██████   ██████  ███████     ██████   ██████      ██████  ██   ██ ██   ██  ██████  ██   ██  ██████\n"
                     "                              ▀▀                                                                                               ")
    print(f"{Style.RESET_ALL}O Dragão das Sombras se aproxima")
    print("  O Dragão das Sombras é uma criatura aterrorizante que habita as profundezas das cavernas mais escuras e esquecidas. \n  Seu corpo colossal é coberto por escamas negras que absorvem a luz, tornando-o quase invisível nas sombras.\n  Seus olhos vermelhos brilham com uma inteligência maligna e um desejo insaciável de poder.\n")

# Valida as vidas para achar algum vencedor
def morte(vida, vidaInimigo):
    if vida <= 0:
        print(f"{Fore.RED}Você morreu{Style.RESET_ALL}")
        return True
    if vidaInimigo <= 0:
        print(f"{Fore.GREEN}Você derrotou o dragão!{Style.RESET_ALL}")
        return True
    return False

# Imprime o "menu" com as vidas dos personagens
def menuVida(nome, mana, vida, vidaInimigo):
    if (vidaInimigo < 0):
        vidaInimigo = 0
    
    print("="*34)
    print(f" {nome}: Vida: {vida} Mana: {mana}")
    print(f" Dragão das Sombras: Vida: {vidaInimigo}")
    print("="*34)

# Aonde será chamado os outros métodos
def main():
    fim = False
    vida = VIDA_PERSONAGEM
    mana = MANA
    vidaInimigo = VIDA_DRAGAO
    lista_set_fraco = []
    lista_set_forte = []
    nome, lista_set_fraco, lista_set_forte = pg.create_caracter()
    #item = pg.escolher_item()

    # if item == "2":
    #     vida += 100

    time.sleep(1) # espera 1 seg
    os.system('cls') # executa 'cls' no terminal para limpar

    while fim == False:
        menuVida(nome, mana, vida, vidaInimigo)
        dano, vida, mana = pg.movimento_personagem(nome, lista_set_fraco, lista_set_forte, vida, mana)
        
        if (mana < 100):
            print("Recarga de MANA + 5")
            mana += 5
            
        vidaInimigo -= dano
        menuVida(nome, mana, vida, vidaInimigo) 
        fim = morte(vida, vidaInimigo)
        if fim == True:
                break
            
        danodrag = dg.inimigoDrag()
        vida -= danodrag
        fim = morte(vida, vidaInimigo)

        # if fim == True and item == "3":
        #     print("Você usou seu Anel da Ressureição")
        #     vida = 80
        #     item =  None
        #     fim = False

    print("Fim de Jogo")

# "Menu iniciar" do jogo 
if __name__ == "__main__":
    time.sleep(1)
    os.system("cls")
    descricaoMenu()
    while True:
        print("\n")
        print("=" * 100)
        print(" "*40,"Iniciar: S | Sair: E\n")
        g = input("Opção: ").upper()
        if g == "S":
            time.sleep(1)
            os.system("cls")
            main()
        elif g == "E":
            break