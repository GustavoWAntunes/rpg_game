import random

# Constantes
DANO_FRACO = 40
DANO_FORTE = 60
DANO_ESPECIAL = 100
DANO_SOPRO_ACIDO = 60
DANO_CHAMAS_NEGRAS = 75
VIDA_PERSONAGEM = 200
VIDA_DRAGAO = 300
CURA = 30

# Decide qual movimento o personagem vai usar
def personagem(tempo, item=None):
    dano = 50 if item == True else 0
    if tempo >= 3:
        print("Escolha a sua ação: \n- (X) Ataque fraco\n- (Y) Ataque forte\n- (B) Ataque especial\n- (A) Curar")
    else:
        print("Escolha a sua ação: \n- (X) Ataque fraco\n- (Y) Ataque forte\n- (A) Curar")
    mov = input()
    if mov.upper() == "X":
        print("Você escolheu ataque fraco!")
        dano += DANO_FRACO
    elif mov.upper() == "Y":
        print("Você escolheu ataque forte!")
        dano += DANO_FORTE
    elif mov.upper() == "B":
        print("Você escolheu ataque especial!")
        dano += DANO_ESPECIAL
        tempo = 0
    elif mov.upper() == "A":
        print("Você escolheu se curar!\n+30 de hp")
        return 1, tempo
    else:
        print("Movimento Errado!")

    danos = dadoPersonagem(dano, mov)
    return danos, tempo

# Decide qual movimento o Dragão vai usar
def inimigoDrag():
    print("O Dragão vai atacar")
    mov = random.randint(1, 2)
    dano = 0
    if mov == 1:
        print("O Dragão das Sombras usa sopro ácido")
        dano = DANO_SOPRO_ACIDO
    elif mov == 2:
        dano = DANO_CHAMAS_NEGRAS
        print("O Dragão das Sombras usa explosão de chamas negras")

    danonov = dadoDragao(dano)
    return danonov

# Joga no "dado" para ver a efetividade do ataque do Dragão
def dadoDragao(dano):
    num = random.randint(1, 5)
    if num <= 2:
        print("Dano: ", num, "\nO Dragão errou!")
        return 0
    else:
        efet = 0.6 if num == 3 else 0.8 if num == 4 else 1
        dano_final = efet * dano
        print("Dano: ", num, "\nO Dragão te acertou!", "\nDano: ", dano_final)
        return dano_final

# Imprime a descrição do inimigo
def descInimigo():
    print("O Dragão das Sombras se aproxima")
    print("  O Dragão das Sombras é uma criatura aterrorizante que habita as profundezas das cavernas mais escuras e esquecidas. \n  Seu corpo colossal é coberto por escamas negras que absorvem a luz, tornando-o quase invisível nas sombras.\n  Seus olhos vermelhos brilham com uma inteligência maligna e um desejo insaciável de poder.")

# Valida as vidas para achar algum vencedor
def morte(vida, vidaInimigo):
    if vida <= 0:
        print("Você morreu")
        return True
    if vidaInimigo <= 0:
        print("Você derrotou o dragão!")
        return True
    return False

# Joga no "dado" para ver a efetividade do ataque do Personagem
def dadoPersonagem(dano, mov):
    num = random.randint(1, 5)
    
    if mov.upper() == 'X':
        if num <= 2:
            print("Dado: ", num, "\nVocê errou!")
            return 0
        else:
            efet = 0.6 if num == 3 else 0.8 if num == 4 else 1
            dano_final = efet * dano
            print("Dado: ", num, "\nVocê deu ", dano_final, " de dano!") 
            return dano_final
    elif mov.upper() == 'Y':
        if num <= 3:
            print("Dado: ", num, "\nVocê errou!")
            return 0
        else:
            efet = 0.7 if num == 4 else 1
            dano_final = efet * dano
            print("Dado: ", num, "\nVocê deu ", dano_final, " de dano!") 
            return dano_final
    else:
            efet = 0.5 if num in [1, 2, 3] else 0.7 if num == 4 else 1
            dano_final = efet * dano
            print("Dado: ", num, "\nVocê deu ", dano_final, " de dano!") 
            return dano_final

# Imprime o "menu" com as vidas dos personagens
def menuVida(vida, vidaInimigo):
    print("_"*34)
    print("| Sua vida: ", vida, " "*15,"| ", 
            "\n| Vida Dragão das Sombras: ", vidaInimigo, " |")
    print("-"*34)

# Escolher item que irá auxiliar na batalha
def escolher_item():
    print("-"*100,"\nVocê pode escolher um entre estes três itens para te auxiliar na batalha")
    print(" Espada Flamejante - Uma espada encantada com o poder do fogo, que aumenta o dano causado em batalhas. (1)",
          "\n Amuleto da Vitalidade - Um amuleto que contém uma poderosa energia de cura, aumentando a vida do portador. (2)",
          "\n Anel da Ressureição - Um anel raro que concede ao usuário uma segunda chance de vida ao ser derrotado. (3)")
    while True:
        item = input("Item n*: ")
        if item in ["1", "2", "3"]:
            return item
        else:
            print("Número de item inválido")

# Aonde será chamado os outros métodos
def main():
    fim = False
    vida = VIDA_PERSONAGEM
    vidaInimigo = VIDA_DRAGAO
    tempo = 0
    descInimigo()
    item = escolher_item()

    if item == "2":
        vida += 100

    while fim == False:
        menuVida(vida, vidaInimigo)
        if item == "1":
            dano, tempos = personagem(tempo, True)
            tempo = tempos + 1
        else:
            dano, tempos = personagem(tempo)
            tempo = tempos + 1
        if dano == 1:
            vida += CURA
            menuVida(vida, vidaInimigo)
        else:
            vidaInimigo -= dano
            menuVida(vida, vidaInimigo)
            fim = morte(vida, vidaInimigo)
            if fim == True:
                break
            
        danodrag = inimigoDrag()
        vida -= danodrag
        fim = morte(vida, vidaInimigo)

        if fim == True and item == "3":
            print("Você usou seu Anel da Ressureição")
            vida = 80
            item =  None
            fim = False

    print("Fim de Jogo")

# "Menu iniciar" do jogo 
if __name__ == "__main__":
    while True:
        print("=" * 100)
        print("Iniciar: P", "\nSair: S")
        g = input("Opção: ").upper()
        print("-" * 100)
        if g == "P":
            main()
        elif g == "S":
            break