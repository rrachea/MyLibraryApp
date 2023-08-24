"""
Script for interactions with database -- dB
"""

import psycopg2
from config import config

# connect to Postgres dB
conn = psycopg2.connect("dbname=suppliers user=postgres password=postgres")
# or can use an ini file, https://www.postgresqltutorial.com/postgresql-python/connect/

###### Useful Functions ######
def connect():
    """
    Function:
        - Connect to dB
    Output:
        - success / error message about connection
    """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

###### Python Script ######

if __name__ == '__main__':
    connect()