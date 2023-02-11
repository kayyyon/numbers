import random
n = random.randrange(1,10)
guess = int(input("Введите любое число: ")) #!
while n!= guess:
    if guess < n:
        print("Загаданное число больше!")
        guess = int(input("Введите число снова: "))
    elif guess > n:
        print("Загаданное число меньше!")
        guess = int(input("Введите число снова: "))
    else:
      break
print("Вы угадали!!")