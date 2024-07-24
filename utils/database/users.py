import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        host='localhost',
        port = 5432,
        database='group4',
        user='postgres',
        password='aznur151'
    )
    conn.autocommit=True
    return conn

def close_db_connection(conn):
    if conn:
        conn.close()


def create_user(user_id, fio):
    conn=connect_to_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        insert into users (user_id, fio) values ('{user_id}','{fio}');
        """)


    close_db_connection(conn)

def update_user_phone(user_id, phone):
    conn=connect_to_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        update users set phone=('{phone}') where user_id=('{user_id}');
        """)
    close_db_connection(conn)
#

def update_user_location(user_id, long, lat):
    conn=connect_to_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        update users set long='{long}',lat='{lat}' where user_id=('{user_id}');
        """)
    close_db_connection(conn)
def update_user(user_id, fio):
    conn=connect_to_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        update users set fio=('{fio}') where user_id=('{user_id}');
        """)
    close_db_connection(conn)

def delete_user(user_id):
    conn=connect_to_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        delete from users where user_id=('{user_id}');
        """)
    close_db_connection(conn)

def get_user(user_id):
    conn=connect_to_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        select * from users where user_id=('{user_id}');
        """)
        res=cursor.fetchone()
    close_db_connection(conn)
    return res

def get_users_all():
    conn=connect_to_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        select * from users;
        """)
        res=cursor.fetchall()
    close_db_connection(conn)
    return res
