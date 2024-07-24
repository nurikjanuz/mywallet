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


def create_operation(user_id, operation_type, operation_comment, operation_sum):
    conn=connect_to_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        insert into operations (user_id, operation_type, operation_comment, sum) values 
        ('{user_id}','{operation_type}','{operation_comment}','{operation_sum}');
        """)


    close_db_connection(conn)


def get_operations(user_id):
    conn=connect_to_db()

    with conn.cursor() as cursor:
        cursor.execute(f"""
        select * from operations where user_id=('{user_id}');
        """)
        res=cursor.fetchall()
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
