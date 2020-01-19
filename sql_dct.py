import mysql.connector
import sys #needed for exit() function

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

while True:
    word = input("Enter your word ('/q' to exit): ")
    if word[:2] == "/q".casefold(): sys.exit("Exiting module...")
    result = search(word)
    if result:
        for r in result:
            print(r)
    else:
        print("No word found.")