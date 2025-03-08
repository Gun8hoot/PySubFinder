import sys
from module.color import color

def arguments():
    count = 0
    wordlist = None
    url = None

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-u" or sys.argv[i] == "-U":
            url = sys.argv[count+1]

        elif sys.argv[i] == "-w" or sys.argv[i] == "-W":
            try:
                wordlist = sys.argv[count + 1]

            except IndexError:
                wordlist = None

        count = count + 1

    if url != None:
        return wordlist, url

    elif url == None:
        print(color.fr_red, "[!] You need to specify at least an URL", color.reset)
        sys.exit(0)