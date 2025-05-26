import random
from colorama import init, Fore, Back, Style
init()

DANO_SOPRO_ACIDO = 60
DANO_CHAMAS_NEGRAS = 75
VIDA_DRAGAO = 300

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
        print(f"Dado: {num} {Fore.RED}\nO Dragão errou!{Style.RESET_ALL}")
        return 0
    else:
        efet = 0.6 if num == 3 else 0.8 if num == 4 else 1
        dano_final = efet * dano
        print("Dado: ", num, "\nO Dragão te acertou!", "\nDano: ", dano_final)
        return dano_final