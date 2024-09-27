##
  # Github https://github.com/aDarkDev/Telegram-Seen
  # 
  # By aDarkDev
  # 
  # Telegram Seen
  # 
  # Python 3
##
import requests , random , sys , threading , psutil , os
#=================================[PROXY]==========================================

def http():
    hit = []
    try:
        zxcvv = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=http%2Chttps",timeout=8).json()["data"]
        for okeys in zxcvv:
            hit.append(okeys['ip']+":"+okeys['port'])
    except:
        pass

    proxy_urls = [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt",
        "https://openproxylist.xyz/http.txt",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
        "https://openproxy.space/list/http",
        "https://proxyspace.pro/http.txt",
        "https://proxyspace.pro/https.txt",
        "https://proxyhub.me/en/all-http-proxy-list.html",
        "https://proxyhub.me/en/all-https-proxy-list.html",
        "https://proxy-tools.com/proxy/http",
        "https://proxy-tools.com/proxy/https",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://www.proxy-list.download/api/v1/get?type=https",
        "https://www.proxyscan.io/download?type=http",
        "https://rootjazz.com/proxies/proxies.txt",
        "https://sheesh.rip/http.txt",
        "https://spys.me/proxy.txt",
        "https://proxysearcher.sourceforge.net/Proxy%20List.php?type=http",
        "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=http",
        "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=https",
        "https://cdn.jsdelivr.net/gh/aslisk/proxyhttps/https.txt",
        "https://cdn.jsdelivr.net/gh/clarketm/proxy-list/proxy-list-raw.txt",
        "https://cdn.jsdelivr.net/gh/hendrikbgr/Free-Proxy-Repo/proxy_list.txt",
        "https://cdn.jsdelivr.net/gh/jetkai/proxy-list/online-proxies/txt/proxies-http.txt",
        "https://cdn.jsdelivr.net/gh/mertguvencli/http-proxy-list/proxy-list/data.txt",
        "https://cdn.jsdelivr.net/gh/mmpx12/proxy-list/https.txt",
        "https://cdn.jsdelivr.net/gh/roosterkid/openproxylist/HTTPS_RAW.txt",
        "https://cdn.jsdelivr.net/gh/saschazesiger/Free-Proxies/proxies/http.txt",
        "https://cdn.jsdelivr.net/gh/ShiftyTR/Proxy-List/https.txt",
        "https://cdn.jsdelivr.net/gh/sunny9577/proxy-scraper/proxies.txt",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://raw.githubusercontent.com/themiralay/Proxy-List-World/master/data.txt",
        "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt",
        "https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt",
        "https://raw.githubusercontent.com/fahimscirex/proxybd/master/proxylist/http.txt",
        "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
        "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
        "https://raw.githubusercontent.com/im-razvan/proxy_list/main/http.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/generated/http_proxies.txt",
        "https://raw.githubusercontent.com/SevenworksDev/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/SevenworksDev/proxy-list/main/proxies/https.txt",
        "https://raw.githubusercontent.com/MrMarble/proxy-list/main/all.txt",
        "https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
        "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
        "https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/http.txt",
        "https://raw.githubusercontent.com/Tsprnay/Proxy-lists/master/proxies/https.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
        "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
        "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt"
        # Add more URLs here as needed
    ]

    for url in proxy_urls:
        try:
            response = requests.get(url, timeout=8)
            response.raise_for_status() # Raise an exception for bad status codes

            for proxy in response.text.splitlines():
                hit.append(proxy)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching proxies from {url}: {e}")

    hit = set(hit) # Remove duplicates after fetching
    hit = "\n".join(hit)
    return hit.split()

def socks4():
    hit = []
    try:
        zxcvv = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc&protocols=socks4",timeout=8).json()["data"]
        for okeys in zxcvv:
            hit.append(okeys['ip']+":"+okeys['port'])
    except:
        pass
    try:
        r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all", allow_redirects=True)
        r2 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4", allow_redirects=True)
        r3 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt", allow_redirects=True)
        for x1 in r.content.decode().replace("\r",'').split("\n"):
            hit.append(x1)
        for x3 in r2.content.decode().replace("\r",'').split("\n"):
            hit.append(x3)
        for x4 in r3.content.decode().replace("\r",'').split("\n"):
            hit.append(x4)
        
    except:
        r2 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4", allow_redirects=True)
        r3 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt", allow_redirects=True)
        for x3 in r2.content.decode().replace("\r",'').split("\n"):
            hit.append(x3)
        for x4 in r3.content.decode().replace("\r",'').split("\n"):
            hit.append(x4)
    hit = set(hit)
    hit = "\n".join(hit)
    return hit.split()

def socks5():
    hit = []
    try:
        zxcvv = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=50&page=1&sort_by=lastChecked&sort_type=desc&protocols=socks5",timeout=8).json()["data"]
        for okeys in zxcvv:
            hit.append(okeys['ip']+":"+okeys['port'])
    except:
        pass

    try:
        r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all", allow_redirects=True)
        r2 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5", allow_redirects=True)
        r3 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt", allow_redirects=True)
        for x1 in r.content.decode().replace("\r",'').split("\n"):
            hit.append(x1)
        for x3 in r2.content.decode().replace("\r",'').split("\n"):
            hit.append(x3)
        for x4 in r3.content.decode().replace("\r",'').split("\n"):
            hit.append(x4)
        
    except:
        r2 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5", allow_redirects=True)
        r3 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt", allow_redirects=True)
        for x3 in r2.content.decode().replace("\r",'').split("\n"):
            hit.append(x3)
        for x4 in r3.content.decode().replace("\r",'').split("\n"):
            hit.append(x4)
    hit = set(hit)
    hit = "\n".join(hit)
    return hit.split()

#=================================[DEF]==========================================

def socks4_start(link):
    global proxy_4, count, req_count
    while proxy_4 != []:
        if req_count >= int(count):
            p = psutil.Process(os.getpid())
            p.terminate()
        proxy = random.choice(proxy_4)
        try:
            session = requests.session()
            session.proxies.update({'http': f'socks4://{proxy}', 'https': f'socks4://{proxy}'})
            session.headers.update({
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
                })
            main_res = session.get(link)
            _token = main_res.text.split('data-view="')[1].split('"')[0]
            views_req = session.get("https://t.me/v/?views=" + _token)
            print(' [+] View Sent ' + 'Stats Code: '+str(views_req.status_code))
            proxy_4.remove(proxy)
            req_count += 1
        except:
            pass

def socks5_start(link):
    global proxy_5, count, req_count
    while proxy_5 != []:
        if req_count >= int(count):
            p = psutil.Process(os.getpid())
            p.terminate()
        proxy = random.choice(proxy_5)
        try:
            session = requests.session()
            session.proxies.update({'http': f'socks5://{proxy}', 'https': f'socks5://{proxy}'})
            session.headers.update({
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
                })
            main_res = session.get(link)
            _token = main_res.text.split('data-view="')[1].split('"')[0]
            views_req = session.get("https://t.me/v/?views=" + _token)
            print(' [+] View Sent ' + 'Stats Code: '+str(views_req.status_code))
            proxy_5.remove(proxy)
            req_count += 1
        except:
            pass

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
        
        
#=================================[START]==========================================
try:
    count = sys.argv[3]
    req_count = 0
    link = sys.argv[1].strip().replace('https://', '').replace('http://', '')
    url_fin = f'https://{link}?embed=1'
    if sys.argv[2] == "socks4":
        proxy_4 = socks4()
        for ii in range(600):
            threading.Thread(target=socks4_start,args=(url_fin,)).start()

    elif sys.argv[2] == "socks5":
        proxy_5 = socks5()
        for ii in range(600):
            threading.Thread(target=socks5_start,args=(url_fin,)).start()
    elif sys.argv[2] == "http":
        proxy_h = http()
        for ii in range(600):
            threading.Thread(target=http_start,args=(url_fin,)).start()
    elif sys.argv[2] == "mix":
        proxy_h = http()
        proxy_5 = socks5()
        proxy_4 = socks4()
        for ii in range(600):
            threading.Thread(target=http_start,args=(url_fin,)).start()
        for ii in range(600):
            threading.Thread(target=socks5_start,args=(url_fin,)).start()
        for ii in range(600):
            threading.Thread(target=socks4_start,args=(url_fin,)).start()
except Exception as e:
    print(e)
    print("""Error . Help : python3 seen.py <link> <type> <count>
Types : http , socks4 , socks5 , mix
""")


            
