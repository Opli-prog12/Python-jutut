import random

print("🎲 Noppa Peli 🎲")

player_score = 0
computer_score = 0

for round in range(5):
    player_roll = int(input("Valitse oma nopan luku (1-6): "))
    computer_roll = random.randint(1, 6)

    print(f"Kierros {round+1}: Pelaaja {player_roll} vs Tietokone {computer_roll}")

    if player_roll > computer_roll:
        print("Pelaaja voitti kierroksen!\n")
        player_score += 1
    elif computer_roll > player_roll:
        print("Tietokone voitti kierroksen!\n")
        computer_score += 1
    else:
        print("Tasapeli!\n")

print("Lopputulos:")
print(f"Pelaaja: {player_score} | Tietokone: {computer_score}")
