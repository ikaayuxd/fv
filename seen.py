import requests
import random
import sys
import threading
import psutil
import os

def read_proxies_from_file(file_path):
    with open(file_path, 'r') as file:
        proxies = [line.strip() for line in file]
    return set(proxies)

def http_start(link):
    global proxy_h , count , req_count
    while proxy_h != []:
        if req_count >= int(count):
            p = psutil.Process(os.getpid())
            p.terminate()
        proxy = random.choice(proxy_h)
        try:
            session = requests.session()
            session.proxies.update({'http': f'http://{proxy}', 'https': f'http://{proxy}'})
            session.headers.update({
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
                })
            main_res = session.get(link)
            _token = main_res.text.split('data-view="')[1].split('"')[0]
            views_req = session.get("https://t.me/v/?views=" + _token)
            print(' [+] View Sent ' + 'Stats Code: '+str(views_req.status_code))
            proxy_h.remove(proxy)
            req_count += 1
        except:
            pass

try:
    count = sys.argv[3]
    req_count = 0
    link = sys.argv[1].strip().replace('https://', '').replace('http://', '')
    url_fin = f'https://{link}?embed=1'

    if sys.argv[2] == "file":
        proxies = read_proxies_from_file('proxies.txt')
        for ii in range(600):
            threading.Thread(target=http_start, args=(url_fin, proxies)).start()

except Exception as e:
    print(e)
    print("Error. Help: python3 seen.py <link> file <count>")
