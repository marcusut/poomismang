import random

with open("poomismang\lemmad.txt", encoding="ANSI") as f:
    sõnad =  f.read().split('\n')

def new_game():
    sõna = sõnad[random.randint(0, len(sõnad)-1)]
    lüngad = " _ " * len(sõna)
    print(lüngad)

new_game()