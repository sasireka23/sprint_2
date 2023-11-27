import sqlite3
import queries as q
import pandas as pd

#DB Connect function
def connect_to_db(db_name = 'rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

#Execute the query function
def execute_q(conn, query):
    cursr = conn.cursor()
    cursr.execute(query)
    return cursr.fetchall()


if __name__ == '__main__':
    conn = connect_to_db()
    result = execute_q(conn, q.SELECT_AVG_ITEM_WEIGHT)

    df = pd.DataFrame(result)
    df.columns = ['name','avg_item_weight']
    print(df.head())
    df.to_csv('rpg_db.csv')
