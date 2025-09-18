import random 
def igra():
    chislo = random.randint(1,10)
    a = None
    while a != chislo:
        a = int(input("угадай число от 1 до 10:"))
        if a < chislo:
            print("больше") 
        elif a > chislo:
            print ("меньше")
        else:
            print("правильно")
igra()
