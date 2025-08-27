#basit quiz app 

from re import S
from tarfile import LENGTH_NAME


questions = {
     "math": {
        "soru": "15 + 20 ?",
        "cevap": "35"
    },
    "physical": {
        "soru": "Yerçekimi ivmesi yaklaşık kaç m/s^2’dir?",
        "cevap": "9.8"
    },
    "general": {
        "soru": "Dünyanın en büyük okyanusu hangisidir?",
        "cevap": "pasifik"
    }
    
}


def login():
    print("=== WELCOME TO THE QUESTIONS APP ===")
    while True:
        name = input("PLEASE WRITE YOUR USERNAME FOR START= ").strip().upper()
        if len(name) <= 2:
            print("YOUR NAME LENGHT NEED TO BE BIG 4 CHARACTER")
            continue
        else:
            print(f"{name} WE CAN START RIGHT NOW YOU NEED TO CHOOSE A CATEGORY")
            return name


def question(username):
    name = username
    print(f"{username} PLEASE CHOICE CATEGORY")
    print("1. MATH")
    print("2. PHYSICAL")
    print("3. GENERAL CULTURE")
    print("IF YOU WANT TO LEAVE PLEASE CHOICE 4")
    choice = input("CHOICE= ")
    while True:
        if choice == "1" :
            soru = questions["math"]["soru"]
            dogru = questions["math"]["cevap"]
            cevap = input(f"{soru} = ").strip()
            if dogru == cevap:
                print(f"CONGRULATION {username}")
                question(username)
            else:
                print("you need to check again")
                continue
        if choice == "2":
            soru = questions["physical"]["soru"]
            dogru = questions["physical"]["cevap"]
            cevap = input(f"{soru} = ").strip()
            if dogru == cevap:
                print(f"CONGRULATION {username}")
                question(username)
            else:
                print("you need to check again")
                continue
        if choice == "3":
            soru = questions["general"]["soru"]
            dogru = questions["general"]["cevap"]
            cevap = input(f"{soru} = ").strip()
            if dogru == cevap:
                print(f"CONGRULATION {username}")
                question(username)
            else:
                print("you need to check again")
                continue
        if choice == "4":
            print(f"SEE YOU LATER {username}")
            quit()

username = login()   # kullanıcı adı alınıyor
question(username)   # aynı kullanıcı adı gönderiliyor





    
