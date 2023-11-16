import random

with open("poomismang\lemmad.txt", encoding="cp1252") as f:
    sõnad =  f.read().split('\n')
def joonista(katsed):
    faasid = [
        """
           -----
               |
               |
               |
               |
               |
        """,
        """
           -----
               |
           O   |
               |
               |
               |
        """,
        """
           -----
               |
           O   |
           |   |
               |
               |
        """,
        """
           -----
               |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
               |
           O   |
          /|\  |
               |
               |
        """,
        """
           -----
               |
           O   |
          /|\  |
          /    |
               |
        """,
        """
           -----
               |
           O   |
          /|\  |
          / \  |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        """
    ]
    print(faasid[7-katsed])

def new_game():
    katsed = 7
    sõna = sõnad[random.randint(0, len(sõnad)-1)]
    arvatud = []
    valed = []
    while katsed > 0:
        lüngad = "".join([täht if täht in arvatud else '_' for täht in sõna])
        joonista(katsed)
        print(f"Sõna: {lüngad}")
        print(f"Valed arvamised: {valed}")
        print(f"Valesid katseid järel: {katsed}")
        arvamus = input("Paku täht: ").casefold()
        if arvamus in sõna:
            arvatud.append(arvamus)
            if all(täht in arvatud for täht in sõna):
                print(f"Palju õnne! Sa arvasid sõna õieti ära. Sõna oli: {sõna}")
                return
        else:
            katsed -= 1
            valed.append(arvamus)

    print(f"Mäng läbi! Sõna oli: {sõna}")

new_game()
