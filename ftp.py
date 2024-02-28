#!/usr/bin/env python3

import os
import re
import sys
import time
import argparse
import requests
from urllib import parse
from datetime import datetime

def process_cli():
    parser = argparse.ArgumentParser(
        description="""THIS'S SIMPLE SCRIPT TO TEST PROXY SERVER CONNECTION.
        GET PROXY FROM WEBSITE.""",
        usage='%(prog)s [-h][-v][-nb] -f FILE',
        epilog="(c) ALPHA4D (Biplob SD) 2019, e-mail: biplobsd11@gmail.com",
        add_help=False
    )
    parent_group = parser.add_argument_group(
        title="Options"
    )
    parent_group.add_argument(
        "-h",
        "--help",
        action="help",
        help="Help"
    )
    parent_group.add_argument(
        "-v",
        "--version",
        action="version",
        help="Display the version number",
        version="%(prog)s version: 1.1.0"
    )
    parent_group.add_argument(
        "-f",
        "--file",
        help="Proxy list file. (default is proxys.txt)",
        metavar="FILE"
    )
    parent_group.add_argument(
        "-nb",
        "--no-banner",
        action="store_true",
        default=False,
        help="Do not print banner (default is False)"
    )
    return parser

def inputdata(filename):
    if not os.path.exists('proxys.txt'):
        open('proxys.txt', 'a+', encoding="utf-8").close()

    with open(filename, 'r+', encoding="utf-8") as handle:
        htmlRO = handle.read()

    x = re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}[\s:\t][0-9]{1,5}", htmlRO)
    for line in range(len(x)):
        x[line] = re.sub(r'[\s]', ':', x[line])

    with open('proxys.txt', 'w+', encoding="utf-8") as p:
        for line in x:
            p.write(line+'\n')
    return x

def test_proxies(proxy_list, urls):
    working_proxies = []

    for url in urls:
        print(f"\nTesting proxies for URL: {url}")
        for proxy in proxy_list:
            proxy_ip = proxy.strip()
            proxies = {
                'http': f'http://{proxy_ip}',
                'https': f'http://{proxy_ip}'
            }
            try:
                response = requests.get(url, proxies=proxies, timeout=5)
                if response.status_code == 200:
                    working_proxies.append((proxy_ip, url))
            except requests.RequestException:
                pass

    return working_proxies

def save_working_proxies(working_proxies, filename):
    with open(filename, 'w+') as w:
        w.write(f"{time.strftime('%X %x %Z')} | Checked proxies for URLs\n")
        for proxy_ip, url in working_proxies:
            w.write(f"Proxy: {proxy_ip} | URL: {url}\n")
        print(f"\nWorking proxies saved to {filename}")

if __name__ == "__main__":
    parser = process_cli()
    NAMESPACE = parser.parse_args(sys.argv[1:])
    proxyslistname = 'proxys.txt'
    if NAMESPACE.file:
        proxyslistname = NAMESPACE.file
    proxyslist = inputdata(proxyslistname)
    banner = r"""
                                _____                     _ _______        _
                                / ____|                   | |__   __|      | |
    _ __  _ __ _____  ___   _| (___  _ __   ___  ___  __| |  | | ___  ___| |_
    | '_ \| '__/ _ \ \/ / | | |\___ \| '_ \ / _ \/ _ \/ _` |  | |/ _ \/ __| __|
    | |_) | | | (_) >  <| |_| |____) | |_) |  __/  __/ (_| |  | |  __/\__ \ |_
    | .__/|_|  \___/_/\_\\__,  |_____/| .__/ \___|\___|\__,_|  |_|\___||___/\__|
    | |                   __/ |      | |
    |_|                  |___/       |_|                       -dev-by-Alpha4d-
    """

    if NAMESPACE.no_banner:
        banner = ""

    print(banner)
    print(f'{len(proxyslist)} proxy ip:port found!')

    # Add the URLs to test with proxies
    urls = [
"http://circleftp.net/",
"http://fs.ebox.live/",
"http://movie.sambd.net/",
"http://ftpbd.net/",
"http://crazyctg.com/",
"http://showtimebd.com/",
"http://tv.tajpata.com/",
"http://naturalbd.com/",
"https://elaach.com/",
"https://www.dhakaftp.com/",
"http://dhakamovie.com/",
"http://funtimebd.com/",
"http://media.dfnbd.net/",
"http://ftpbd.net/",
"http://10.16.100.244/",
"http://172.16.50.9/SAM-FTP-1/",
"http://ftp4.circleftp.net/",
"http://dflix.live/",
"http://fs2.amrbd.com/",
"http://fs.plus.net.bd",
"http://discoveryftp.net/",
"http://server3.ftpbd.net/",
"http://server5.ftpbd.net",
"http://Iplex.live",
"https://ftp1.aliflailabd.com/",
"http://cdn.dflix.live/Movies",
"http://172.16.50.3/",
"http://172.16.50.4/",
"http://172.16.50.7/",
"http://new.circleftp.net/",
    # ... (add the rest of your URLs)
]
    # Test proxies for the URLs
    working_proxies = test_proxies(proxyslist, urls)

    # Save working proxies to a file
    save_working_proxies(working_proxies, 'working_proxies.txt')
