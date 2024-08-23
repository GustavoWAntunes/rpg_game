import random

# constants
WEAK_DAMAGE = 40
STRONG_DAMAGE = 60
SPECIAL_DAMAGE = 100
ACID_BLOW_DAMAGE = 60
BLACK_FLAMES_DAMAGE = 75
CHARACTER_HEALTH = 200
DRAGON_HEALTH = 300
HEAL = 30

# Decide which move the character will use
def character(time, item=None):
    damage = 50 if item else 0
    if time >= 3:
        print("Choose your action: \n- (X) Weak Attack\n- (Y) Strong Attack\n- (B) Special Attack\n- (A) Heal")
    else:
        print("Choose your action: \n- (X) Weak Attack\n- (Y) Strong Attack\n- (A) Heal")
    move = input()
    if move.upper() == "X":
        print("You chose a weak attack!")
        damage += WEAK_DAMAGE
    elif move.upper() == "Y":
        print("You chose a strong attack!")
        damage += STRONG_DAMAGE
    elif move.upper() == "B":
        print("You chose a special attack!")
        damage += SPECIAL_DAMAGE
        time = 0
    elif move.upper() == "A":
        print("You chose to heal!\n+30 hp")
        return 1, time
    else:
        print("Wrong move!")

    damages = characterDice(damage, move)
    return damages, time

# Decide which move the Dragon will use
def enemyDragon():
    print("The Dragon is going to attack")
    move = random.randint(1, 2)
    damage = 0
    if move == 1:
        print("The Shadow Dragon uses Acid Blow")
        damage = ACID_BLOW_DAMAGE
    elif move == 2:
        damage = BLACK_FLAMES_DAMAGE
        print("The Shadow Dragon uses Black Flames Explosion")

    final_damage = dragonDice(damage)
    return final_damage

# Roll the "dice" to see the effectiveness of the Dragon's attack
def dragonDice(damage):
    num = random.randint(1, 5)
    if num <= 2:
        print("Roll: ", num, "\nThe Dragon missed!")
        return 0
    else:
        effectiveness = 0.6 if num == 3 else 0.8 if num == 4 else 1
        final_damage = effectiveness * damage
        print("Roll: ", num, "\nThe Dragon hit you!", "\nDamage: ", final_damage)
        return final_damage

# Print enemy description
def describeEnemy():
    print("The Shadow Dragon approaches")
    print("  The Shadow Dragon is a terrifying creature that inhabits the depths of the darkest and most forgotten caves. \n  Its colossal body is covered in black scales that absorb light, making it nearly invisible in the shadows.\n  Its red eyes glow with a malevolent intelligence and an insatiable thirst for power.")

# Validate lives to find a winner
def death(health, enemyHealth):
    if health <= 0:
        print("You died")
        return True
    if enemyHealth <= 0:
        print("You defeated the dragon!")
        return True
    return False

# Roll the "dice" to see the effectiveness of the Character's attack
def characterDice(damage, move):
    num = random.randint(1, 5)
    
    if move.upper() == 'X':
        if num <= 2:
            print("Roll: ", num, "\nYou missed!")
            return 0
        else:
            effectiveness = 0.6 if num == 3 else 0.8 if num == 4 else 1
            final_damage = effectiveness * damage
            print("Roll: ", num, "\nYou dealt ", final_damage, " damage!") 
            return final_damage
    elif move.upper() == 'Y':
        if num <= 3:
            print("Roll: ", num, "\nYou missed!")
            return 0
        else:
            effectiveness = 0.7 if num == 4 else 1
            final_damage = effectiveness * damage
            print("Roll: ", num, "\nYou dealt ", final_damage, " damage!") 
            return final_damage
    else:
            effectiveness = 0.5 if num in [1, 2, 3] else 0.7 if num == 4 else 1
            final_damage = effectiveness * damage
            print("Roll: ", num, "\nYou dealt ", final_damage, " damage!") 
            return final_damage

# Prints the "menu" with the characters' lives
def healthMenu(health, enemyHealth):
    print("_"*34)
    print("| Your health: ", health, " "*15,"| ", 
            "\n| Shadow Dragon's health: ", enemyHealth, " |")
    print("-"*34)

# Choose an item that will help in battle
def choose_item():
    print("-"*100,"\nYou can choose one of these three items to aid you in battle")
    print(" Flaming Sword - A sword enchanted with the power of fire, increasing the damage dealt in battles. (1)",
          "\n Amulet of Vitality - An amulet that contains a powerful healing energy, increasing the bearer's health. (2)",
          "\n Resurrection Ring - A rare ring that grants the user a second chance at life upon defeat. (3)")
    while True:
        item = input("Item number: ")
        if item in ["1", "2", "3"]:
            return item
        else:
            print("Invalid item number")

# Where will the other methods be called?
def main():
    end = False
    health = CHARACTER_HEALTH
    enemyHealth = DRAGON_HEALTH
    time = 0
    describeEnemy()
    item = choose_item()

    if item == "2":
        health += 100

    while end == False:
        healthMenu(health, enemyHealth)
        if item == "1":
            damage, time_passed = character(time, True)
            time = time_passed + 1
        else:
            damage, time_passed = character(time)
            time = time_passed + 1
        if damage == 1:
            health += HEAL
            healthMenu(health, enemyHealth)
        else:
            enemyHealth -= damage
            healthMenu(health, enemyHealth)
            end = death(health, enemyHealth)
            if end == True:
                break
            
        dragon_damage = enemyDragon()
        health -= dragon_damage
        end = death(health, enemyHealth)

        if end == True and item == "3":
            print("You used your Resurrection Ring")
            health = 80
            item = None
            end = False

    print("Game Over")

# "Game" start menu
if __name__ == "__main__":
    while True:
        print("=" * 100)
        print("Start: P", "\nExit: S")
        option = input("Option: ").upper()
        print("-" * 100)
        if option == "P":
            main()
        elif option == "S":
            break