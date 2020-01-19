import mysql.connector
import sys #needed for exit() function
from difflib import SequenceMatcher


#establish connection
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

def search(word):
    cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
    result = cursor.fetchall()
    return result

def typo(word):
    cursor.execute(f"SELECT * FROM Dictionary WHERE Expression LIKE '{word[0]}%'")
    result = cursor.fetchall()
    #print(f"result = {type(result)}")
    past_r = ()
    for r in result:
        if r == past_r:
            result.remove(r)
        past_r = r
    return result

while True:
    word = input("Enter your word ('/q' to exit): ")
    if word[:2] == "/q".casefold(): sys.exit("Exiting module...")
    result = search(word)
    if result:
        a = 0
        print(f"Results for '{word}':")
        for r in result:
            a = a + 1
            print(f"{a}. {r[1]}")
    elif typo(word):
        a = 0
        print(f"Possible matches for '{word}':")
        for r in typo(word):
            a = a + 1
            print(f"{a}. {r[0]}")            
    else:
        print("No word found.")