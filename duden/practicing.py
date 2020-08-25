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

row_number = '3'

#answers
cur.fetchall()
# select answer column
ans_sin_nom = cur.execute("SELECT singular_nominativ FROM Words WHERE rowid = \"" + row_number +"\"")
print(ans_sin_nom)
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
        'What is the singular nominativ of' + ' ' + word + ' ' : ans_sin_nom,
        'What is the plural nominativ of' + ' ' +  word + ' ' : ans_plu_nom,
        'What is the singular genitiv of' + ' ' +  word + ' ' : ans_sin_gen,
        'What is the plural genitiv of' + ' ' +  word + ' ' : ans_plu_gen,
        'What is the singular dativ of' + ' ' +  word + ' ' : ans_sin_dat,
        'What is the plural dativ of' + ' ' +  word + ' ' : ans_plu_dat,
        'What is the singular akkusativ of' + ' ' +  word + ' ' : ans_sin_akk,
        'What is the plural akkusativ of' + ' ' +  word + ' ' : ans_plu_akk
    }
    print("*** Quiz ***\n")
    name = input("Please enter your name: ").title()
    print()
    # tell you the score
    print("\nWell done {0}, you scored {1} out of {2}.".format(name, quiz(question), len(question)))
def quiz(question):
    # prompt the user for the question and check if answer is correct or not
    score = 0
    singular_nom = list(question)
    input(singular_nom[0])
    if singular_nom == ans_sin_nom:
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Singular_Nominative = Correction_Singular_Nominative-1 WHERE singular_nominativ = \"''' + word +"\"")
    else:
        print("Sorry, correct answer is \"{}\".".format(ans_sin_nom))
        sqlstring=('''UPDATE Words SET Correction_Singular_Nominative = Correction_Singular_Nominative+1 WHERE singular_nominativ = \"''' + word +"\"")
        correction = cur.execute(sqlstring)
        
    plural_nom = list(question)
    input(plural_nom[1])
    if plural_nom == ans_plu_nom:
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Plural_Nominative = Correction_Plural_Nominative-1 WHERE singular_nominativ = \"''' + word +"\"")
    else:
        print("Sorry, correct answer is \"{}\".".format(ans_plu_nom))
        sqlstring=('''UPDATE Words SET Correction_Plural_Nominative = Correction_Plural_Nominative+1 WHERE singular_nominativ = \"''' + word +"\"")
        correction = cur.execute(sqlstring)
    
    singular_gen = list(question)
    input(singular_gen[2])
    if singular_gen == ans_sin_gen:
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Singular_Genitiv = Correction_Singular_Genitiv-1 WHERE singular_nominativ = \"''' + word +"\"")
    else:
        print("Sorry, correct answer is \"{}\".".format(ans_sin_gen))
        sqlstring=('''UPDATE Words SET Correction_Singular_Genitiv = Correction_Singular_Genitiv+1 WHERE singular_nominativ = \"''' + word +"\"")
        correction = cur.execute(sqlstring)

    plural_gen = list(question)
    input(plural_gen[3])
    if plural_gen == ans_plu_gen:
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Plural_Genitiv = Correction_Plural_Genitiv-1 WHERE singular_nominativ = \"''' + word +"\"")
    else:
        print("Sorry, correct answer is \"{}\".".format(ans_plu_gen))
        sqlstring=('''UPDATE Words SET Correction_Plural_Genitiv = Correction_Plural_Genitiv+1 WHERE singular_nominativ = \"''' + word +"\"")
        correction = cur.execute(sqlstring)

    singular_dat = list(question)
    input(singular_dat[4])
    if singular_dat == ans_sin_dat:
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Singular_Dativ = Correction_Singular_Dativ-1 WHERE singular_nominativ = \"''' + word +"\"")
    else:
        print("Sorry, correct answer is \"{}\".".format(ans_sin_dat))
        sqlstring=('''UPDATE Words SET Correction_Singular_Dativ = Correction_Singular_Dativ+1 WHERE singular_nominativ = \"''' + word +"\"")
        correction = cur.execute(sqlstring)
    plural_dat = list(question)
    input(plural_dat[5])
    if plural_dat == ans_plu_dat:
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Plural_Dativ = Correction_Plural_Dativ-1 WHERE singular_nominativ = \"''' + word +"\"")
    else:
        print("Sorry, correct answer is \"{}\".".format(ans_plu_dat))
        sqlstring=('''UPDATE Words SET Correction_Plural_Dativ = Correction_Plural_Dativ+1 WHERE singular_nominativ = \"''' + word +"\"")
        correction = cur.execute(sqlstring)
    singular_akk = list(question)
    input(singular_akk[6])
    if singular_akk == ans_sin_akk:
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Singular_Akkusativ = Correction_Singular_Akkusativ-1 WHERE singular_nominativ = \"''' + word +"\"")
    else:
        print("Sorry, correct answer is \"{}\".".format(ans_sin_akk))
        sqlstring=('''UPDATE Words SET Correction_Singular_Akkusativ = Correction_Singular_Akkusativ+1 WHERE singular_nominativ = \"''' + word +"\"")
        correction = cur.execute(sqlstring)
    plural_akk = list(question)
    input(plural_akk[7])
    if plural_akk == ans_plu_akk:
        score += 1
        print("Correct.")
        sqlstring=('''UPDATE Words SET Correction_Plural_Akkusativ = Correction_Plural_Akkusativ-1 WHERE singular_nominativ = \"''' + word +"\"")
        correction = cur.execute(sqlstring)
    else:
        print("Sorry, correct answer is \"{}\".".format(ans_plu_akk))
        sqlstring=('''UPDATE Words SET Correction_Plural_Akkusativ = Correction_Plural_Akkusativ+1 WHERE singular_nominativ = \"''' + word +"\"")
        correction = cur.execute(sqlstring)
    conn.commit()
    conn.close()
    return score
if __name__ == "__main__":
    main()
