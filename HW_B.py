#Bonus

import random

rate    = [   2,     3,    9,     7,   11]
symbols = ["🍒", "🍋", "⭐", "🔔", "💎"]
money = 50

print("=== SLOT MACHINE === \n")

while money > 0:
    print(f"money: {money}")
    index = random.randint(0,len(symbols)-1)

    choice=input("Enter your bet(or 'q' to quit): ")

    if choice == "q":
     break

    bet=int(choice)
    if bet<1 or bet>money:
        print("invalid bet!\n")
        continue

    spin=[random.randint(0,len(symbols)-1) for _ in range(3)]
    print(symbols[spin[0]],symbols[spin[1]],symbols[spin[2]])

    if spin[0]==spin[1]==spin[2]:
        r=rate[spin[0]]
        win=bet*777*r
        money+=win
        print(f"🔥 JACKPOT! You won {win}!\n")

    elif spin[0]==spin[1]or spin[0]==spin[2]:
        r=rate[spin[0]]
        win=bet*r
        money+=win
        print(f"✨ You got 2! You won{win}!\n")

    elif spin[1] == spin[2]:
        r=rate[spin[1]]
        win=bet*r
        money+=win
        print(f"✨ You got 2! You won{win}!\n")

    else:
        money-=bet
        print(f"💸 You lost!{bet}\n")

print("Game over! final money count:", money)

