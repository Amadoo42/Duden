import sqlite3

try:
    conn = sqlite3.connect('words.sqlite')
    cur = conn.cursor()
    print("Connected to SQLite")

    sqlite_select_query = '''SELECT * FROM Words'''
    cur.execute(sqlite_select_query)
    records = cur.fetchall()
    for row in records:
        #This is the row in the sql database ('Katze, die', 'Hauskatze', 'die Katze')
        part = row[0]
        word = part[0:-5]

except sqlite3.Error as error:
        print("Failed to read data from table", error)

# prompt the user for the question
singular_nom = 'What is the singular nominativ of' + ' ' + word + ' '
plural_nom = 'What is the plural nominativ of' + ' ' +  word + ' '
singular_gen = 'What is the singular genitiv of' + ' ' +  word + ' '
plural_gen = 'What is the plural genitiv of' + ' ' +  word + ' '
singular_dat = 'What is the singular dativ of' + ' ' +  word + ' '
plural_dat = 'What is the plural dativ of' + ' ' +  word + ' '
singular_akk = 'What is the singular akkusativ of' + ' ' +  word + ' '
plural_akk = 'What is the plural akkusativ of' + ' ' +  word + ' '


row_number = '3'

#answers
cur.fetchall()
# select answer column
ans_sin_nom = cur.execute("SELECT singular_nominativ FROM Words WHERE rowid = \"" + row_number +"\"")
ans_plu_nom = cur.execute("SELECT plural_nominativ FROM Words WHERE rowid = \"" + row_number +"\"")
ans_sin_gen = cur.execute("SELECT singular_genitiv FROM Words WHERE rowid = \"" + row_number +"\"")
ans_plu_gen = cur.execute("SELECT genitiv_plural FROM Words WHERE rowid = \"" + row_number +"\"")
ans_sin_dat = cur.execute("SELECT singular_dativ FROM Words WHERE rowid = \"" + row_number +"\"")
ans_plu_dat = cur.execute("SELECT plural_dativ FROM Words WHERE rowid = \"" + row_number +"\"")
ans_sin_akk = cur.execute("SELECT singular_akkusativ FROM Words WHERE rowid = \"" + row_number +"\"")
ans_plu_akk = cur.execute("SELECT akkusativ_plural FROM Words WHERE rowid = \"" + row_number +"\"")

def main():
    # ask the question
    question = {
        input(singular_nom),
        input(plural_nom),
        input(singular_gen),
        input(plural_gen),
        input(singular_dat),
        input(plural_dat),
        input(singular_akk),
        input(plural_akk)
    }
    print("*** Quiz ***\n")
    name = input("Please enter your name: ").title()
    print()
    # tell you the score
    print("\nWell done {0}, you scored {1} out of {2}.".format(name, quiz(question), len(question)))
def quiz(question):
    score = 0
    # determine if answer is correct or not
    if q.lower() == ans_sin_nom.lower():
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Singular_Nominative = Correction_Singular_Nominative-1 WHERE singular_nominativ = \"''' + a +"\"")
    if q.lower() == ans_plu_nom.lower():
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Plural_Nominative = Correction_Plural_Nominative-1 WHERE singular_nominativ = \"''' + a +"\"")
    if q.lower() == ans_sin_gen.lower():
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Singular_Genitiv = Correction_Singular_Genitiv-1 WHERE singular_nominativ = \"''' + a +"\"")
    if q.lower() == ans_plu_gen.lower():
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Plural_Genitiv = Correction_Plural_Genitiv-1 WHERE singular_nominativ = \"''' + a +"\"")
    if q.lower() == ans_sin_dat.lower():
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Singular_Dativ = Correction_Singular_Dativ-1 WHERE singular_nominativ = \"''' + a +"\"")
    if q.lower() == ans_plu_dat.lower():
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Plural_Dativ = Correction_Plural_Dativ-1 WHERE singular_nominativ = \"''' + a +"\"")
    if q.lower() == ans_sin_akk.lower():
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Singular_Akkusativ = Correction_Singular_Akkusativ-1 WHERE singular_nominativ = \"''' + a +"\"")
    if q.lower() == ans_plu_akk.lower():
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Plural_Akkusativ = Correction_Plural_Akkusativ-1 WHERE singular_nominativ = \"''' + a +"\"")
    
        correction = cur.execute(sqlstring)
        conn.commit()
        conn.close()
    else:
        print("Sorry, correct answer is \"{}\".".format(a))
        sqlstring=('''UPDATE Words SET Correction_Singular_Nominative = Correction_Singular_Nominative+1 WHERE singular_nominativ = \"''' + a +"\"")
    return score
if __name__ == "__main__":
    main()
