import os,sys
from module.arguments import arguments
from module.wordlist import wordlist
from module.subFinder import finder
from module.color import color

def main():
    with open("./other/banner.txt", 'r') as b:
        banner = b.read()
    b.close()   
    print(color.fr_purple, banner, color.reset, '\n')
    WL_PATH, URL = arguments()
    WL_NAME = wordlist(WL_PATH)
    finder(WL_NAME, URL)

    
if __name__ == '__main__':
    main()