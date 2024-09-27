import requests
import random
import sys
import threading
import psutil
import os
import time

# =================================[PROXY]==========================================

def http():
    hit = []

    with open("proxies.txt", "r") as file:
        for line in file:
            hit.append(line.strip())

    hit = set(hit)
    hit = "\n".join(hit)
    return hit.split()

# =================================[DEF]==========================================

def http_start(link):
    global proxy_h, count, req_count
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

            time.sleep(1) # Add a short delay to avoid too many requests
            views_req = session.get("https://t.me/v/?views=" + _token)

            # Detailed logging
            print(f' [+] View Sent using proxy: {proxy}') 
            print(f'    Stats Code: {views_req.status_code}')
            print(f'    Request: {views_req.request.url}') # Show the full request URL
            print(f'    Response Text (partial): {views_req.text[:100]}...') # Show the beginning of the response text

            if views_req.status_code == 200: # Check for success
                req_count += 1
                proxy_h.remove(proxy) # Remove the proxy if successful
            else:
                print(f'    Error: {views_req.status_code}')
                print(f'    Response Text: {views_req.text}')

            time.sleep(5) # Add a delay between requests
        except Exception as e:
            print(f' [-] Proxy {proxy} failed: {e}')
            proxy_h.remove(proxy) # Remove the proxy if it fails
            time.sleep(1) # Wait a bit before trying again

# =================================[START]==========================================
try:
    count = sys.argv[3]
    req_count = 0
    link = sys.argv[1].strip().replace('https://', '').replace('http://', '')
    url_fin = f'https://{link}?embed=1'
    if sys.argv[2] == "http":
        proxy_h = http()
        for ii in range(600):
            threading.Thread(target=http_start,args=(url_fin,)).start()
except Exception as e:
    print(e)
    print("""Error . Help : python3 seen.py <link> <type> <count>
Types : http , socks4 , socks5 , mix
""")
