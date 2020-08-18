import sqlite3

try:
    connection = sqlite3.connect('words.sqlite')
    cur = connection.cursor()
    print("Connected to SQLite")

    sqlite_select_query = '''SELECT * FROM Words'''
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    #print("Total rows are:  ", len(records))
    #print("Printing each row")
    for row in records:
        #print("Word: ", row[0])
        #print("Meaning: ", row[1])
        #print("Singular Nominativ: ", row[2])
        #print("Plural Nominativ: ", row[3])
        #print("Singular Genitiv: ",row[4])
        #print("Plural Genitiv: ", row[5])
        #print("Singular Daitv: ", row[6])
        #print("Plural Dativ: ", row[7])
        #print("Singular Akkusativ: ", row[8])
        #print("Plural Akkusativ: ", row[9])
        #print("\n")
        part = row[0]
        word = part[0:-5]
        cur.close()

except sqlite3.Error as error:
        print("Failed to read data from table", error)
finally:
    if (connection):
        connection.close()
        print("The Sqlite connection is closed")


def main():
    # ask the question
    question = {'What is the singular nominativ of' + ' ' + word + ' ':row[2], 'What is the plural nominativ of' + ' ' +  word + ' ':row[3], 'What is the singular genitiv of' + ' ' +  word + ' ':row[4], 'What is the plural genitiv of' + ' ' +  word + ' ':row[5], 'What is the singular dativ of' + ' ' +  word + ' ':row[6], 'What is the plural dativ of' + ' ' +  word + ' ':row[7], 'What is the singular akkusativ of' + ' ' +  word + ' ':row[8], 'What is the plural akkusativ of' + ' ' +  word + ' ':row[9]}
    print("*** Quiz ***\n")
    name = input("Please enter your name: ").title()
    print()
    # tell you the score
    print("\nWell done {0}, you scored {1} out of {2}.".format(name, quiz(question), len(question)))
def quiz(question):
    score = 0
    # determine if answer is correct or not
    for q,a in question.items():
        if input(q).lower() == a.lower():
            score += 1
            print("Correct.")
        else:
            print("Sorry, correct answer is \"{}\".".format(a))
    return score
if __name__ == "__main__":
    main()
