import requests                             #   GET / POST request libraries.
from requests.exceptions import HTTPError   #   Exceptions for above. I don't think this is required anymore.
import urllib3                              #   urllib3 Library for added control.
import pandas as pd                         #   PANDAS dataframes.
import numpy as np                          #   Numpy matrixes.
import sys                                  #   Sys control to exit script - call with sys.exit()
import os                                   #   os architecture
import pprint                               #   Better console printing
import dns.resolver
from colorama import *
import datetime

init(autoreset=True) 
# Section 1.0 - Controls
urllib3.disable_warnings()                  # Disable warning for unverified connections. If removed you will need to change the verify=False to True in GET

# Section 1.1 - Function Setups 
    # PrintSplash is to display the title and version information in the console
    # ContinueCheck is a function that checks Y / N answers from user input
    # StartScan triggers the scan
    # SortResults puts your response strings into a PANDAS dataframe and prints to .csv
    
def PrintSplash():
    print(Fore.MAGENTA + """
    #######################################################
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #       """+Fore.WHITE+"""            LATK SCANNER """+Fore.MAGENTA+"""                     #
    #      """+Fore.WHITE+"""          BY LA-TK FOR DTO-TK    """+Fore.MAGENTA+"""              #
    #                                                     #
    #      """+Fore.WHITE+"""         DECEMBER 2019 BUILD 1  """+Fore.MAGENTA+"""               #
    #                                                     #
    #        S U C C U M B   T O   T H E   V O I D        #
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    #######################################################  
    """) 

def ContinueCheck(q):
    while "the answer is invalid":
        reply = str(input(q + ' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            print(Fore.MAGENTA + 'Execution cancelled.')
            sys.exit(0)
            return False
    
def StartScan():
    global totalResults
    for site in Websites:
        try:
            a = datetime.datetime.now()
            response = requests.get(site,verify=False,timeout=10).text
            b = datetime.datetime.now()
            c = b - a
            print(Fore.MAGENTA + '\nCHECKED : '+ Fore.YELLOW + str(site).upper() + Fore.WHITE + ' === ' + str(c.seconds) + ' seconds')
            #print(response)
            for Results in FingerPrints:
                if Results in response:
                    print(Fore.GREEN + 'VULNERABILITY DETECTED : ' + Fore.YELLOW + Results + ' : ' + Fore.WHITE + site)
                    ResultArray.append('VULNERABILITY DETECTED||' + Results + '||' + site)
                    #GetDNSInfo(site)
                    totalResults = totalResults + 1
        except Exception as e:
            a='error'
            
# def GetDNSInfo(url):
#     ids = ['A','CNAME']
#     for a in ids:
#         try:
#             answers = dns.resolver.query(url, a)
#             for rdata in answers:
#                 print('\n'+a, ':', rdata.to_text())
#                 print(answers.qname)

#         except Exception as e:
#             print(e)  # or pass

def SortResults():
    df = pd.DataFrame(ResultArray)            
    df.to_csv('ScannerResults.csv')
    print(Fore.GREEN + '\nScannerResults.csv successfully written into working directory! TIP: Separate CSV columns on || identifier')
    #print(Fore.GREEN + 'TIP: Separate CSV columns on || identifier')

# Section 1.2 - Arrays ( From Notepads )
 
with open(r"fingerprints.txt","r") as fd:
    FingerPrints = fd.read().splitlines()
with open(r"websites.txt","r") as fd:
    Websites = fd.read().splitlines()
with open(r"subdomains.txt","r") as fd:
    SubDomains = fd.read().splitlines()

# Section 2.0 - Program Start and Function calls where required.    #print(len( LIST NAME ))
totalResults = 0

ResultArray = ['Status,Fingerprint,URL']                            # Add headers for .csv export
PrintSplash()                                                       # Call PrintSplash function (1.1)
ContinueCheck('Are you sure you want to run this?')                 # Confirm program start.
StartScan()                                                         # Call StartScan function (1.1)
print(str(Fore.MAGENTA + 'Scan completed ' + Fore.WHITE + str(totalResults) + ' Fingerprints Found'))   # Show results (decide whether to export..)
ContinueCheck(Fore.MAGENTA + 'Scan complete. Do you want to save this data?')     # Confirm data export.
SortResults()                                                       # Call SortResults function (1.1)
