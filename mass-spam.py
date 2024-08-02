import random
import string
import requests
import threading
from colorama import Fore, Back
from datetime import datetime
def deviceId():
    characters = string.ascii_lowercase + string.digits
    part1 = ''.join(random.choices(characters, k=8))
    part2 = ''.join(random.choices(characters, k=4))
    part3 = ''.join(random.choices(characters, k=4))
    part4 = ''.join(random.choices(characters, k=4))
    part5 = ''.join(random.choices(characters, k=12))
    device_id = f"{part1}-{part2}-{part3}-{part4}-{part5}"
    return device_id
def UserAgent():
    with open('user-agents.txt', 'r') as file:
        user_agents = file.readlines()
        random_user_agent = random.choice(user_agents).strip()
        return random_user_agent
def random_message():
    with open("words.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
    return random.choice(content).strip()
def get_users():
    users = []
    with open("users.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
    for line in content:
        users.append(line.strip())
    return users
users = get_users()
def send(thread_id, user):
    message = random_message()
    device = deviceId()
    headers = {
                'Host': 'ngl.link',
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'accept': '*/*',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-requested-with': 'XMLHttpRequest',
                'sec-ch-ua-mobile': '?0',
                'user-agent': f'{UserAgent()}',
                'sec-ch-ua-platform': '"Windows"',
                'origin': 'https://ngl.link',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-dest': 'empty',
                'referer': f'https://ngl.link/{user}',
                'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
            }
    data = {
                'username': f'{user}',
                'question': f'{message}',
                'deviceId': f'{device}',
                'gameSlug': '',
                'referrer': '',
            }
    response = requests.post('https://ngl.link/api/submit', headers=headers, data=data)
threads = []
THREAD_COUNTER = 0
a = datetime.now().timestamp() * 1000
for user in users:
    THREAD_COUNTER += 1
    thread = threading.Thread(target=send, args=(THREAD_COUNTER,user))
    thread.start()
    print(f"Thread started for: {Fore.RED}{user}{Fore.RESET} | Thread Id: {Fore.RED}{THREAD_COUNTER}{Fore.RESET}")
    threads.append(thread)
for thread in threads:
    thread.join()
b = datetime.now().timestamp() * 1000 
took = round(b-a)
print(f"Finished | Took: {Fore.RED}{took}{Fore.RESET} ms | Started threads: {Fore.RED}{THREAD_COUNTER}{Fore.RESET}")
