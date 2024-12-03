coke1 = 50
ch = 0
coins = [25 , 10 , 5]

while coke1 > 0:
    print("Amount Due: " + str(coke1))
    user_input = int(input("Insert Coin: "))
    if user_input in coins:
        coke1 = coke1 - user_input
        ch = ch + user_input

if ch >= coke1:
    print("Change Owed: " + str(ch - 50))