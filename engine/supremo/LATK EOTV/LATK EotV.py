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
ChrDrvLoc = (cwd + '/driver/chromedriver.exe')         # Dynamic driver - place within folder rather than edit code. Or use below [ Method 1 ]
chrome_options = Options()
chrome_options.add_experimental_option("detach", False)
chrome_options.add_argument("--headless")
chrome_options.add_argument('log-level=3')
chrome_options.add_argument("--window-size=%s" % "1920,1080")
driver = webdriver.Chrome(executable_path=r''+ChrDrvLoc,chrome_options=chrome_options)
#driver = webdriver.Chrome(executable_path=r'C:\Users\Luke\Desktop\Python Projects\Utilities\chromedriver.exe',chrome_options=chrome_options) - [ Method 1 ]
OutputFile = (cwd + '/Screens/')                       # Change output screenshot directory here if required.
with open(r''+cwd + "/EotVWebsites.txt","r") as fd:    # Change notepad to read from here if required.
    Websites = fd.read().splitlines()
    
def GrabScreens():                                               # FUNCTION - Start the extraction process.
    Checkedn = 0
    for url in Websites:                                                            # Loop through supplied .txt file
        if url[:4] != 'http': url = 'https://' + url
        try:                                                                        # Try GET request. If successful..
            driver.get(url)
            driver.save_screenshot(OutputFile +                                     # Save file and..
                                FormatURL(str.replace(
                                    str.replace(url,r'/','_'),'.','_')              # Refer below Formatting FUNCTION
                                    )
                                + ' ' + time.strftime("%Y%m%d-%H%M%S") + '.png')
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
    driver.close()

def FormatURL(s):                                                # FUNCTION - Formatting of URL's into file names (we don't like slashes..)
    s = re.sub(r"[^\w\s]", '', s)
    s = re.sub(r"\s+", '-', s)
    return s

def PrintSplash():                                               # FUNCTION - LATK Splash
    print(Fore.MAGENTA + """
    #######################################################
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #       """+Fore.WHITE+"""              LATK EotV  """+Fore.MAGENTA+"""                     #
    #      """+Fore.WHITE+"""          BY LA-TK FOR DTO-TK    """+Fore.MAGENTA+"""              #
    #                                                     #
    #      """+Fore.WHITE+"""         DECEMBER 2019 BUILD 4  """+Fore.MAGENTA+"""               #
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
GrabScreens()                                                                      # Start the program.
print(Fore.GREEN + '\nExtraction complete.')                                       # Finish line.
os.startfile(cwd + '/Screens/')
