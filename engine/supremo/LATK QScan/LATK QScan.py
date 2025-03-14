from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os 
import time
from colorama import *
import re
import sys
import time
import requests

#   ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗ ██╗     ███████╗
#  ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║     ██╔════╝
#  ██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     ███████╗
#  ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║     ╚════██║
#  ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗███████║
#   ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝                                                                
#                                                                    Section 2.0


init(autoreset=True)
cwd = str.replace(os.getcwd(),'\\','/')
with open(r''+cwd + "/QScan Websites.txt","r") as fd:    # Change notepad to read from here if required.
    Websites = fd.read().splitlines()
    
def QScan():                                               # FUNCTION - Start the extraction process.
    Checkedn = 0
    for url in Websites:                                                            # Loop through supplied .txt file
        if url[:4] != 'http': url = 'https://' + url
        try:                                                                        # Try GET request. If successful..
            response = requests.get(url).status_code
            print(response)
        except:
            pass
        Checkedn = Checkedn + 1                                                     # Completion counter
        sys.stdout.write(Fore.MAGENTA + '\r'+str(Checkedn) + ' / ' 
                         + str(len(Websites)) +Fore.WHITE + ' === ' 
                         + Fore.GREEN + str(url).upper() 
                         + Fore.WHITE + ' === ' 
                         + Fore.YELLOW + "{0:.0%}".format( Checkedn / len(Websites))) 
        sys.stdout.flush()                                                                  # I use sys.stdout write/flush to send messages to the console..
        sys.stdout.write('                                                              ')  # that overwrite themselves, rather than spamming (verbose)

def PrintSplash():                                               # FUNCTION - LATK Splash
    print(Fore.MAGENTA + """
    #######################################################
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #       """+Fore.WHITE+"""             LATK QSCan  """+Fore.MAGENTA+"""                     #
    #      """+Fore.WHITE+"""          BY LA-TK FOR DTO-TK    """+Fore.MAGENTA+"""              #
    #                                                     #
    #      """+Fore.WHITE+"""         DECEMBER 2019 BUILD 1  """+Fore.MAGENTA+"""               #
    #                                                     #
    #        S U C C U M B   T O   T H E   V O I D        #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #######################################################  
    """) 

def ContinueCheck(q):                                            # FUNCTION - Confirm start
    while "the answer is invalid":
        reply = str(input(q + Fore.WHITE + ' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            print(Fore.MAGENTA + 'Execution cancelled.')
            sys.exit(0)
            return False

# Section 4 - Start and run
PrintSplash()                                                                      # Call PrintSplash function (1.1)
ContinueCheck(Fore.MAGENTA + 'Are you sure you want to run this?')                 # Confirm program start.
QScan()                                                                      # Start the program.
print(Fore.GREEN + '\nExtraction complete.')                                       # Finish line.
