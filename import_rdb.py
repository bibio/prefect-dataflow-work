from prefect import flow, task
from prefect_sqlalchemy import SqlAlchemyConnector

@task(log_prints=True)
def create_table(conn: SqlAlchemyConnector):
    conn.execute(
        "CREATE TABLE IF NOT EXISTS hello_prefect (id INTEGER PRIMARY KEY, name TEXT)"
    )

@task(log_prints=True)
def load_data(conn: SqlAlchemyConnector):
    copy_sql = "COPY hello_prefect FROM STDIN DELIMITERS ','"
    with conn.get_client(client_type="connection") as sa_conn:
        with open("data.csv", "r") as f:
            sa_conn.connection.cursor().copy_expert(copy_sql, f)

@flow(log_prints=True)
def hello_prefect():
    conn =  SqlAlchemyConnector.load("connection")
    create_table(conn)
    load_data(conn)


if __name__ == "__main__":
    hello_prefect()
