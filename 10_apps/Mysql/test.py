import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()

word = input("Enter word: ")

definition = cursor.execute("SELECT DEFINITION FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()
c = 0
print(f'Your word was "{word}" your results are:')
if results:
    for result in results:
        c += 1
        print(str(c) + ": " + result[0])
else:
    print("No word found")

