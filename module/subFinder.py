#   SUBDOMAIN FINDER MODULE
from urllib.parse import urlparse, urlunparse
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from module.color import color
import sys, time,os

def finder(WL, URL):
    # Parse the URL
    try:
        LINK = []
        parsed_url = urlparse(URL)
        scheme = parsed_url.scheme  # https
        netloc = parsed_url.netloc  # domain.ext
        path = parsed_url.path
        print(f'{color.fr_yellow}[!] The script will test : {color.underline}{scheme}://SUB.{netloc}{color.reset}')
        with open(str(WL)) as f:
            WL = f.readlines()

        for lines in WL:
            URL = scheme+"://"+lines+"."+netloc
            URL = URL.replace('\n', '')
            try:
                with urlopen(URL, timeout=5):
                    print(f'{color.fr_green}[+] Subdomain found: {color.bold_on}{URL}{color.reset}')
                    


            except URLError or HTTPError:
                pass
        f.close()
        
    except KeyboardInterrupt:
        sys.exit()
        