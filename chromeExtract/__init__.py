from termcolor import colored, cprint
import argparse

def print_art():
    cprint("""[=]                                                                               [=]    
[=]          ___ _                                __      _                  _    [=]
[=]     / __\ |__  _ __ ___  _ __ ___   ___  /__\_  _| |_ _ __ __ _  ___| |_      [=]
[=]    / /  | '_ \| '__/ _ \| '_ ` _ \ / _ \/_\ \ \/ / __| '__/ _` |/ __| __|     [=]
[=]   / /___| | | | | | (_) | | | | | |  __//__  >  <| |_| | | (_| | (__| |_      [=]
[=]   \____/|_| |_|_|  \___/|_| |_| |_|\___\__/ /_/\_\\\\__|_|  \__,_|\___|\__|     [=]
[=]                                                                               [=]    
[=]    By Mauro Baladés (https://github.com/mauro-balades/ChromeVaultExtract)     [=]    
[=]         You better not use this for something bad >:(                         [=]    
[=]                                                                               [=]    
[=]                                                                               [=]    
    """, "blue", attrs=["bold"])

def main():
    parser = argparse.ArgumentParser(description='Dump google chrome\'s passwords.')
    parser.add_argument('--output', '-o', dest='output',
                    help='Output file for the found accounts')
    args = parser.parse_args()

    print_art()

    if args.output is not None:
        #output_accounts(args.output, accounts)
        pass

main()