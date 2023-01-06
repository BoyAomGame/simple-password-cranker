#จินตนการว่าอันนี้คือเว็บที่ต้องการ password

password = "Target123"

def login():
    login = input("Please enter password!:")   
login() 

if login == password:
    print("Password Correct")
else:
    print("Password incorrect!(Ctrl+C To Exit)")
    login()