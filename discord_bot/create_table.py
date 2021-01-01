import psycopg2

from settings.settings import DATABASES


def create_tables():
    """ create user search table in the PostgreSQL database"""
    command = """
        CREATE TABLE user_search (
            user_search_id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            query VARCHAR(255) NOT NULL   
        )
    """
    conn = None
    try:
        # connect to the PostgresSQL server
        # conn = psycopg2.connect(
        #     host=DATABASES['HOST'],
        #     database=DATABASES['DB_NAME'],
        #     user=DATABASES['USER'],
        #     password=DATABASES['PASSWORD'],
        #     port=DATABASES['PORT']
        # )
        conn = psycopg2.connect(DATABASES['DATABASE_URL'], sslmode='require')
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        # commit the changes
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
