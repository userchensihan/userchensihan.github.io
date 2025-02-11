import requests
from stem import Signal
from stem.control import Controller
url="https://check.torproject.org"
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from bs4 import BeautifulSoup 
proxies = {'https':'socks5h://127.0.0.1:9150'}
while True:
        try:
            c=Controller.from_port()
            c.authenticate()
            c.signal(Signal.NEWNYM)
            r = requests.get(url=url, proxies=proxies,verify=False).text
            print(BeautifulSoup(r,'lxml').strong.string)
        except KeyboardInterrupt:
            print('Control-C')
            break
