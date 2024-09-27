import requests
import random
import threading
import time
import sys

def load_proxies_from_file(filename):
    """Loads proxies from the specified file and fetches from websites listed."""
    try:
        with open(filename, "r") as file:
            proxy_urls = file.read().splitlines()

        proxies = []
        for url in proxy_urls:
            try:
                response = requests.get(url)
                response.raise_for_status()
                proxies.extend(response.text.splitlines())
            except requests.RequestException as e:
                print(f"Error fetching proxies from {url}: {e}")

        return proxies

    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return []

def send_views(link, proxy):
    """Sends views using the specified proxy."""
    session = requests.Session()
    session.proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}',
    }
    session.headers.update({
        'accept-language': 'en-US,en;q=0.9',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    })

    try:
        main_res = session.get(link)
        _token = main_res.text.split('data-view="')[1].split('"')[0]
        views_req = session.get("https://t.me/v/?views=" + _token)
        print(' [+] View Sent ' + 'Stats Code: ' + str(views_req.status_code))
        return True
    except Exception as e:
        print(f"Error sending view through proxy {proxy}: {e}")
        return False

if __name__ == "__main__":
    try:
        count = int(sys.argv[3]) # Number of views
        req_count = 0 # Sent requests counter
        link = sys.argv[1].strip().replace('https://', '').replace('http://', '')
        url_fin = f'https://{link}?embed=1'
        proxy_type = sys.argv[2].lower() # Proxy type (http, socks4, socks5)

        # Load proxies from your text files and fetch from websites listed
        proxies = load_proxies_from_file(f"{proxy_type}.txt")

        if not proxies:
            print(f"No proxies found in {proxy_type}.txt. Please check the file.")
            sys.exit(1)

        # Create threads for sending views
        while req_count < count:
            if proxies:
                proxy = random.choice(proxies)
                threading.Thread(target=send_views, args=(url_fin, proxy)).start()
                req_count += 1
                time.sleep(1) # Rate limiting
            else:
                print("No available proxies to use.")
                break

    except Exception as e:
        print(e)
        print("""Error. Help: python3 seen.py <link> <type> <count>
        Types: http, socks4, socks5
        """)
        
