from sshtunnel import SSHTunnelForwarder
import pymysql, os

SSH_HOST = os.getenv("SSH_HOST")
SSH_PORT = os.getenv("SSH_PORT")
SSH_USER = os.getenv("SSH_USER")
SSH_PASSWORD = os.getenv("SSH_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

with SSHTunnelForwarder(
    (SSH_HOST, SSH_PORT),
    ssh_username=SSH_USER,
    ssh_password=SSH_PASSWORD,
    remote_bind_address=(DB_HOST, int(DB_PORT)),
) as server:
    server.start()

    print("SSH tunnel established.")
    print("Local bind port:", server.local_bind_port)

    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
        database="blog",
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM blog.post;")
            result = cursor.fetchall()
            print(result)
            pass
    finally:
        connection.close()
    print("Database connection closed.")
    server.stop()
