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
# select answer column and transform the answer into word for
ans_sin_nom = cur.execute("SELECT singular_nominativ FROM Words WHERE rowid = \"" + row_number +"\"")
nom_sin_ans = cur.fetchone()
ans_plu_nom = cur.execute("SELECT plural_nominativ FROM Words WHERE rowid = \"" + row_number +"\"")
nom_plu_ans = cur.fetchone()
ans_sin_gen = cur.execute("SELECT singular_genitiv FROM Words WHERE rowid = \"" + row_number +"\"")
gen_sin_ans = cur.fetchone()
ans_plu_gen = cur.execute("SELECT genitiv_plural FROM Words WHERE rowid = \"" + row_number +"\"")
gen_plu_ans = cur.fetchone()
ans_sin_dat = cur.execute("SELECT singular_dativ FROM Words WHERE rowid = \"" + row_number +"\"")
dat_sin_ans = cur.fetchone()
ans_plu_dat = cur.execute("SELECT plural_dativ FROM Words WHERE rowid = \"" + row_number +"\"")
dat_plu_ans = cur.fetchone()
ans_sin_akk = cur.execute("SELECT singular_akkusativ FROM Words WHERE rowid = \"" + row_number +"\"")
akk_sin_ans = cur.fetchone()
ans_plu_akk = cur.execute("SELECT akkusativ_plural FROM Words WHERE rowid = \"" + row_number +"\"")
akk_plu_ans = cur.fetchone()

def main():
    # ask the question
    question = {
        'What is the singular nominativ of' + ' ' + word + ' ' : nom_sin_ans[0],
        'What is the plural nominativ of' + ' ' +  word + ' ' : nom_plu_ans[0],
        'What is the singular genitiv of' + ' ' +  word + ' ' : gen_sin_ans[0],
        'What is the plural genitiv of' + ' ' +  word + ' ' : gen_plu_ans[0],
        'What is the singular dativ of' + ' ' +  word + ' ' : dat_sin_ans[0],
        'What is the plural dativ of' + ' ' +  word + ' ' : dat_plu_ans[0],
        'What is the singular akkusativ of' + ' ' +  word + ' ' : akk_sin_ans[0],
        'What is the plural akkusativ of' + ' ' +  word + ' ' : akk_plu_ans[0]
    }
    print("*** Quiz ***\n")
    name = input("Please enter your name: ").title()
    print()
    # Tell you the score
    print("\nWell done {0}, you scored {1} out of {2}.".format(name, quiz(question), len(question)))
def quiz(question):
    row_number = '3'
    # Prompt the user for the question and check if answer is correct or not
    score = 0
    singular_nom = list(question)
    sin_nom_ask = cur.execute("SELECT Correction_Singular_Nominative FROM Words WHERE rowid = \"" + row_number +"\"")
    sin_nom_num = cur.fetchone()
    if sin_nom_num[0] > 0:
        singular_nom_inp = input(singular_nom[0])
        if singular_nom_inp == nom_sin_ans[0]:
            score += 1
            print("Correct.")
            sqlstring=('''UPDATE Words SET Correction_Singular_Nominative = Correction_Singular_Nominative-1 WHERE singular_nominativ = \"''' + nom_sin_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
        else:
            print("Sorry, correct answer is \"{}\".".format(nom_sin_ans[0]))
            sqlstring=('''UPDATE Words SET Correction_Singular_Nominative = Correction_Singular_Nominative+1 WHERE singular_nominativ = \"''' + nom_sin_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
    else:
        pass

    plural_nom = list(question)
    plu_nom_ask = cur.execute("SELECT Correction_Plural_Nominative FROM Words WHERE rowid = \"" + row_number +"\"")
    plu_nom_num = cur.fetchone()
    if plu_nom_num[0] > 0:
        plural_nom_inp = input(plural_nom[1])
        if plural_nom_inp == nom_plu_ans[0]:
            score += 1
            print("Correct.")
            sqlstring=('''UPDATE Words SET Correction_Plural_Nominative = Correction_Plural_Nominative-1 WHERE plural_nominativ = \"''' + nom_plu_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
        else:
            print("Sorry, correct answer is \"{}\".".format(nom_plu_ans[0]))
            sqlstring=('''UPDATE Words SET Correction_Plural_Nominative = Correction_Plural_Nominative+1 WHERE plural_nominativ = \"''' + nom_plu_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
    else:
        pass
    
    singular_gen = list(question)
    sin_gen_ask = cur.execute("SELECT Correction_Singular_Genitiv FROM Words WHERE rowid = \"" + row_number +"\"")
    sin_gen_num = cur.fetchone()
    if sin_gen_num[0] > 0:
        singular_gen_inp = input(singular_gen[2])
        if singular_gen_inp == gen_sin_ans[0]:
            score += 1
            print("Correct.")
            sqlstring=('''UPDATE Words SET Correction_Singular_Genitiv = Correction_Singular_Genitiv-1 WHERE singular_genitiv = \"''' + gen_sin_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
        else:
            print("Sorry, correct answer is \"{}\".".format(gen_sin_ans[0]))
            sqlstring=('''UPDATE Words SET Correction_Singular_Genitiv = Correction_Singular_Genitiv+1 WHERE singular_genitiv = \"''' + gen_sin_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
    else:
        pass

    plural_gen = list(question)
    plu_gen_ask = cur.execute("SELECT Correction_Plural_Genitiv FROM Words WHERE rowid = \"" + row_number +"\"")
    plu_gen_num = cur.fetchone()
    if plu_gen_num[0] > 0:
        plural_gen_inp = input(plural_gen[3])
        if plural_gen_inp == gen_plu_ans[0]:
            score += 1
            print("Correct.")
            sqlstring=('''UPDATE Words SET Correction_Plural_Genitiv = Correction_Plural_Genitiv-1 WHERE genitiv_plural = \"''' + gen_plu_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
        else:
            print("Sorry, correct answer is \"{}\".".format(gen_plu_ans[0]))
            sqlstring=('''UPDATE Words SET Correction_Plural_Genitiv = Correction_Plural_Genitiv+1 WHERE genitiv_plural = \"''' + gen_plu_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
    else:
        pass

    singular_dat = list(question)
    sin_dat_ask = cur.execute("SELECT Correction_Singular_Dativ FROM Words WHERE rowid = \"" + row_number +"\"")
    sin_dat_num = cur.fetchone()
    if sin_dat_num[0] > 0:
        singular_dat_inp = input(singular_dat[4])
        if singular_dat_inp == dat_sin_ans[0]:
            score += 1
            print("Correct.")
            sqlstring=('''UPDATE Words SET Correction_Singular_Dativ = Correction_Singular_Dativ-1 WHERE singular_dativ = \"''' + dat_sin_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
        else:
            print("Sorry, correct answer is \"{}\".".format(dat_sin_ans[0]))
            sqlstring=('''UPDATE Words SET Correction_Singular_Dativ = Correction_Singular_Dativ+1 WHERE singular_dativ = \"''' + dat_sin_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
    else: 
        pass
    plural_dat = list(question)
    plu_dat_ask = cur.execute("SELECT Correction_Plural_Dativ FROM Words WHERE rowid = \"" + row_number +"\"")
    plu_dat_num = cur.fetchone()
    if plu_dat_num[0] > 0:
        plural_dat_inp = input(plural_dat[5])
        if plural_dat_inp == dat_plu_ans[0]:
            score += 1
            print("Correct.")
            sqlstring=('''UPDATE Words SET Correction_Plural_Dativ = Correction_Plural_Dativ-1 WHERE plural_dativ = \"''' + dat_plu_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
        else:
            print("Sorry, correct answer is \"{}\".".format(dat_plu_ans[0]))
            sqlstring=('''UPDATE Words SET Correction_Plural_Dativ = Correction_Plural_Dativ+1 WHERE plural_dativ = \"''' + dat_plu_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
    else:
        pass
    singular_akk = list(question)
    sin_akk_ask = cur.execute("SELECT Correction_Singular_Akkusativ FROM Words WHERE rowid = \"" + row_number +"\"")
    sin_akk_num = cur.fetchone()
    if sin_akk_num[0] > 0:
        singular_akk_inp = input(singular_akk[6])
        if singular_akk_inp == akk_sin_ans[0]:
            score += 1
            print("Correct.")
            sqlstring=('''UPDATE Words SET Correction_Singular_Akkusativ = Correction_Singular_Akkusativ-1 WHERE singular_akkusativ = \"''' + akk_sin_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
        else:
            print("Sorry, correct answer is \"{}\".".format(akk_sin_ans[0]))
            sqlstring=('''UPDATE Words SET Correction_Singular_Akkusativ = Correction_Singular_Akkusativ+1 WHERE singular_akkusativ = \"''' + akk_sin_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
    else:
        pass
    plural_akk = list(question)
    plu_akk_ask = cur.execute("SELECT Correction_Plural_Akkusativ FROM Words WHERE rowid = \"" + row_number +"\"")
    plu_akk_num = cur.fetchone()
    if plu_akk_num[0] > 0:
        plural_akk_inp = input(plural_akk[7])
        if plural_akk_inp == akk_plu_ans[0]:
            score += 1
            print("Correct.")
            sqlstring=('''UPDATE Words SET Correction_Plural_Akkusativ = Correction_Plural_Akkusativ-1 WHERE akkusativ_plural = \"''' + akk_plu_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
        else:
            print("Sorry, correct answer is \"{}\".".format(akk_plu_ans[0]))
            sqlstring=('''UPDATE Words SET Correction_Plural_Akkusativ = Correction_Plural_Akkusativ+1 WHERE akkusativ_plural = \"''' + akk_plu_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
    else:
        pass
    conn.close()
    return score
if __name__ == "__main__":
    main()
