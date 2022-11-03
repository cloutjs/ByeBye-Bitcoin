import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import time
import os
import threading
import random

threads = 0
checked = 0

useproxys = True

with open("configs.txt", "r") as cfgs:
    useproxys = bool(cfgs.read())

try:
    threads = int(input("How many threads do you want to use?: "))
except Exception:
    print("Invalid answer. Try again.")
    try:
        threads = int(input("How many threads do you want to use?: "))
    except Exception:
        print("Invalid answer. Using 1 thread.")
        threads = 1

url = "https://www.bitcoinlist.io/random"
proxie_type = "socks5"
print("reading proxies")
proxies = open("proxies.txt").read().splitlines()
print("done reading proxies")


def process():
    global checked

    while True:
        os.system(f"title Bye Bye Bitcoin // Checked Wallets: {checked} // by clout")
        headers = CaseInsensitiveDict()
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
        if useproxys:
            req = requests.get(url, headers=headers, proxies={f"{proxie_type}": f'{proxie_type}://' + random.choice(proxies)})
        else:
            req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        wallets = soup.find_all("tr")
        for wallet in wallets:
            getwallet = str(wallet.getText()).strip()
            privkey = getwallet.split()[0].strip()
            uncompaddy = getwallet.split()[1].strip()
            compaddy = getwallet.split()[2].strip()
            balance = getwallet.split()[3].strip()
            if "Private Key" in getwallet:
                pass
            else:
                checked += 1
                if float(balance) > 0:              
                    #requests.post("webhook URL", json={"content": f"{balance} BTC found\n\nAdress: {compaddy}\nPrivate Key: {privkey}"}) 
                    open('hits.txt', 'a+').write(f"{balance} BTC found in Adress: {compaddy} // Private Key: {privkey}")
                os.system("cls")
                os.system(f"title Bye Bye Bitcoin // Checked Wallets: {checked} // by clout")
                print(f"""
                .-.____________________.-.
         ___ _.' .-----.    _____________|======+--------------------+
        /_._/   (      |   /_____________|      |   Bye Bye Bitcoin  |
          /      `  _ ____/                     |      by clout      |
         |_      .\( \\                          |____________________|
        .'  `-._/__`_//
      .'       |'           Private Key: {privkey}
     /        /             Uncompressed Address: {uncompaddy}
    /        |              Compressed Address: {compaddy}
    |        '              Balance: {balance}
    |        |
    `-._____.-'""")
            time.sleep(0.5)


if __name__ == "__main__":
    for _ in range(threads):
        x = threading.Thread(target=process)
        x.start()
    
