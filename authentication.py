def authenticate():
    #Correct username and password
    USERNAME="player"
    PASSWORD="goal!" 

    print("HEY! Welcome to my program,\nHere you can search for the information of any Football players you want!!!!")
    attempts=3
    while attempts > 0:
        username=input("ENTER USERNAME:").strip().lower()
        password=input("ENTER PASSWORD:").strip()

        if username == USERNAME and password == PASSWORD:
            print("...Access Granted!!...")
            return True
        else:
            attempts -= 1
            print(f"Wrong username or password.You have {attempts} Tries Left!!\n")

    print("Access Denied!!....Exiting the Program....") 
    return False       
