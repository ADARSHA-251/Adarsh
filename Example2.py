import random
num=random.randint(1,10)
guess=int(input("Guess a number from 1 to 10:"))
print(num,guess)
if (num==guess):
    print("you are correct")
else:
    print("you are not correct")
