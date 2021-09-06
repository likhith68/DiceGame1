import random
n='y'
while n.lower()!='n':
    K=random.randint(1,6)
    print(K)
    n=input("Do you wanna roll the dice again??(y/n)")