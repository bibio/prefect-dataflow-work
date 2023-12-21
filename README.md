# prefect-dataflow-work

## Setup

1. Type bellow
```
prefect cloud login
pip install -r requirements.txt

docker compose up -d
```
2. Create Block AWS Credentials In Prefect Cloud UI.
1. Create Block SQLAlchemy Connection String.

```
python
> from prefect_sqlalchemy import SqlAlchemyConnector
> SqlAlchemyConnetor.new("postgresql+psycopg2://postgres:passw0rd@localhost:5432/testdb").save("connection")

prefect blocks ls
```

## Run

```
python import_rdb.py
```

## Deployment

(WIP)