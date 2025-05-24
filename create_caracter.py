import json
# usar mana
# usar dado ainda
DANO_FRACO = ""
DANO_FORTE = ""

print("CRIE SEU PERSONAGEM")
nome = input("Nome: ")
print("ESCOLHA AS SUAS HABILIDADES(APENAS DUAS):")

# DANO "FRACO"
print("[1] Corte Veloz(40 de dano) - Dê um corte rápido no inimigo")
print("[2] Rajada Gelada(50 de dano, - 20 de Mana) - Lance uma forte rajada de gelo no inimigo")
print("[3] Benção da Luz(30 de dano, + 20 de vida) - Cegue o inimigo e ganhe tempo")
dano_fraco = input("Escolha seu dano fraco: ")

# DANO "FORTE"
print("[1] Lâmina Astuta(60 de dano) - Dê uma forte estocada no inimigo")
print("[2] Raio eterno(80 de dano, -50 de Mana) - Eletrecute o inimigo")
print("[3]Fúria Ardente(50 de dano, +50 de vida) - Use sua raiva para lutar sem medo de se machucar!(porém você é meio fraco)")

with open('movimentos.json', 'r', encoding='utf-8') as dados_arquivo: # lê o Json
    dados_golpes = json.load(dados_arquivo)

print(dados_golpes['GOLPE FRACO 1'])


dano_fraco = 'GOLPE FRACO ' + dano_fraco
print(dano_fraco)
