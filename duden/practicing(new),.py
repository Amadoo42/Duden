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
        'Singular_Nominative',
        'What is the plural nominativ of' + ' ' +  word + ' ' : nom_plu_ans[0],
        'Plural_Nominative',
        'What is the singular genitiv of' + ' ' +  word + ' ' : gen_sin_ans[0],
        'Singular_Genitiv',
        'What is the plural genitiv of' + ' ' +  word + ' ' : gen_plu_ans[0],
        'Plural_Genitiv',
        'What is the singular dativ of' + ' ' +  word + ' ' : dat_sin_ans[0],
        'Singular_Dativ',
        'What is the plural dativ of' + ' ' +  word + ' ' : dat_plu_ans[0],
        'Plural_Dativ',
        'What is the singular akkusativ of' + ' ' +  word + ' ' : akk_sin_ans[0],
        'Singular_Akkusativ',
        'What is the plural akkusativ of' + ' ' +  word + ' ' : akk_plu_ans[0],
        'Plural_Akkusativ'
    }
    for word_Form in range(1,8)
        ask_about_word_form(row_id, word_Form)

def ask_about_word_form(row_id, word_Form):
    # ask about one form
    score = 0
    singular_nom = list(question)
    sin_nom_ask = cur.execute("SELECT Correction_"+question[word_Form]+" FROM Words WHERE rowid = \"" + row_number +"\"")
    sin_nom_num = cur.fetchone()
    if sin_nom_num[0] > 0:
        singular_nom_inp = input(singular_nom[0])
        if singular_nom_inp == nom_sin_ans[0]:
            score += 1
            print("Correct.")
            sqlstring=('''UPDATE Words SET Correction_'''+question[word_Form]+''' = Correction_'''+question[word_Form]+"-1 WHERE singular_nominativ = \"" + nom_sin_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
        else:
            print("Sorry, correct answer is \"{}\".".format(nom_sin_ans[0]))
            sqlstring=('''UPDATE Words SET Correction_'''+question[word_Form]+''' = Correction_'''+question[word_Form]+"+1 WHERE singular_nominativ = \"" + nom_sin_ans[0] +"\"")
            correction = cur.execute(sqlstring)
            conn.commit()
    else:
        pass

    conn.close()
    return score
if __name__ == "__main__":
    fetching_words()
    ask_about_word(row_id)
    
