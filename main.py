
#Web
import random
import numpy as np 

password = "Target123"
def cranker():
    wordlist = ["12345", "BobTring", "Elonload", "I LIKE BOB", "Password", "Target123", "Traget123", "Sus"]
    random_word = random.choice(wordlist)
    return random_word
cranker()
print(cranker())

def checker():
    password = "Target123"
    while cranker() != password:
        print("Password incorrect! Retrying")
        print("Trying:", cranker())
    
    print("Password Correct!")
    print("You can enter correct password", password)
checker()