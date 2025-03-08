import os,sys,time
from module.color import color

def wordlist(file):
    WL_TAR = None
    WL_FILE = None

    if file == None:
        choise = input(f"{color.fr_orange}[!] You haven't chosen a wordlist, do you want to use the basic one? (Y/n) : {color.reset}")
        if choise == "n" or choise == "N":
            print("[!] Abording ...")
            sys.exit()

        elif choise == "y" or choise == "Y":
            for x in os.listdir():
                if x.endswith('.tar') or x.endswith('.tar.gz') or x.endswith('.zip') or x.endswith('.rar'):
                    WL_TAR = x
                    
                elif x.endswith('.txt') and x != "requirements.txt":
                    WL_FILE = x

                elif WL_FILE != None:
                    break

            if WL_FILE != None:
                return WL_FILE

            elif WL_TAR != None:
                TAR = os.system("tar -xvf ./subdomains_WL.tar 2>/dev/null")
                if TAR == 0:
                    return WL_FILE

                elif TAR == 512:
                    print("[!] Default wordlist is not on the folder. Use python ./main.py -u/-U [URL] -w/-W [WORDLIST]")
                    sys.exit()

                else: 
                    print('ERROR')

                    
    elif file != None:
        return file

