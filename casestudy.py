import random
min_value=1
max_value=6
response="y"
while response=="y" or response=="yes":
    print(random.randint(min_value,max_value))
    response=input("Do you want to roll the dice again?")
