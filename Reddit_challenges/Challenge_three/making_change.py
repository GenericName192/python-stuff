def change_giver(amount):
    coins = 0
    while amount >= 0:
        if amount >= 500:
            amount -= 500
            coins += 1
        elif amount >= 100:
            amount -= 100
            coins += 1
        elif amount >= 25:
            amount -= 25
            coins += 1
        elif amount >= 10:
            amount -= 10
            coins += 1
        elif amount >= 5:
            amount -= 5
            coins += 1
        elif amount >= 1:
            amount -= 1
            coins += 1
        else:
            return coins


print(change_giver(123456))