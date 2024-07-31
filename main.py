import argparse
from account import add_account, update_account_balance

parser = argparse.ArgumentParser(
                    prog='FinCLI',
                    description='FinCLI is a personal finance cli tool built in Python',
                    epilog='')

parser.add_argument('-c', '--create')
parser.add_argument('-b', '--balance')
parser.add_argument('-u', '--update')
parser.add_argument('-v', '--view')
args = parser.parse_args()

#Parse arg values
if(args.create and args.balance):
    add_account(args.create, args.balance)
if(args.update and args.balance):
    update_account_balance(args.update, args.balance)
else:
    print("No valid option was used")

