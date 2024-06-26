import random

def personagem(tempo, item=None):
    dano = 0
    if item == "sim": 
        dano += 50
    if tempo >= 3:
        print("Escolha a sua ação: \n- (X) Ataque fraco\n- (Y) Ataque forte\n- (B) Ataque especial\n- (A) Curar")
    else:
        print("Escolha a sua ação: \n- (X) Ataque fraco\n- (Y) Ataque forte\n- (A) Curar")
    mov = input()
    if mov.upper() == "X":
        print("Você escolheu ataque fraco!")
        dano += 40
    elif mov.upper() == "Y":
        print("Você escolheu ataque forte!")
        dano += 60
    elif mov.upper() == "B":
        print("Você escolheu ataque especial!")
        dano += 100
        tempo = 0
    elif mov.upper() == "A":
        print("Você escolheu se curar!")
        return 1, tempo
    else:
        print("Movimento Errado!")

    danos = dadoPersonagem(dano, mov, "per")
    return danos, tempo

def inimigoDrag():
    print("O Dragão vai atacar")
    mov = random.randint(1, 2)
    dano = 0
    if mov == 1:
        print("O Dragão das Sombras usa sopro ácido")
        dano = 60
    elif mov == 2:
        dano = 75
        print("O Dragão das Sombras usa explosão de chamas negras")

    danonov = dadoDragão(dano)
    return danonov

def dadoDragão(dano):
    danon = 0
    num = random.randint(1, 5)
    if num <= 2:
        print("O Dragão errou!")
    elif num == 3:
        danon = dano * 0.6
        print("O Dragão te acertou!", "\nDano: ", danon)
    elif num == 4:
        danon = dano * 0.8
        print("O Dragão te acertou!", "\nDano: ", danon)
    elif num == 5:
        danon = dano
        print("O Dragão te acertou!", "\nDano: ", dano)

    return danon

def descInimigo():
    print("O Dragão das Sombras se aproxima")
    print("  O Dragão das Sombras é uma criatura aterrorizante que habita as profundezas das cavernas mais escuras e esquecidas. \n  Seu corpo colossal é coberto por escamas negras que absorvem a luz, tornando-o quase invisível nas sombras.\n  Seus olhos vermelhos brilham com uma inteligência maligna e um desejo insaciável de poder.")

def morte(vida, vidaInimigo):
    fim = 0
    if vida <= 0:
        print("Você morreu")
        fim = 1
    if vidaInimigo <= 0:
        print("Você derrotou o dragão!")
        fim = 1 
    return fim

def dadoPersonagem(dano, mov, carac):
    num = random.randint(1, 5)
    danon = 0
    if carac == "per":
        if mov.upper() == 'X':
            if num <= 2:
                print("Dado: ", num, "\nVocê errou!") 
            elif num == 3:
                danon = dano * 0.6
                print("Dado: ", num, "\nVocê deu ", danon, " de dano!") 
            elif num == 4:
                danon = dano * 0.8
                print("Dado: ", num, "\nVocê deu ", danon, " de dano!") 
            elif num == 5:
                danon = dano
                print("Dado: ", num, "\nVocê deu ", danon, " de dano!") 
        elif mov.upper() == "Y":
            if num <= 3:
                print("Dado: ", num, "\nVocê errou!") 
            elif num == 4:
                danon = dano * 0.7
                print("Dado: ", num, "\nVocê deu ", danon, " de dano!") 
            elif num == 5:
                danon = dano
                print("Dado: ", num, "\nVocê deu ", danon, " de dano!") 
        elif mov.upper() == "B":
            if num <= 3:
                danon = dano * 0.5
                print("Dado: ", num, "\nVocê deu ", danon, " de dano!") 
            elif num == 4:
                danon = dano * 0.7
                print("Dado: ", num, "\nVocê deu ", danon, " de dano!") 
            elif num == 5:
                danon = dano
                print("Dado: ", num, "\nVocê deu ", danon, " de dano!") 
        elif mov.upper() == "A":
            print("Você usou cura, +20 de hp")
        else:
            print("Opção incorreta!")

    return danon

def menuVida(vida, vidaInimigo):
    print("_"*34)
    print("| Sua vida: ", vida, " "*15,"| ", 
            "\n| Vida Dragão das Sombras: ", vidaInimigo, " |")
    print("-"*34)

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

def main():
    fim = 0
    vida = 200
    vidaInimigo = 300
    tempo = 0
    descInimigo()
    item = escolher_item()

    if item == "2":
        vida += 100

    while fim == 0:
        menuVida(vida, vidaInimigo)
        if item == "1":
            dano, tempos = personagem(tempo, "sim")
            tempo = tempos + 1
        else:
            dano, tempos = personagem(tempo)
            tempo = tempos + 1
        if dano == 1:
            vida += 30
            menuVida(vida, vidaInimigo)
        else:
            vidaInimigo -= dano
            menuVida(vida, vidaInimigo)
            fim = morte(vida, vidaInimigo)
            if fim == 1:
                break
        danodrag = inimigoDrag()
        vida -= danodrag
        fim = morte(vida, vidaInimigo)

        if fim == 1 and item == "3":
            print("Você usou seu Anel da Ressureição")
            vida = 80
            item =  None
            fim = 0

    print("Fim de Jogo")

if __name__ == "__main__":
    g = ""
    while g.upper() != "S":
        print("="*100)
        print("Iniciar: P", "\nSair: S")
        g = input("Opção: ")
        print("-"*100)
        if g.upper() == "P":
            main()