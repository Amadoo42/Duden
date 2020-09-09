import sqlite3

def fetching_words():
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
def ask_about_word(row_id):
    # ask the user about the word 8 forms
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

def ask_about_word_form(row_id, word_Form):
    # ask about one form
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
    conn.close()
    return score
if __name__ == "__main__":
    fetching_words()
    ask_about_word(row_id)
    ask_about_word_form(row_id, word_Form)
