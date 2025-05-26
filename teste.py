import personagem as pg
nome = ""
lista_set_fraco = []
lista_set_forte = []

nome, lista_set_fraco, lista_set_forte = pg.create_caracter()

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

if mov.upper() == "Q":
    print(f"{nome} escolheu {nome_golpe_fraco}")
    print(f"+ {mais_vida_fraco} de vida") if mais_vida_fraco > 0 else None
    print(f"- {menos_mana_fraco} de mana") if menos_mana_fraco > 0 else None
elif mov.upper() == "W":
    print(f"{nome} escolheu {nome_golpe_forte}")
    print(f"+ {mais_vida_forte} de vida") if mais_vida_forte > 0 else None
    print(f"- {menos_mana_forte} de mana") if menos_mana_forte > 0 else None
elif mov.upper() == "E":
    print(f"{nome} escolheu se curar!\n+30 de hp.")

# roda dado
#retorna o dano

# Decide qual movimento o personagem vai usar
# def personagem(tempo, item=None):
#     dano = 50 if item == True else 0
#     msg = "Escolha a sua ação: \n- (X) Ataque fraco\n- (Y) Ataque forte\n- (A) Curar (+30hp)"
#     if tempo >= 3:
#         print(f"{msg}\n- {Fore.YELLOW}(B) Ataque especial{Style.RESET_ALL}\n")
#     else:
#         print(msg)
#     mov = input()
#     if mov.upper() == "X":
#         print("Você escolheu ataque fraco!")
#         dano += DANO_FRACO
#     elif mov.upper() == "Y":
#         print("Você escolheu ataque forte!")
#         dano += DANO_FORTE
#     elif mov.upper() == "B":
#         print(f"Você escolheu {Fore.YELLOW}ataque especial{Style.RESET_ALL}!") 
#         dano += DANO_ESPECIAL
#         tempo = 0
#     elif mov.upper() == "A":
#         print("Você escolheu se curar!\n+30 de hp")
#         return 1, tempo
#     else:
#         print("Movimento Errado!")

#     danos = pg.dadoPersonagem(dano, mov)
#     return danos, tempo