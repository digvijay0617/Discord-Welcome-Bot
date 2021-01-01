import psycopg2

from settings.settings import DATABASES


class DbConnection:
    """
    Class to handle all db operations.
    """
    conn = None

    def __init__(self):
        try:
            # connect to the PostgresSQL server
            self.conn = psycopg2.connect(
                host=DATABASES['HOST'],
                database=DATABASES['DB_NAME'],
                user=DATABASES['USER'],
                password=DATABASES['PASSWORD'],
                port=DATABASES['PORT']
            )
        except Exception as error:
            print(error)

    def insert_data(self, user_id, query):
        """
        Method in insert data in user search table
        :param user_id: User id integer
        :param query: query string
        :return: None
        """
        try:
            cursor = self.conn.cursor()
            postgres_insert_query = """ INSERT INTO user_search (USER_ID, QUERY) VALUES (%s,%s)"""
            record_to_insert = (user_id, query)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.conn.commit()
            count = cursor.rowcount
            print(count, 'Record inserted successfully into user search table')
        except Exception as error:
            print('Failed to insert record into user search table', error)
        finally:
            # closing database connection.
            if (self.conn):
                cursor.close()
                self.conn.close()
                print("PostgreSQL connection is closed")

    def get_data(self, user_id, search):
        """
        Method to get the recent search data from user search table
        :param user_id: User id integer
        :param search: user search string
        :return:
        """
        try:
            cursor = self.conn.cursor()
            postgres_insert_query = """ SELECT QUERY from user_search where USER_ID = %s and QUERY LIKE %s"""
            record_to_insert = (user_id, '%'+search+'%')
            cursor.execute(postgres_insert_query, record_to_insert)
            records = cursor.fetchall()
            count = cursor.rowcount
            print(count, 'Record inserted successfully into user search table')
            return [record[0] for record in records], False
        except Exception as error:
            print('Failed to search record into user search table', error)
        finally:
            # closing database connection.
            if self.conn:
                cursor.close()
                self.conn.close()
                print("PostgreSQL connection is closed")
        return [], True
