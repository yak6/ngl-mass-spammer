import requests
import threading
from colorama import Fore
from datetime import datetime
def check_user(username):
    r = requests.get(f"https://ngl.link/{username}")
    if r.status_code == 200 or r.status_code == 204:
        return True
    elif r.status_code == 404:
        return False
    else:
        return False
def load_users():
    with open("users2check.txt", "r", encoding="utf-8") as file:
        content = file.read().split()
    return content
def check_and_write(user, thread_id):
    if check_user(user) == True:
        valid_users.append(user)
    else:
        pass
point_a = datetime.now().timestamp() * 1000
valid_users = []
threads = []
users = load_users()
counter = 0

for user in users:
    counter += 1
    thread = threading.Thread(target=check_and_write, args=(user,counter))
    thread.start()
    print(f"Checking if {Fore.RED}{user}{Fore.RESET} is valid...")
    threads.append(thread)
for thread in threads:
    thread.join()
for user in valid_users:
    with open("valid-users.txt", "a", encoding="utf-8") as file:
        file.write(user+"\n")
point_b = datetime.now().timestamp() * 1000
print(f"Valid users has been added to the valid list. It took {Fore.RED}{round(point_b-point_a)}{Fore.RESET} ms to check. ")
