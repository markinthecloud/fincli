import sqlite3
from db import connect_db
#from tabulate import tabulate

def add_account(name:str, balance:float):
    #
    # TODO: Prevent duplicate account names being added
    #
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, balance))
    conn.commit()
    conn.close()
    print(f"Account '{name}' added with balance {balance}.")

def update_account_balance(name:str, balance:float):
    #
    # TODO: Check account exists before making db call
    #
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE accounts SET balance = (?) WHERE name = (?)", (balance, name))
    conn.commit()
    conn.close()
    print(f"Account '{name}' updated with balance {balance}.")  
