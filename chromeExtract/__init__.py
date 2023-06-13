from termcolor import colored, cprint
import argparse

def main():
    parser = argparse.ArgumentParser(description='Dump google chrome\'s passwords.')
    parser.add_argument('--output', '-o', dest='output',
                    help='Output file for the found accounts')
    args = parser.parse_args()

    if args.output is not None:
        #output_accounts(args.output, accounts)
        pass