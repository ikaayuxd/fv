import requests
import random
import sys
import threading
import psutil
import os

def get_proxies_from_files(file_list):
    proxies = set()

    for filename in file_list:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    response = requests.get(line)
                    if response.status_code == 200:
                        proxies.update(response.text.split('\n'))

    return list(proxies)

def http_start(link, proxies):
    global count, req_count
    while proxies:
        if req_count >= int(count):
            p = psutil.Process(os.getpid())
            p.terminate()
        proxy = random.choice(proxies)
        try:
            session = requests.session()
            session.proxies.update({'http': f'http://{proxy}', 'https': f'http://{proxy}'})
            main_res = session.get(link)
            _token = main_res.text.split('data-view="')[1].split('"')[0]
            views_req = session.get(f"https://t.me/v/?views={_token}")
            print('[+] View Sent. Status Code: ' + str(views_req.status_code))
            proxies.remove(proxy)
            req_count += 1
        except Exception as e:
            print(f"Error: {e}")
            pass

def socks4_start(link, proxies):
    global count, req_count
    while proxies:
        if req_count >= int(count):
            p = psutil.Process(os.getpid())
            p.terminate()
        proxy = random.choice(proxies)
        try:
            session = requests.session()
            session.proxies.update({'http': f'socks4://{proxy}', 'https': f'socks4://{proxy}'})
            main_res = session.get(link)
            _token = main_res.text.split('data-view="')[1].split('"')[0]
            views_req = session.get(f"https://t.me/v/?views={_token}")
            print('[+] View Sent. Status Code: ' + str(views_req.status_code))
            proxies.remove(proxy)
            req_count += 1
        except Exception as e:
            print(f"Error: {e}")
            pass

def socks5_start(link, proxies):
    global count, req_count
    while proxies:
        if req_count >= int(count):
            p = psutil.Process(os.getpid())
            p.terminate()
        proxy = random.choice(proxies)
        try:
            session = requests.session()
            session.proxies.update({'http': f'socks5://{proxy}', 'https': f'socks5://{proxy}'})
            main_res = session.get(link)
            _token = main_res.text.split('data-view="')[1].split('"')[0]
            views_req = session.get(f"https://t.me/v/?views={_token}")
            print('[+] View Sent. Status Code: ' + str(views_req.status_code))
            proxies.remove(proxy)
            req_count += 1
        except Exception as e:
            print(f"Error: {e}")
            pass

if __name__ == "__main__":
    try:
        count = sys.argv[3]
        req_count = 0
        link = sys.argv[1].strip().replace('https://', '').replace('http://', '')
        url_fin = f'https://{link}?embed=1'

        files = ['http.txt', 'socks4.txt', 'socks5.txt']  # Replace with your file names

        proxies = get_proxies_from_files(files)

        for _ in range(200):
            threading.Thread(target=http_start, args=(url_fin, proxies.copy())).start()
            threading.Thread(target=socks4_start, args=(url_fin, proxies.copy())).start()
            threading.Thread(target=socks5_start, args=(url_fin, proxies.copy())).start()

    except Exception as e:
        print(f"Error: {e}")
        print("Error. Usage: python3 seen.py <link> <type> <count>")
        print("Types: http, socks4, socks5, mix")
