import sqlite3
import queries as q

#step 1 - connect to the database

connection =  sqlite3.connect('rpg_db.sqlite3')

#step 2 - make the cursor

cursor = connection.cursor()

#step3 - write the query


#step 4 - execute the query

results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])
