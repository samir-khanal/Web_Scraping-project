import os
try:
    from config import APP_USERNAME, APP_PASSWORD
except ImportError:
    APP_USERNAME = os.environ.get("APP_USERNAME", "default_user")
    APP_PASSWORD = os.environ.get("APP_PASSWORD", "default_pass")
def authenticate():

    print("HEY! Welcome to my program,\nHere you can search for the information of any Football players you want!!!!")
    attempts=3
    while attempts > 0:
        username=input("ENTER USERNAME:").strip().lower()
        password=input("ENTER PASSWORD:").strip()

        if username == APP_USERNAME and password == APP_PASSWORD:
            print("...Access Granted!!...")
            return True
        else:
            attempts -= 1
            print(f"Wrong username or password.You have {attempts} Tries Left!!\n")

    print("Access Denied!!....Exiting the Program....") 
    return False       
