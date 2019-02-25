import sqlite3

conn = sqlite3.connect('raffle.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS Name;

CREATE TABLE Name (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT
);
''')
while True:
    entrant = raw_input('Enter name: ')
    if ( len(entrant) < 1 ) : break
    entries =int(raw_input('Number of entries: '))


    for entry in range(entries):
        print "Loading....Please Wait"
        cur.execute('''INSERT INTO Name (name)
            VALUES ( ? )''', ( entrant, ) )
        cur.execute('SELECT id FROM Name WHERE name = ? ', (entrant, ))
        entrant_id = cur.fetchone()[0]
        conn.commit()
cur.execute('''SELECT name FROM Name ORDER BY RANDOM() LIMIT 1''')
winner = cur.fetchone()[0]
print winner + " is the winner!"
