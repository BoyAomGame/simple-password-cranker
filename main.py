import time
import random

#This function is used for using random word from wordlist.
def cranker():
    wordlist = ["12345", "BobTring", "Elonload", "I LIKE BOB", "Password", "Target123", "Traget123", "Sus"]
    random_word = random.choice(wordlist)
    return random_word
cranker()

#This function checking password from function Cranker
def checker():
    password = "Target123"
    while cranker() != password:
        print("Password incorrect! Retrying")
        print("Trying:", cranker())
        time.sleep(5)
    print("Password Correct!")
    print("Password that correct is ", password)
checker()