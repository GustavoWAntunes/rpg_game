import json
import random
from colorama import init, Fore, Back, Style
import os
import time

init()

    # time.sleep(1) # espera 1 seg
    # os.system('cls') # executa 'cls' no terminal para limpar

# escolha suas habilidaes
def create_caracter():
    print("======= Crie seu Personagem =======")
    nome = input("Escolha seu nome: ")

    time.sleep(0.5)
    os.system('cls')

    print("ESCOLHA AS SUAS HABILIDADES(APENAS DUAS):")

    # DANO "FRACO"
    print("[1] Corte Veloz(40 de dano) - Dê um corte rápido no inimigo")
    print("[2] Rajada Gelada(50 de dano, - 20 de Mana) - Lance uma forte rajada de gelo no inimigo")
    print("[3] Benção da Luz(30 de dano, + 5 de vida) - Cegue o inimigo e ganhe tempo")
    dano_fraco = input("Escolha seu dano fraco: ")
 
    # DANO "FORTE"
    print("[1] Lâmina Astuta(60 de dano) - Dê uma forte estocada no inimigo")
    print("[2] Raio Eterno(80 de dano, -50 de Mana) - Eletrecute o inimigo")
    print("[3] Fúria Ardente(50 de dano, +20 de vida) - Use sua raiva para lutar sem medo de se machucar!(porém você é meio fraco)")
    dano_forte = input("Escolha seu dano fraco: ")

    # escolher_item()

    with open('movimentos.json', 'r', encoding='utf-8') as dados_arquivo: # lê o Json
        dados_golpes = json.load(dados_arquivo)

    # DADOS GOLPE FRACO
    nome_golpe_fraco_escolhido = dados_golpes["GOLPE FRACO"][dano_fraco]["GOLPE"]
    dano_golpe_fraco = dados_golpes["GOLPE FRACO"][dano_fraco]["DANO"]
    menos_mana_fraco = dados_golpes["GOLPE FRACO"][dano_fraco]["MENOS_MANA"]
    mais_vida_fraco = dados_golpes["GOLPE FRACO"][dano_fraco]["MAIS_VIDA"]

    lista_set_fraco = [nome_golpe_fraco_escolhido, dano_golpe_fraco, mais_vida_fraco, menos_mana_fraco]

    # DADOS GOLPE FORTE
    nome_golpe_forte_escolhido = dados_golpes["GOLPE FORTE"][dano_forte]["GOLPE"]
    dano_golpe_forte = dados_golpes["GOLPE FORTE"][dano_forte]["DANO"]
    menos_mana_forte = dados_golpes["GOLPE FORTE"][dano_forte]["MENOS_MANA"]
    mais_vida_forte = dados_golpes["GOLPE FORTE"][dano_forte]["MAIS_VIDA"]

    lista_set_forte = [nome_golpe_forte_escolhido, dano_golpe_forte, mais_vida_forte, menos_mana_forte]

    return nome, lista_set_fraco, lista_set_forte

# Escolher item que irá auxiliar na batalha
# def escolher_item():
#     print("-"*100,"\nVocê pode escolher um entre estes três itens para te auxiliar na batalha")
#     print(f" [1] {Fore.LIGHTRED_EX}Espada Flamejante - Uma espada encantada com o poder do fogo, que aumenta o dano causado em batalhas.{Style.RESET_ALL}")
#     print(f" [2] {Fore.YELLOW}Amuleto da Vitalidade - Um amuleto que contém uma poderosa energia de cura, aumentando a vida do portador.{Style.RESET_ALL}")
#     print(f" [3] {Fore.LIGHTCYAN_EX}Anel da Ressureição - Um anel raro que concede ao usuário uma segunda chance de vida ao ser derrotado.{Style.RESET_ALL}")
    
#     while True:
#         item = input("Item n*: ")
#         if item in ["1", "2", "3"]:
#             return item
#         else:
#             print("Número de item inválido")

# Joga no "dado" para ver a efetividade do ataque do Personagem
def dadoPersonagem(dano, mov):
    num = random.randint(1, 5)
    
    if mov.upper() == 'Q':
        if num <= 2:
            print(f"Dado: {num} {Fore.RED}\nVocê errou!{Style.RESET_ALL}")
            return 0
        else:
            efet = 0.6 if num == 3 else 0.8 if num == 4 else 1
            dano_final = efet * dano
            print(f"Dado: {num} \nVocê deu {dano_final} de dano!") 
            return dano_final
    elif mov.upper() == 'W':
        if num <= 3:
            print(f"Dado: {num} {Fore.RED}\nVocê errou!{Style.RESET_ALL}")
            return 0
        else:
            efet = 0.7 if num == 4 else 1
            dano_final = efet * dano
            print("Dado: ", num, "\nVocê deu ", dano_final, " de dano!")
            return dano_final

# escolhe o movimento do personagem 
def movimento_personagem(nome, lista_set_fraco, lista_set_forte, vida_personagem, mana_personagem):
    nome_golpe_fraco = lista_set_fraco[0]
    nome_golpe_forte = lista_set_forte[0]

    dano_fraco = lista_set_fraco[1]
    dano_forte = lista_set_forte[1]

    mais_vida_fraco = lista_set_fraco[2]
    mais_vida_forte = lista_set_forte[2]

    menos_mana_fraco = lista_set_fraco[3]
    menos_mana_forte = lista_set_forte[3]
    print(f"Escolha sua ação: \n (Q) {nome_golpe_fraco}\n (W) {nome_golpe_forte}\n (E) Curar (+30hp)")
    mov = input()

    if mov.upper() == "Q": # validação se tem mana o suficiente e se a vida já está cheia
        print(f"{nome} escolheu {nome_golpe_fraco}")
        print(f"+ {mais_vida_fraco} de vida") if mais_vida_fraco > 0 else None
        print(f"- {menos_mana_fraco} de mana") if menos_mana_fraco > 0 else None
        dano =dadoPersonagem(dano_fraco, "Q")
        vida_personagem += mais_vida_fraco
        mana_personagem -= menos_mana_fraco
    elif mov.upper() == "W":
        print(f"{nome} escolheu {nome_golpe_forte}")
        print(f"+ {mais_vida_forte} de vida") if mais_vida_forte > 0 else None
        print(f"- {menos_mana_forte} de mana") if menos_mana_forte > 0 else None
        dano = dadoPersonagem(dano_forte, "W")
        vida_personagem += mais_vida_forte
        mana_personagem -= menos_mana_forte
    elif mov.upper() == "E":
        print(f"{nome} escolheu se curar!\n+30 de hp.")
        vida_personagem += 30

    return dano, vida_personagem, mana_personagem