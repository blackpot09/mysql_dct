import mysql.connector
import sys #needed for exit() function
from difflib import get_close_matches

class bc:
    H = '\033[95m'
    OKB = '\033[94m'
    OKG = '\033[92m'
    W = '\033[93m'
    F = '\033[91m'
    E = '\033[0m'
    B = '\033[1m'
    U = '\033[4m'

lbreak = f"========================================================================"

print("\n" + lbreak)
print(f"                            {bc.B}{bc.F}I AM HERE{bc.E}")
print(lbreak)
print("\nEstablishing connection with MYSQL server...")

#establish connection
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

print("Connection established!\nEnjoy your personal dictionary.")
print(lbreak + "\n")

cursor = con.cursor()

def listit(mylist):
    a = 0
    print(f"{lbreak}\nResults for {bc.W}{mylist[0][0]}{bc.E}:\n")
    for r in mylist:
        a = a + 1
        print(f"{a}. {r[1]}")
    print(f"{lbreak}\n")    

def search(word):
    cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
    result = cursor.fetchall()
    return result

def typo(word):
    cursor.execute(f"SELECT Expression FROM Dictionary WHERE Expression LIKE '{word[0]}%'")
    result = cursor.fetchall()
    possible = set([r[0] for r in result])
    likely = get_close_matches(word, possible)[:3]
    return likely 

while True:
    word = input("Enter your word ('/q' to exit): ")
    if word[:2] == "/q".casefold(): sys.exit(f"\n{lbreak}\n{bc.F}Program terminated by user. Farewell.{bc.E}\n{lbreak}\n")
    if search(word): listit(search(word))
    elif typo(word):
        b = 0
        for r in typo(word):
            b = b + 1
            tin = input(f"Did you mean: {bc.W}{r.title()}{bc.E}? {bc.OKB}(Y/N){bc.E}: ")
            if tin.casefold()[:2] == "/q".casefold(): sys.exit(f"\n{lbreak}{bc.F}Program terminated by user. Farewell.{bc.E}{lbreak}\n")
            elif tin.casefold()[0] == "C".casefold():
                print("Cancelled by user.")
                break
            elif tin.casefold() == "Y".casefold(): 
                listit(search(r))
                break
            if b == len(typo(word)):
                 print(f"{lbreak}\nNo similar words found. Please try again.\n{lbreak}\n")
                 break
    else:
        print(f"\n{lbreak}\nNo word found.\n{lbreak}\n")
