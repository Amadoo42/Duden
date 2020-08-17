import sqlite3

conn = sqlite3.connect('words.sqlite')
cur = conn.cursor()

# insert data from database into file
cur.execute("SELECT rowid, singular_nominativ FROM Words ORDER BY rowid")
cur.execute("SELECT rowid, plural_nominativ FROM Words ORDER BY rowid")
cur.execute("SELECT rowid, singular_genitiv FROM Words ORDER BY rowid")
cur.execute("SELECT rowid, genitiv_plural FROM Words ORDER BY rowid")
cur.execute("SELECT rowid, singular_dativ FROM Words ORDER BY rowid")
cur.execute("SELECT rowid, plural_dativ FROM Words ORDER BY rowid")
cur.execute("SELECT rowid, singular_akkusativ FROM Words ORDER BY rowid")
cur.execute("SELECT rowid, akkusativ_plural FROM Words ORDER BY rowid")

words = cur.fetchmany(20)
singular_nom = cur.fetchone()
plural_nom = cur.fetchone()
singular_gen = cur.fetchone()
plural_gen = cur.fetchone()
singular_dat = cur.fetchone()
plural_dat = cur.fetchone()
singular_akk = cur.fetchone()
plural_akk = cur.fetchone()

def main():
    # ask the question
    question = {'singular nominativ of' + words + ' ':singular_nom[1]}
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

